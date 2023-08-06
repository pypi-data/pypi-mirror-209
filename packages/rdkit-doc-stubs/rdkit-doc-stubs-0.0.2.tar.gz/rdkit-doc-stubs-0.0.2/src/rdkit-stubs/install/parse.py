import re

from .classes import *
from .infer import InferTypes
from .modules import BUILTIN_TYPES, MODULES

PARAM_PATTERN = re.compile(r"^(\((.*?)\))?(.*?)(=(.*))?$")
ATTRIBUTE_PATTERN = re.compile(
    r"^(.*?)(?:\s?(?:=|\r\n|\r|\n)\s?(.*)((?:(?:(?:\r\n|\r|\n)?)(?:.*))*))?$"
)

FUNC_DEF_PATTERN = re.compile(r"(?:.*?\()(.*)(?:\))(?:(?:\s*->\s*)(.*)(?:\s*:))?")


class Parse:
    """Collection of functions to parse found elements to their python equivalent"""

    def __init__(self, module: str) -> None:
        self.inferer = InferTypes(module)
        self.name = module

    @staticmethod
    def remove_keywords(name: str) -> str:
        """Remove reserved keywords from the name"""
        if name in ("from", "in", "class", "return", "def", "as", "import"):
            name = name + "_"
        return name

    def remove_module(self, x: str) -> str | None:
        """Remove the module name from the class name

        Returns None if the module name is not present
        """
        if x.startswith(self.name + "."):
            x = x.removeprefix(self.name + ".")
            return x

    def remove_rdkit(self, x: str) -> str | None:
        """Remove the module name of another rdkit module from the class name

        Returns None if no rdkit module is present"""
        if x.startswith("rdkit."):
            # If the rdkit module is in the name, add it to the imports
            self.inferer.imports.add(x)
            return ".".join(x.split(".")[-2:])

    def base(self, base: str) -> str:
        """Parse the base class name"""

        # If base is empty or "" return ""
        if not base:
            return ""

        # Remove the current's module name
        if class_in_current_module := self.remove_module(base):
            base = class_in_current_module

        # Remove names of other rdkit modules
        elif class_in_rdkit := self.remove_rdkit(base):
            base = class_in_rdkit

        else:
            # Remove the module name of other specified modules
            for module in ("Boost.Python", "sqlalchemy", "enum"):
                if base.startswith(module + "."):
                    # If the module is in the name, add it to the imports
                    self.inferer.imports.add(module)
                    return base

        return base

    def returns(self, returns: str) -> str:
        """Parse the return type of a function"""

        # If returns is empty or "" return ""
        if not returns:
            return ""

        x = returns.removeprefix("→").removesuffix(":").strip()

        ## HARD CODED
        # Errors in the documentation

        if "in the interval" in x:
            x = "float"
        if "returns True" in x:
            x = "bool"

        # Add to the import list
        self.inferer.imports.add(x)

        return x

    def classes(self, classes: list[FoundClass]) -> list[FoundClass]:
        """Parse a list of classes with Parse.cls"""
        return [self.cls(c) for c in classes]

    def functions(self, functions: list[FoundFunction]) -> list[FoundClass]:
        """Parse a list of functions with Parse.function"""
        return [self.function(f) for f in functions]

    def cls(self, cls: FoundClass, level=0) -> FoundClass:
        """Parse a class"""

        # Parse the base class
        cls.base = self.base(cls.base)

        # Parse the subclasses (recursive)
        cls.subclasses = [self.cls(c, level=level + 1) for c in cls.subclasses]

        # Parse the methods, unpack overloaded methods
        cls.methods = [self.function(m, method=True) for m in cls.methods]
        cls.methods = [m for fn in cls.methods for m in fn]

        # Parse the attributes
        cls.attributes = [self.attribute(a) for a in cls.attributes]

        # Set the indentation level
        cls.level = level

        return cls

    def function(self, fn: FoundFunction, method=False) -> list[FoundFunction]:
        """Parse a function"""

        if not fn.overloads:
            # If the function has no overloads, parse it normally
            # Keep the original docstring
            fn.params = [self.param(p) for p in fn.params]
            fn.returns = self.returns(fn.returns)
            fn.overloads = []
            fn.method = method
            fn.overload = False
            return [fn]

        else:
            # If the function has overloads, parse them seperately and add overload to the imports
            self.inferer.imports.add("overload")

            # Initialize the list of overloaded functions
            fns: list[FoundFunction] = []

            # Split the docstring in the docstring of the function and the docstring of the overload for each overload
            docstring = fn.docstring
            for ix, overload in enumerate([None] + fn.overloads):
                d, docstring = (
                    (docstring, None)
                    if ix == len(fn.overloads)
                    else docstring.split(fn.overloads[ix], 1)
                )

                # Find the params and return value of the overload
                params, returns = (
                    self.overload(overload) if ix != 0 else (fn.params, fn.returns)
                )

                # Parse the params and return value
                params = [self.param(p) for p in params]
                returns = self.returns(returns)

                # Add the overload to the list of overloaded functions
                fns.append(
                    FoundFunction(
                        fn.name,
                        params,
                        returns,
                        docstring,
                        d,
                        method=method,
                        overload=True,
                    )
                )

            return fns

    def overload(self, overload: str) -> tuple[list[str], str]:
        """Parse an overload of a function"""

        # Split function def in overload in params and return value
        matched_params, matched_returns = FUNC_DEF_PATTERN.match(overload).groups()

        # Optional params are seperated with brackets
        # Split them from the required params
        req_params, *opt_params = matched_params.split("[,")

        # Split the required params by comma
        req_params = req_params.split(",")

        # Combine the required and optional params
        combined_params = req_params + opt_params

        # Clean up the params, remove whitespaces and brackets and wrong apostrophes
        params = [p.strip().replace("’", "'") for p in combined_params]

        # Remove the brackets from the last optional params
        if "[" in params[-1]:
            print("WARNING: last optional param is a list, potential bug")
        while params[-1].endswith("]"):
            params[-1] = params[-1].removesuffix("]").strip()

        returns = matched_returns.strip()

        return params, returns

    def attribute(self, text: str) -> FoundAttribute:
        """Parse an attribute"""

        # Split the attribute in name, value and annotation
        name, type, annotation = ATTRIBUTE_PATTERN.match(text).groups()

        # Infer the type of the attribute
        type = type.strip() if type else ""
        type = self.inferer.infer_type(type)

        name = name.strip()

        ## HARD CODED
        if name == "None":
            name = "None_"

        if annotation:
            # If the attribute has an annotation, add it to the imports
            annotation = annotation.strip()
            self.inferer.imports.add("Annotated")

        return FoundAttribute(name, type, annotation)

    def param(self, text: str) -> FoundParam:
        """Parse a parameter"""

        # Split the parameter in name, type and default value
        _, typ, name, _, default = PARAM_PATTERN.match(text).groups()

        # Incositent documentation: type annotated python-style
        if ":" in name:
            name, typ = name.split(":")

        name = name.strip()

        # Remove reserved keywords from the name
        name = self.remove_keywords(name)

        if typ:
            typ = typ.strip()

            # Remove the current's module name
            if class_in_current_module := self.remove_module(typ):
                typ = class_in_current_module

            ## HARD CODED
            elif typ == "FilterCatalogs":
                typ = "FilterCatalogParams.FilterCatalogs"
            else:
                # Class in other module, add the type to the imports
                self.inferer.imports.add(typ)

        if default:
            default = default.strip()

            # Remove the current's module name
            if class_in_current_module := self.remove_module(default):
                default = class_in_current_module

            # Remove the rdkit module name
            elif class_in_other_module := self.remove_rdkit(default):
                default = class_in_other_module

            else:
                if default.startswith("<") and default.endswith(">"):
                    default = default.removeprefix("<").removesuffix(">").strip()

                    # If default is a Boost function, set default to ellipsis and type to Callable and add it to the imports
                    if "Boost.Python.function" in default:
                        default, typ = "...", "Callable"
                        self.inferer.imports.add("Callable")

                    # If default is a function, use the function name as default
                    elif "function" in default:
                        default = default.replace("function", "").strip()

                        ## HARD CODED
                        # Functions not in current module, need to be imported
                        if default == "EuclideanDist":
                            default = "DistFunctions.EuclideanDist"
                            self.inferer.imports.add(
                                "rdkit.ML.KNN.DistFunctions.EuclideanDist"
                            )
                        elif default == "ID3Boot":
                            default = "ID3.ID3Boot"
                            self.inferer.imports.add("rdkit.ML.DecTree.ID3.ID3Boot")

                    # If default is a class, use the class name as default and add it to the imports
                    elif "class" in default:
                        default = default.replace("class", "").replace("'", "").strip()
                        self.inferer.imports.add(default)

                    ## HARD CODED
                    # If default is a TextIOWrapper, set default to ellipsis and type to TextIOWrapper and add it to the imports
                    elif "TextIOWrapper" in default:
                        default, typ = "...", "_io.TextIOWrapper"
                        self.inferer.imports.add("_io")

                    else:
                        # Else set default to ellipsis and type to the infered defaults' type
                        default, typ = "...", self.inferer.infer_classvar(default)

        ## HARD CODED
        if "-->" in name:
            name, typ = "x", "list[int]"
        if " " and "MHFP" in name:
            if "integers" in name:
                name, typ = "mhfp", "list[int]"
            elif "strings" in name:
                name, typ = "mhfp", "list[str]"

        return FoundParam(name, typ, default)

    @staticmethod
    def module(
        name: str,
        docstring: str,
        functions: list[FoundFunction],
        classes: list[FoundClass],
    ):
        """Create a module from the parsed data, main entry point of the parser"""

        # Initialize the parser with module name
        parser = Parse(name)

        # Parse found classes
        classes = parser.classes(classes)

        # Parse found functions and unpack overloaded functions
        functions = parser.functions(functions)
        functions = [f for fn in functions for f in fn]

        # Parse found imports, remove available classes
        imports = parser.imports([c.name for c in classes])

        return FoundModule(name, docstring, imports, functions, classes)

    def imports(self, classes: list[str]):
        """Parse the imports"""

        # Initialize the set of missing imports
        missing_imports = set()

        for import_ in self.inferer.imports:
            # Skip None imports
            if not import_:
                continue

            # Initialize the base class of the import
            cls = None

            if import_.startswith("rdkit."):
                cls = import_.split(".")[-2]

            # Skip imports of builtin types, classes in current module and base classes in current module
            if (
                import_ in BUILTIN_TYPES
                or import_ in classes
                or (cls and cls in classes)
            ):
                continue

            # Import Boost.Python for every kind of Boost.Python import
            if import_.startswith("Boost.Python."):
                missing_imports.add("Boost.Python")
                continue

            # If the import has not been found, add it to the missing imports
            missing_imports.add(import_)

        # Initialize the set of imports to be returned
        out = set()

        for module in missing_imports:
            # Try to find the parent module in HARD CODED modules dictionary
            if module in MODULES:
                parent = MODULES[module]
            else:
                # If not found, split it in parent and module
                try:
                    parent = ".".join(module.split(".")[:-2])
                    module = module.split(".")[-2]
                except IndexError as e:
                    print(module)
                    raise e

            # If module is current module, skip it
            if module == self.name:
                continue

            # If parent is not None, add the import with the parent
            if parent:
                out.add(f"from {parent} import {module}")
            # Else add the import without the parent
            else:
                out.add(f"import {module}")

        return out
