import ast
import os
import re

import black
import isort

NONE_PATTERN = re.compile(r"(?<!>\s)None:")


def shift(string: str, level: int, pad: str) -> str:
    """Shifts each line of a string to the right by level * PAD spaces"""
    pad = level * pad
    return pad + f"\n{pad}".join(string.split("\n")) + "\n"


def format_and_sort(code: str) -> str:
    """Formats and sorts the code using isort and black"""
    code = isort.code(code)
    code = black.format_str(code, mode=black.Mode(is_pyi=True))
    return code


def parse_base(path: str) -> ast.Module:
    """Parses the base stub file"""
    base = open(path).read()

    ## HARD CODED
    base = base.replace("(anonymousnamespace)", "anonymousnamespace")
    base = re.sub(NONE_PATTERN, "None_:", base)
    base = base.replace("used to filter multiple conformations", "Any")

    return ast.parse(base)


def unparse_and_format(x: ast.AST) -> str:
    """Unparses the AST and formats the code"""
    code = ast.unparse(x).strip()
    return format_and_sort(code)


def find_path(dir: str, stmt: str) -> str:
    """Finds the path of a module or package from an import statement in a specific directory"""
    path = dir + "/" + stmt.replace(".", "/")

    if os.path.isdir(path):
        path += "/__init__.pyi"
    else:
        path += ".pyi"

    return path
