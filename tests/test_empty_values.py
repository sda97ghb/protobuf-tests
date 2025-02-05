import pytest

from protobuf_tests.protos.messages_pb2 import Person


def test_absent_fields_are_serialized_as_empty_bytes() -> None:
    person = Person(
        first_name=None,
        last_name=None,
        nick_names=None,
        age=None,
        number_of_fingers=None,
        favourite_numbers=None,
        address_home=None,
        address_work=None,
        favourite_places=None,
    )
    serialized = person.SerializeToString()
    assert serialized == b""


def test_string_field_with_implicit_cardinality() -> None:
    # Defined as `string first_name = 1;`
    person = Person.FromString(b"")
    assert person.first_name == ""
    with pytest.raises(
        ValueError,
        match="Field Person.first_name does not have presence.",
    ):
        person.HasField("first_name")


def test_string_field_with_optional() -> None:
    # Defined as `optional string last_name = 2;`
    person = Person.FromString(b"")
    assert person.last_name == ""
    assert not person.HasField("last_name")


def test_string_field_with_repeated() -> None:
    # Defined as `repeated string nick_names = 3;`
    person = Person.FromString(b"")
    assert person.nick_names == []
    with pytest.raises(
        ValueError,
        match="Field Person.nick_names does not have presence.",
    ):
        person.HasField("nick_names")


def test_int_field_with_implicit_cardinality() -> None:
    # Defined as `int32 age = 4;`
    person = Person.FromString(b"")
    assert person.age == 0
    with pytest.raises(ValueError, match="Field Person.age does not have presence."):
        person.HasField("age")


def test_int_field_with_optional() -> None:
    # Defined as `optional int32 number_of_fingers = 5;`
    person = Person.FromString(b"")
    assert person.number_of_fingers == 0
    assert not person.HasField("number_of_fingers")


def test_int_field_with_repeated() -> None:
    # Defined as `repeated int32 favourite_numbers = 6;`
    person = Person.FromString(b"")
    assert person.favourite_numbers == []
    with pytest.raises(
        ValueError,
        match="Field Person.favourite_numbers does not have presence.",
    ):
        person.HasField("favourite_numbers")


def test_embedded_message_field_with_implicit_cardinality() -> None:
    # Defined as `Address address_home = 7;`
    person = Person.FromString(b"")
    assert person.address_home.city == ""
    assert person.address_home.street == ""
    assert not person.HasField("address_home")


def test_embedded_message_field_with_optional() -> None:
    # Defined as `optional Address address_work = 8;`
    person = Person.FromString(b"")
    assert person.address_work.city == ""
    assert person.address_work.street == ""
    assert not person.HasField("address_work")


def test_embedded_message_field_with_repeated() -> None:
    # Defined as `repeated Address favourite_places = 9;`
    person = Person.FromString(b"")
    assert person.favourite_places == []
    with pytest.raises(
        ValueError,
        match="Field Person.favourite_places does not have presence.",
    ):
        person.HasField("favourite_places")
