from dataclasses import dataclass


@dataclass
class FoundFunction:
    name: str
    params: list[str]
    returns: str
    docstring: str
    overloads: list[str] | None = None
    method: bool | None = None
    overload: bool | None = None


@dataclass
class FoundClass:
    name: str
    base: str
    docstring: str
    subclasses: list["FoundClass"]
    methods: list[FoundFunction]
    attributes: list[str]
    level: int | None = None


@dataclass
class FoundModule:
    name: str
    docstring: str
    imports: set[str]
    functions: list[FoundFunction]
    classes: list[FoundClass]


@dataclass
class FoundParam:
    name: str
    type: str
    default: str


@dataclass
class FoundAttribute:
    name: str
    type: str
    annotation: str
