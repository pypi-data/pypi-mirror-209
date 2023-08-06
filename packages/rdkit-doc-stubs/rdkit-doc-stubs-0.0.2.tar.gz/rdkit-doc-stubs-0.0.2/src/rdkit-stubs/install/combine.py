import ast
from dataclasses import dataclass
from enum import Enum
from typing import Any, Type

from .align import Align

PRINT_WARNINGS = False


def areinstances(types, *args):
    """Check if all args are instances of the given types."""
    return all(isinstance(x, types) for x in args)


class T(Enum):
    CLASS = 0
    FUNCTION = 1
    ANNASSIGN = 2
    ASSIGN = 3
    EXPR = 4
    IMPORT = 5
    ALWAYS = 6
    NEVER = 7

    __repr__ = lambda self: self.name


# Store AST nodes with unique key (frozen to be hashable)
@dataclass(frozen=True)
class KeyAST:
    name: str
    type: T
    private: bool
    overload: bool


class SortedAST:
    def __init__(self, ast: ast.Module | ast.ClassDef):
        self.ast = ast
        self.dict = self._get_dict()

    def names_for_type(self, types: tuple[Type] = None, nottypes: tuple[Type] = None):
        """Get all names for the given type(s) and exclude the given type(s)."""

        return [
            key.name
            for key in self.dict
            if not (types and key.type not in types)
            and not (nottypes and key.type in nottypes)
        ]

    def get_by_name(self, name: str):
        """Get the AST node with the given name.

        Raises ValueError if there are multiple nodes with the same name but specific cases.
        """

        # Get all items with the given name
        items = [x for key, x in self.dict.items() if key.name == name]

        # If not found, return None
        if len(items) == 0:
            return None
        # If single item found, return the item
        if len(items) == 1:
            return items[0]

        # If more than two items found, raise an error
        if len(items) > 2:
            raise ValueError((name, items))

        # If two items found, check specific cases
        if len(items) == 2:
            types = {type(x) for x in items}
            # If one is AnnAssign and the other is Assign, return the AnnAssign
            if types == {ast.AnnAssign, ast.Assign}:
                return [x for x in items if isinstance(x, ast.AnnAssign)][0]
            # If one is FunctionDef and the other is AnnAssign, return the FunctionDef
            elif types == {ast.FunctionDef, ast.AnnAssign}:
                return [x for x in items if isinstance(x, ast.FunctionDef)][0]
            else:
                # Else raise an error
                raise ValueError((types, name, items))

    def __repr__(self) -> str:
        return self.dict.__repr__()

    def _get_dict(self):
        # Initialize data dictionary
        data: dict[KeyAST, Any] = {}

        for value in self.ast.body:
            # Get name and type of value based on type
            name, type = self._get_info(value)

            # Check if key is private
            private = name.startswith("_")

            # Check if key is an overload
            overload = has_overload(value) if type == T.FUNCTION else False

            # Create key
            key = KeyAST(name, type, private, overload)

            # If key is overload, make it a list
            if key.overload:
                value = [value]

            # If key not in data, add it
            if key not in data:
                data[key] = value

            else:
                # If key in data, but its an overload, add it to the list
                if key.overload:
                    data[key] += value

                ## HARD CODED
                # Assigns which are defined twice in mypy's stubs
                elif key.name in ("InfoEntropy", "InfoGain", "binaryHolder"):
                    data[key] = value

                else:
                    # Else raise an error
                    raise ValueError(f"Key already in data\n{key=}\n{data=}")
        return data

    @staticmethod
    def _get_info(x):
        """Get name and type of value based on type"""

        # If value is a function or class, get name from its name
        if isinstance(x, ast.FunctionDef):
            return str(x.name), T.FUNCTION

        elif isinstance(x, ast.ClassDef):
            return str(x.name), T.CLASS

        # If value is an annotated assignment or assignment with only 1 target, get name from its target's id
        elif isinstance(x, ast.AnnAssign):
            return str(x.target.id), T.ANNASSIGN
        elif (
            isinstance(x, ast.Assign)
            and len(x.targets) == 1
            and isinstance(x.targets[0], ast.Name)
        ):
            return str(x.targets[0].id), T.ASSIGN

        # If value is an expression, get name from its unparsed value
        elif isinstance(x, ast.Expr) and isinstance(x.value, ast.Constant):
            return ast.unparse(x.value).strip(), T.EXPR

        # If value is an import or an import from, unparse it and return always ast.Import
        elif isinstance(x, ast.ImportFrom | ast.Import):
            return ast.unparse(x).strip(), T.IMPORT

        raise NotImplementedError(x)


