import re
from typing import Callable


class InferTypes:
    def __init__(self, module_name: str) -> None:
        self.module_name = module_name

        # Initialize needed imports set
        self.imports: set[str] = set()

        # Initialize replacement counter and dict
        self.repl_counter = 0
        self.repl: dict[int, str] = {}

        self.PST: tuple[tuple[str, str, str, Callable]] = (
            ("(", ")", "tuple", self.infer_lts),
            ("[", "]", "list", self.infer_lts),
            ("{", "}", "dict", self.infer_dict),
            ("<", ">", "", self.infer_classvar),
        )

    def store_match(self, match: re.Match) -> str:
        """Store match in dict and return numbered replacement"""

        self.repl_counter += 1
        self.repl[self.repl_counter] = match.group(0)
        return f"__§§{self.repl_counter}__"

    def replace(self, x: str):
        """Replace strings, tuples, lists, dicts with numbered replacements"""

        prev = None
        while prev != x:
            prev = x
            # Replace strings
            x = re.sub(r"('.*?')", self.store_match, x, 1)

            # Replace tuples, lists, dicts
            for p, s in zip("[(}", "])}"):
                x = re.sub(f"\\{p}.*?\\{s}", self.store_match, x, 1)

        return x

    def first_element(self, x: str):
        """Return first element of a tuple, list, dict"""

        # First replace all strings, tuples, lists, dicts with numbered replacements
        x = self.replace(x)

        # Split at comma and return first element
        return x.split(",")[0].strip()

    def first_element_dict(self, x: str):
        """Return first element of a dict"""

        # Get the first element of the dict
        x = self.first_element(x)

        # Split at colon and return key, value
        k, v = x.split(":")
        return k.strip(), v.strip()

    def _infer_lstd(self, x: str, p: str, s: str, dict=False):
        """Private method to infer list, tuple, set, dict"""

        # Remove prefix and suffix
        x = x.removeprefix(p).removesuffix(s)

        # If x is empty, return Any
        if x == "":
            self.imports.add("Any")
            return "Any" if not dict else "Any, Any"

        # Else return first element
        x = self.first_element(x) if not dict else self.first_element_dict(x)

        return (
            self.infer_type(x)
            if not dict
            else f"{self.infer_type(x[0])}, {self.infer_type(x[1])}"
        )

    def infer_lts(self, x: str, p: str, s: str):
        """Infer list, tuple, set"""
        return self._infer_lstd(x, p, s, dict=False)

    def infer_dict(self, x: str, p: str, s: str):
        """Infer dict"""
        return self._infer_lstd(x, p="{", s="}", dict=True)

    def infer_classvar(self, x: str, p="<", s=">"):
        """Infer classvar"""

        # Remove prefix and suffix
        x = x.removeprefix(p).removesuffix(s)

        if "object" in x:
            # If object ... or ... object is in x, remove object and at 0x ...,
            value = x.replace("object", "").strip()
            value = re.sub(r"(at 0x.*)", "", value).strip()

            # If value starts with module name, remove module name and return value
            if value.startswith(self.module_name + "."):
                value = value.removeprefix(self.module_name + ".")
                return value
            else:
                # Else add value to imports and return base class (second last part of value)
                self.imports.add(value)
                return ".".join(value.split(".")[-2:])

        ## Half HARD CODED
        # If module ... is in x, return ModuleType and add it to imports
        if "module" in x:
            self.imports.add("ModuleType")
            return "ModuleType"

        ## HARD CODED
        if x.startswith("HashLayer"):
            return "HashLayer"

        # If x is empty, raise NotImplementedError
        raise NotImplementedError(
            f"Cannot infer type from classvar: {x}, please report this issue"
        )

    def infer_lstd(self, value: str):
        """Infer list, tuple, set, dict"""
        # Set is not supported, potential bug
        for p, s, t, fn in self.PST:
            if value.startswith(p) and value.endswith(s):
                b0, b1 = ("[]") if t else ("", "")
                return f"{t}{b0}[{fn(value, p, s)}]{b1}"

    def infer_type(self, value: str):
        """Infer type from value"""

        # If value is None, Any or empty, return Any and add Any to imports
        if value is None or value in ("", "Any"):
            self.imports.add("Any")
            return "Any"

        # If §§ is in value, replace it with its original value and infer type for that value
        if "§§" in value:
            for k, v in self.repl.items():
                value = value.replace(f"__§§{k}__", v)
            return self.infer_type(value)

        # If value are special values, return their type
        if value == "None":
            return "None"

        if value in ("True", "False"):
            return "bool"

        # If value is in quotes, return str
        if value.startswith("'") and value.endswith("'"):
            return "str"

        # If value is an alias, return typing's _Alias and add it to imports
        if value.startswith("Alias for"):
            self.imports.add("_Alias")
            return "_Alias"

        # If value is in a rdkit module, add it to imports and return the base class (second last part of value)
        if value.startswith("rdkit."):
            self.imports.add(value)
            return value.split(".")[-2]

        # If numeric, try to parse it as int or float and return the type
        try:
            int(value)
            return "int"
        except:
            pass
        try:
            float(value)
            return "float"
        except:
            pass

        # If only a part is in parentheses, return it and add it to imports
        match = re.match(r"^([a-z, A-Z]*)\(.*\)$", value)
        if match and (match_value := match.group(1)):
            self.imports.add(match_value)
            return match_value

        # If value is in enclosed in "(){}[]<>", return the type of the enclosed value
        stacked_type = self.infer_lstd(value)
        if stacked_type:
            return stacked_type

        else:
            # If value could not be inferred, raise ValueError
            raise ValueError(f"Cannot infer type from value: {value}")


# %%
