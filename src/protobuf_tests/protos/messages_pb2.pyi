from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers

DESCRIPTOR: _descriptor.FileDescriptor

class Address(_message.Message):
    __slots__ = ("city", "street")
    CITY_FIELD_NUMBER: _ClassVar[int]
    STREET_FIELD_NUMBER: _ClassVar[int]
    city: str
    street: str
    def __init__(
        self,
        city: str | None = ...,
        street: str | None = ...,
    ) -> None: ...

class Person(_message.Message):
    __slots__ = (
        "address_home",
        "address_work",
        "age",
        "favourite_numbers",
        "favourite_places",
        "first_name",
        "last_name",
        "nick_names",
        "number_of_fingers",
    )
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    NICK_NAMES_FIELD_NUMBER: _ClassVar[int]
    AGE_FIELD_NUMBER: _ClassVar[int]
    NUMBER_OF_FINGERS_FIELD_NUMBER: _ClassVar[int]
    FAVOURITE_NUMBERS_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_HOME_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_WORK_FIELD_NUMBER: _ClassVar[int]
    FAVOURITE_PLACES_FIELD_NUMBER: _ClassVar[int]
    first_name: str
    last_name: str
    nick_names: _containers.RepeatedScalarFieldContainer[str]
    age: int
    number_of_fingers: int
    favourite_numbers: _containers.RepeatedScalarFieldContainer[int]
    address_home: Address
    address_work: Address
    favourite_places: _containers.RepeatedCompositeFieldContainer[Address]
    def __init__(
        self,
        first_name: str | None = ...,
        last_name: str | None = ...,
        nick_names: _Iterable[str] | None = ...,
        age: int | None = ...,
        number_of_fingers: int | None = ...,
        favourite_numbers: _Iterable[int] | None = ...,
        address_home: Address | _Mapping | None = ...,
        address_work: Address | _Mapping | None = ...,
        favourite_places: _Iterable[Address | _Mapping] | None = ...,
    ) -> None: ...
