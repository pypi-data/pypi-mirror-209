import re
from typing import Callable

from bs4 import BeautifulSoup, Tag

from .classes import *

DOCSTRING_PATTERN: Callable[[str], str] = (
    lambda x: r"(" + x + r"\(.*\)(?:\s*->\s*(.*?))?\s*:(?!:))"
)


class Find:
    """Collection of functions to find elements in the HTML tree of the RDKit documentation"""

    @staticmethod
    def name(node: Tag) -> str:
        return node.find("span", class_="sig-name descname").get_text().strip()

    @staticmethod
    def base(node: Tag) -> str:
        base = node.find("code", class_="py-class")
        if base:
            return base.get_text().strip()
        else:
            return ""

    @staticmethod
    def params(node: Tag) -> list[str]:
        params = node.find_all("em", class_="sig-param")
        return [p.get_text().strip() for p in params]

    @staticmethod
    def attributes(node: Tag) -> list[str]:
        attributes = node.findChildren("dl", class_="py attribute", recursive=False)
        return [a.get_text().strip().replace("¶", "") for a in attributes]

    @staticmethod
    def docstring(node: Tag, classes: list[str]) -> str:
        first = node.find("dl", {"class": classes})

        if first:
            docstring_nodes = first.findPreviousSiblings()[::-1]
        else:
            docstring_nodes = node.findChildren(recursive=False)

        docstring = "\n".join([x.get_text() for x in docstring_nodes[1:]])

        return re.sub(r"\n\n\n+", "\n\n", docstring).strip()

    @staticmethod
    def func_docstring(node: Tag) -> str:
        docstring = node.find("dd").get_text()
        return re.sub(r"\n\n\n+", "\n\n", docstring).strip()

    @staticmethod
    def returns(node: Tag) -> str:
        returns = node.find("span", class_="sig-return")
        if returns:
            return returns.get_text().strip()
        else:
            return ""

    @staticmethod
    def overloads(docstring: str, name: str) -> list[str]:
        overloads: list[str] = []
        while docstring_contains_func := re.search(DOCSTRING_PATTERN(name), docstring):
            fn_def = docstring_contains_func.group(1)
            # :: = C++ synthax
            if not "::" in fn_def:
                ## HARD CODED (Alternative: exlude lines starting with >>>)
                if not "EnumerateHeterocycles" in fn_def:
                    overloads.append(fn_def.strip())
            _, docstring = docstring.split(fn_def, 1)
        return overloads

    @staticmethod
    def functions(node: Tag, method=False) -> list[FoundFunction]:
        class_ = "py method" if method else "py function"
        return [
            Find.function(node)
            for node in node.findChildren("dl", class_=class_, recursive=False)
        ]

    @staticmethod
    def function(node: Tag) -> FoundFunction:
        name = Find.name(node)
        params = Find.params(node)
        returns = Find.returns(node)
        doc = Find.func_docstring(node)
        overloads = Find.overloads(doc, name)
        return FoundFunction(name, params, returns, doc, overloads)

    @staticmethod
    def classes(node: Tag) -> list[FoundClass]:
        classes = node.findChildren("dl", class_="py class", recursive=False)
        exceptions = node.findChildren("dl", class_="py exception", recursive=False)
        classes = classes + exceptions
        return [Find.cls(c) for c in classes]

    @staticmethod
    def cls(node: Tag) -> FoundClass:
        name = Find.name(node)

        node = node.find("dd")

        base = Find.base(node)
        doc = Find.docstring(node, ["py method", "py attribute", "py class"])

        methods = Find.functions(node, method=True)
        attributes = Find.attributes(node)
        subclasses = Find.classes(node)

        return FoundClass(name, base, doc, subclasses, methods, attributes)

    def module(
        data: str,
    ) -> tuple[str, list[FoundClass], list[FoundFunction],]:
        soup = BeautifulSoup(data, "html.parser")
        node = soup.find("section")

        doc = Find.docstring(node, ["py exception", "py class", "py function"])

        classes = Find.classes(node)

        functions = Find.functions(node)

        return doc, functions, classes
