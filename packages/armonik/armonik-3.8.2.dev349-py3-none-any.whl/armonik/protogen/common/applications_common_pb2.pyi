from . import objects_pb2 as _objects_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ApplicationRaw(_message.Message):
    __slots__ = ["name", "version", "namespace", "service"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    name: str
    version: str
    namespace: str
    service: str
    def __init__(self, name: _Optional[str] = ..., version: _Optional[str] = ..., namespace: _Optional[str] = ..., service: _Optional[str] = ...) -> None: ...

class ListApplicationsRequest(_message.Message):
    __slots__ = ["page", "page_size", "filter", "sort"]
    class OrderByField(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        ORDER_BY_FIELD_UNSPECIFIED: _ClassVar[ListApplicationsRequest.OrderByField]
        ORDER_BY_FIELD_NAME: _ClassVar[ListApplicationsRequest.OrderByField]
        ORDER_BY_FIELD_VERSION: _ClassVar[ListApplicationsRequest.OrderByField]
        ORDER_BY_FIELD_NAMESPACE: _ClassVar[ListApplicationsRequest.OrderByField]
        ORDER_BY_FIELD_SERVICE: _ClassVar[ListApplicationsRequest.OrderByField]
    ORDER_BY_FIELD_UNSPECIFIED: ListApplicationsRequest.OrderByField
    ORDER_BY_FIELD_NAME: ListApplicationsRequest.OrderByField
    ORDER_BY_FIELD_VERSION: ListApplicationsRequest.OrderByField
    ORDER_BY_FIELD_NAMESPACE: ListApplicationsRequest.OrderByField
    ORDER_BY_FIELD_SERVICE: ListApplicationsRequest.OrderByField
    class OrderDirection(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        ORDER_DIRECTION_UNSPECIFIED: _ClassVar[ListApplicationsRequest.OrderDirection]
        ORDER_DIRECTION_ASC: _ClassVar[ListApplicationsRequest.OrderDirection]
        ORDER_DIRECTION_DESC: _ClassVar[ListApplicationsRequest.OrderDirection]
    ORDER_DIRECTION_UNSPECIFIED: ListApplicationsRequest.OrderDirection
    ORDER_DIRECTION_ASC: ListApplicationsRequest.OrderDirection
    ORDER_DIRECTION_DESC: ListApplicationsRequest.OrderDirection
    class Filter(_message.Message):
        __slots__ = ["name", "version", "namespace", "service"]
        NAME_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        NAMESPACE_FIELD_NUMBER: _ClassVar[int]
        SERVICE_FIELD_NUMBER: _ClassVar[int]
        name: str
        version: str
        namespace: str
        service: str
        def __init__(self, name: _Optional[str] = ..., version: _Optional[str] = ..., namespace: _Optional[str] = ..., service: _Optional[str] = ...) -> None: ...
    class Sort(_message.Message):
        __slots__ = ["fields", "direction"]
        FIELDS_FIELD_NUMBER: _ClassVar[int]
        DIRECTION_FIELD_NUMBER: _ClassVar[int]
        fields: _containers.RepeatedScalarFieldContainer[ListApplicationsRequest.OrderByField]
        direction: ListApplicationsRequest.OrderDirection
        def __init__(self, fields: _Optional[_Iterable[_Union[ListApplicationsRequest.OrderByField, str]]] = ..., direction: _Optional[_Union[ListApplicationsRequest.OrderDirection, str]] = ...) -> None: ...
    PAGE_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    page: int
    page_size: int
    filter: ListApplicationsRequest.Filter
    sort: ListApplicationsRequest.Sort
    def __init__(self, page: _Optional[int] = ..., page_size: _Optional[int] = ..., filter: _Optional[_Union[ListApplicationsRequest.Filter, _Mapping]] = ..., sort: _Optional[_Union[ListApplicationsRequest.Sort, _Mapping]] = ...) -> None: ...

class ListApplicationsResponse(_message.Message):
    __slots__ = ["applications", "page", "page_size", "total"]
    APPLICATIONS_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    applications: _containers.RepeatedCompositeFieldContainer[ApplicationRaw]
    page: int
    page_size: int
    total: int
    def __init__(self, applications: _Optional[_Iterable[_Union[ApplicationRaw, _Mapping]]] = ..., page: _Optional[int] = ..., page_size: _Optional[int] = ..., total: _Optional[int] = ...) -> None: ...

class CountTasksByStatusRequest(_message.Message):
    __slots__ = ["name", "version"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    name: str
    version: str
    def __init__(self, name: _Optional[str] = ..., version: _Optional[str] = ...) -> None: ...

class CountTasksByStatusResponse(_message.Message):
    __slots__ = ["status"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: _containers.RepeatedCompositeFieldContainer[_objects_pb2.StatusCount]
    def __init__(self, status: _Optional[_Iterable[_Union[_objects_pb2.StatusCount, _Mapping]]] = ...) -> None: ...
