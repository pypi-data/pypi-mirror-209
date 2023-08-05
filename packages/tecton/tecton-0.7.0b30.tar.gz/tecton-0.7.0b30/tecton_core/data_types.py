import abc
from typing import List

from pypika.enums import SqlTypes

from tecton_proto.common import data_type_pb2


class DataType(abc.ABC):
    """
    Base DataType class. A python utility for working with `tecton_proto.common.DataType` protos.
    """

    @property
    @abc.abstractmethod
    def proto(self) -> data_type_pb2.DataType:
        pass

    def __hash__(self) -> int:
        return hash(self.proto.SerializeToString(deterministic=True))

    def __eq__(self, other: object):
        if not isinstance(other, DataType):
            return False
        return self.proto == other.proto

    def __str__(self):
        # Require __str__ implementation. Used in error messages.
        raise NotImplementedError

    # TODO: if we stop throwing NotImplementedError, this could be made a real attribute
    @property
    def sql_type(self) -> SqlTypes:
        # Used for safe typecasting in sql-based compute platforms
        raise NotImplementedError


class Int32Type(DataType):
    @property
    def proto(self) -> data_type_pb2.DataType:
        return data_type_pb2.DataType(type=data_type_pb2.DATA_TYPE_INT32)

    def __str__(self) -> str:
        return "Int32"

    @property
    def sql_type(self) -> SqlTypes:
        return SqlTypes.INTEGER


class Int64Type(DataType):
    @property
    def proto(self) -> data_type_pb2.DataType:
        return data_type_pb2.DataType(type=data_type_pb2.DATA_TYPE_INT64)

    def __str__(self) -> str:
        return "Int64"

    @property
    def sql_type(self) -> SqlTypes:
        return SqlTypes.INTEGER


class Float32Type(DataType):
    @property
    def proto(self) -> data_type_pb2.DataType:
        return data_type_pb2.DataType(type=data_type_pb2.DATA_TYPE_FLOAT32)

    def __str__(self) -> str:
        return "Float32"

    @property
    def sql_type(self) -> SqlTypes:
        return SqlTypes.FLOAT


class Float64Type(DataType):
    @property
    def proto(self) -> data_type_pb2.DataType:
        return data_type_pb2.DataType(type=data_type_pb2.DATA_TYPE_FLOAT64)

    def __str__(self) -> str:
        return "Float64"

    @property
    def sql_type(self) -> SqlTypes:
        return SqlTypes.FLOAT


class StringType(DataType):
    @property
    def proto(self) -> data_type_pb2.DataType:
        return data_type_pb2.DataType(type=data_type_pb2.DATA_TYPE_STRING)

    def __str__(self) -> str:
        return "String"

    @property
    def sql_type(self) -> SqlTypes:
        return SqlTypes.VARCHAR


class BoolType(DataType):
    @property
    def proto(self) -> data_type_pb2.DataType:
        return data_type_pb2.DataType(type=data_type_pb2.DATA_TYPE_BOOL)

    def __str__(self) -> str:
        return "Bool"

    @property
    def sql_type(self) -> SqlTypes:
        return SqlTypes.BOOLEAN


class TimestampType(DataType):
    @property
    def proto(self) -> data_type_pb2.DataType:
        return data_type_pb2.DataType(type=data_type_pb2.DATA_TYPE_TIMESTAMP)

    def __str__(self) -> str:
        return "Timestamp"

    @property
    def sql_type(self) -> SqlTypes:
        return SqlTypes.TIMESTAMP


class ArrayType(DataType):
    def __init__(self, element_type: DataType) -> None:
        self._element_type = element_type

    @property
    def proto(self) -> data_type_pb2.DataType:
        return data_type_pb2.DataType(type=data_type_pb2.DATA_TYPE_ARRAY, array_element_type=self.element_type.proto)

    @property
    def element_type(self) -> DataType:
        return self._element_type

    def __str__(self) -> str:
        return f"Array({self._element_type})"

    # TODO: have this work for SQL types
    @property
    def sql_type(self) -> SqlTypes:
        # Used for safe typecasting in sql-based compute platforms
        raise NotImplementedError


# Note StructField does not inherit from DataType. This is because it is not directly convertable to a data type proto.
class StructField:
    def __init__(self, name: str, data_type: DataType) -> None:
        self._name = name
        self._data_type = data_type

    @property
    def proto(self) -> data_type_pb2.StructField:
        return data_type_pb2.StructField(name=self._name, data_type=self._data_type.proto)

    @property
    def name(self) -> str:
        return self._name

    @property
    def data_type(self) -> DataType:
        return self._data_type

    def __str__(self) -> str:
        return f"Field({self._name}, {self._data_type})"


class StructType(DataType):
    def __init__(self, fields: List[StructField]) -> None:
        self._fields = fields

    @property
    def proto(self) -> data_type_pb2.DataType:
        return data_type_pb2.DataType(
            type=data_type_pb2.DATA_TYPE_STRUCT, struct_fields=[field.proto for field in self.fields]
        )

    @property
    def fields(self) -> List[StructField]:
        return self._fields

    def __str__(self) -> str:
        fields_string = ", ".join(str(field) for field in self._fields)
        return f"Struct({fields_string})"

    # TODO: have this work for SQL types
    @property
    def sql_type(self) -> SqlTypes:
        # Used for safe typecasting in sql-based compute platforms
        raise NotImplementedError


def data_type_from_proto(proto: data_type_pb2.DataType) -> DataType:
    """
    Factory method to creata a DataType python class from a `tecton_proto.common.DataType` proto.
    """
    assert proto
    assert proto.type

    if proto.type == data_type_pb2.DATA_TYPE_INT32:
        return Int32Type()
    elif proto.type == data_type_pb2.DATA_TYPE_INT64:
        return Int64Type()
    elif proto.type == data_type_pb2.DATA_TYPE_FLOAT32:
        return Float32Type()
    elif proto.type == data_type_pb2.DATA_TYPE_FLOAT64:
        return Float64Type()
    elif proto.type == data_type_pb2.DATA_TYPE_STRING:
        return StringType()
    elif proto.type == data_type_pb2.DATA_TYPE_BOOL:
        return BoolType()
    elif proto.type == data_type_pb2.DATA_TYPE_TIMESTAMP:
        return TimestampType()
    elif proto.type == data_type_pb2.DATA_TYPE_ARRAY:
        assert proto.array_element_type
        element_type = data_type_from_proto(proto.array_element_type)
        return ArrayType(element_type)
    elif proto.type == data_type_pb2.DATA_TYPE_STRUCT:
        fields = [StructField(field.name, data_type_from_proto(field.data_type)) for field in proto.struct_fields]
        return StructType(fields)
    else:
        msg = f"Unexpected data type {proto}"
        raise ValueError(msg)