def init_combine(new: ast.Module | ast.ClassDef, base: ast.Module | ast.ClassDef):
    # Check if new and base are the same type and are modules or classes
    assert type(new) == type(base) and isinstance(
        new, ast.Module | ast.ClassDef
    ), f"Can't combine module with class: {new=} {base=}"
    cls = type(new)

    # Keyword arguments for the new class depending on whether its a module or class
    kwargs = (
        {"type_ignores": new.type_ignores}
        if isinstance(new, ast.Module)
        else {
            "name": new.name,
            "bases": new.bases,
            "keywords": new.keywords,
            "decorator_list": new.decorator_list,
        }
    )
    return cls, kwargs


def has_decorator(fn: ast.FunctionDef, decorator: str):
    """Check if function has a decorator with the given name"""
    return any(isinstance(d, ast.Name) and d.id == decorator for d in fn.decorator_list)


# Check if function has overload decorator
has_overload = lambda fn: has_decorator(fn, "overload")

# Check if function has property decorator
has_property = lambda fn: has_decorator(fn, "property")


def combine(new: ast.ClassDef | ast.Module, base: ast.ClassDef | ast.Module):
    """Combine two ASTs into one."""

    # Init base class and keyword arguments for the new class
    cls, kwargs = init_combine(new, base)

    # Combine body of new and base
    body = update_body(new, base)

    return cls(**kwargs, body=body)


def update_function(new: list | ast.FunctionDef, base: list | ast.FunctionDef):
    """Update function(s) in base with function(s) in new."""

    if isinstance(new, ast.FunctionDef):
        # If multiple functions found in base and only one in new,
        # just print a warning if PRINT_WARNINGS is True
        if isinstance(base, list) and PRINT_WARNINGS:
            print(
                f"""Warning: multiple definitions of function in base
{new=}
{base=}
    """
            )
        # If only a single function found in base, make it a list
        new = [new]

    # Always return new functions
    return new


def update_body(new: ast.Module | ast.ClassDef, base: ast.Module | ast.ClassDef):
    """Update body of base with body of new."""

    # Sort new and base by name in to dictionaries
    new_, base_ = SortedAST(new), SortedAST(base)

    # Get all expressions and imports from new and base
    new_elems, base_elems = (
        [x.get_by_name(name) for name in x.names_for_type(types=(T.EXPR, T.IMPORT))]
        for x in (new_, base_)
    )
    # Combine expressions and imports, starting with new and then base
    body = new_elems + base_elems

    # Get all names from new and base that are not expressions or imports
    new_names, base_names = (
        x.names_for_type(nottypes=(T.EXPR, T.IMPORT)) for x in (new_, base_)
    )

    # Combine names, prioritizing base names
    combined_names = Align.align(new_names, base_names)

    # Initialize list for other elements
    other = []

    for name in combined_names:
        # Get elements with the current name from new and base
        new_elem, base_elem = (x.get_by_name(name) for x in (new_, base_))

        # If either element is None, add the other element
        if None in (new_elem, base_elem):
            other.append(new_elem or base_elem)

        # If both elements are classes, combine them (recursively)
        elif areinstances(ast.ClassDef, new_elem, base_elem):
            other.append(combine(new_elem, base_elem))

        # If both elements are functions or lists (always containing functions),
        # update them with new functions
        elif areinstances(ast.FunctionDef | list, new_elem, base_elem):
            other.extend(update_function(new_elem, base_elem))

        # If both elements are annotated assignments, return annotated assignment from new
        elif areinstances(ast.AnnAssign, new_elem, base_elem):
            other.append(new_elem)

        # If new is function and old is assignmet, return assignment from base
        elif isinstance(new_elem, ast.FunctionDef) and isinstance(
            base_elem, ast.Assign
        ):
            other.append(base_elem)

        # If new is function and old is annotated assignment, return function from new
        elif isinstance(new_elem, ast.FunctionDef) and isinstance(
            base_elem, ast.AnnAssign
        ):
            other.append(new_elem)

        # If new is an annotated assignment and old is a function,
        # return annotated assignment from new if function has property decorator
        elif (
            isinstance(new_elem, ast.AnnAssign)
            and isinstance(base_elem, ast.FunctionDef)
            and has_property(base_elem)
        ):
            x = new_elem.annotation.id
            new_elem.annotation.id = "property[" + str(x) + "]"
            other.append(new_elem)

        else:
            # Else raise an error
            raise NotImplementedError((new_elem, base_elem))

    # Combine expression and imports with other elements
    return body + other
