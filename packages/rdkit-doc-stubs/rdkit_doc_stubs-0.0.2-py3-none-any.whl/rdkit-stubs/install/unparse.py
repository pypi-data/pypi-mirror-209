from .classes import *
from .utils import shift

# Indentation: 4 spaces
PAD = "    "


def unparse_param(self: FoundParam):
    #   : type or ""
    type = f": {self.type}" if self.type else ""

    #  = default or ""
    default = f" = {self.default}" if self.default else ""

    #   name: type = default
    return f"{self.name}{type}{default}"


def unparse_function(self: FoundFunction):
    # Insert self as first parameter if not present if this is a method
    if self.method and (not self.params or self.params[0].name != "self"):
        params = [FoundParam("self", None, None)] + self.params
    else:
        params = self.params

    # Insert indent if this is a method
    pad = PAD if self.method else ""

    #   @overload or ""
    decorator = (pad + f"@overload\n") if self.overload else ""

    #   param: type = default, ...
    params = ", ".join(map(unparse_param, params))

    #   -> returns or ""
    returns = f" -> {self.returns}" if self.returns else ""

    #   def name(params) -> returns:
    fn_def = f"{pad}def {self.name}({params}){returns}:\n"

    #   """doc""" or ""
    doc = (
        f'{pad}{PAD}"""\n{self.docstring}\n"""\n'
        if self.docstring and self.docstring.strip()
        else ""
    )

    #       ...
    body = f"{pad}{PAD}...\n"

    return decorator + fn_def + doc + body


def unparse_class(self: FoundClass):
    #   class name(base):
    class_def = f"class {self.name}({self.base}):\n"

    #   """doc""" or ""
    doc = f'{PAD}"""\n{self.docstring}\n"""\n' if self.docstring.strip() else ""

    #  attribute: type = ...
    attributes = "\n".join(map(unparse_attribute, self.attributes)) + "\n"

    #   class X:
    #       ...
    subclasses = "\n".join(map(unparse_class, self.subclasses)) + "\n"

    #   def method(self, params) -> returns:
    #       ...
    methods = "\n".join(map(unparse_function, self.methods)) + "\n"

    # Combine all the body parts
    body = attributes + subclasses + methods

    # Add ellipsis if there is no body
    body = body if body.strip() else f"{PAD}...\n"

    # Insert indent if this is a subclass
    return shift(class_def + doc + body, self.level, PAD)


def unparse_attribute(self: FoundAttribute):
    # Remove quotes from annotation
    annotation = (
        self.annotation.removeprefix("'").removesuffix("'") if self.annotation else None
    )

    #   type or Annotated[type, """annotation"""]
    type = (
        self.type if not annotation else f'Annotated[{self.type}, """{annotation}"""]'
    )

    # Insert indent as this is a subclass
    #   name: type = ...
    return f"{PAD}{self.name}: {type} = ..."


def unparse_module(self: FoundModule):
    # Link to the module's documentation
    header = f"# Path: https://rdkit.org/docs/source/{self.name}.html\n"

    #  """doc""" or ""
    doc = (
        f'"""\n{self.docstring}\n"""\n'
        if self.docstring and self.docstring.strip()
        else ""
    )

    #   import ...
    #   from ... import ...
    imports = "\n".join(self.imports) + "\n"

    #   class X:
    #       ...
    classes = "\n".join(map(unparse_class, self.classes)) + "\n"

    #   def function(params) -> returns:
    #       ...
    functions = "\n".join(map(unparse_function, self.functions)) + "\n"

    return header + doc + imports + classes + functions
