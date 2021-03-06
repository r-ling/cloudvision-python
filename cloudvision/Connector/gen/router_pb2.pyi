# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from google.protobuf.timestamp_pb2 import (
    Timestamp as google___protobuf___timestamp_pb2___Timestamp,
)

from notification_pb2 import (
    Dataset as notification_pb2___Dataset,
    Notification as notification_pb2___Notification,
    NotificationBatch as notification_pb2___NotificationBatch,
)

from sharding_pb2 import (
    Sharding as sharding_pb2___Sharding,
)

from typing import (
    Iterable as typing___Iterable,
    List as typing___List,
    Mapping as typing___Mapping,
    MutableMapping as typing___MutableMapping,
    Optional as typing___Optional,
    Text as typing___Text,
    Tuple as typing___Tuple,
    Union as typing___Union,
    cast as typing___cast,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int
builtin___str = str
if sys.version_info < (3,):
    builtin___buffer = buffer
    builtin___unicode = unicode


class PathWildCardExpandType(builtin___int):
    DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
    @classmethod
    def Name(cls, number: builtin___int) -> builtin___str: ...
    @classmethod
    def Value(cls, name: builtin___str) -> 'PathWildCardExpandType': ...
    @classmethod
    def keys(cls) -> typing___List[builtin___str]: ...
    @classmethod
    def values(cls) -> typing___List['PathWildCardExpandType']: ...
    @classmethod
    def items(cls) -> typing___List[typing___Tuple[builtin___str, 'PathWildCardExpandType']]: ...
    WILDCARD_EXPAND_LEGACY = typing___cast('PathWildCardExpandType', 0)
    WILDCARD_EXPAND_LATEST = typing___cast('PathWildCardExpandType', 1)
    WILDCARD_EXPAND_EXACT_RANGE = typing___cast('PathWildCardExpandType', 2)
    WILDCARD_EXPAND_RELAXED_RANGE = typing___cast('PathWildCardExpandType', 3)
WILDCARD_EXPAND_LEGACY = typing___cast('PathWildCardExpandType', 0)
WILDCARD_EXPAND_LATEST = typing___cast('PathWildCardExpandType', 1)
WILDCARD_EXPAND_EXACT_RANGE = typing___cast('PathWildCardExpandType', 2)
WILDCARD_EXPAND_RELAXED_RANGE = typing___cast('PathWildCardExpandType', 3)
global___PathWildCardExpandType = PathWildCardExpandType

class Path(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class Type(builtin___int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: builtin___int) -> builtin___str: ...
        @classmethod
        def Value(cls, name: builtin___str) -> 'Path.Type': ...
        @classmethod
        def keys(cls) -> typing___List[builtin___str]: ...
        @classmethod
        def values(cls) -> typing___List['Path.Type']: ...
        @classmethod
        def items(cls) -> typing___List[typing___Tuple[builtin___str, 'Path.Type']]: ...
        EXACT = typing___cast('Path.Type', 0)
        REGEXP = typing___cast('Path.Type', 1)
    EXACT = typing___cast('Path.Type', 0)
    REGEXP = typing___cast('Path.Type', 1)
    global___Type = Type

    type = ... # type: global___Path.Type
    path = ... # type: typing___Text
    keys = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___bytes]
    path_elements = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___bytes]

    def __init__(self,
        *,
        type : typing___Optional[global___Path.Type] = None,
        path : typing___Optional[typing___Text] = None,
        keys : typing___Optional[typing___Iterable[builtin___bytes]] = None,
        path_elements : typing___Optional[typing___Iterable[builtin___bytes]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> Path: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Path: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"keys",b"keys",u"path",b"path",u"path_elements",b"path_elements",u"type",b"type"]) -> None: ...
global___Path = Path

class Query(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def dataset(self) -> notification_pb2___Dataset: ...

    @property
    def paths(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[global___Path]: ...

    def __init__(self,
        *,
        dataset : typing___Optional[notification_pb2___Dataset] = None,
        paths : typing___Optional[typing___Iterable[global___Path]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> Query: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Query: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"dataset",b"dataset"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"dataset",b"dataset",u"paths",b"paths"]) -> None: ...
global___Query = Query

class SubscribeRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def query(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[global___Query]: ...

    @property
    def sharded_sub(self) -> sharding_pb2___Sharding: ...

    def __init__(self,
        *,
        query : typing___Optional[typing___Iterable[global___Query]] = None,
        sharded_sub : typing___Optional[sharding_pb2___Sharding] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> SubscribeRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> SubscribeRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"sharded_sub",b"sharded_sub"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"query",b"query",u"sharded_sub",b"sharded_sub"]) -> None: ...
global___SubscribeRequest = SubscribeRequest

class GetRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    start = ... # type: builtin___int
    versions = ... # type: builtin___int
    end = ... # type: builtin___int
    exact_range = ... # type: builtin___bool
    wildcard_expand_type = ... # type: global___PathWildCardExpandType

    @property
    def query(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[global___Query]: ...

    @property
    def sharded_sub(self) -> sharding_pb2___Sharding: ...

    def __init__(self,
        *,
        query : typing___Optional[typing___Iterable[global___Query]] = None,
        start : typing___Optional[builtin___int] = None,
        versions : typing___Optional[builtin___int] = None,
        end : typing___Optional[builtin___int] = None,
        exact_range : typing___Optional[builtin___bool] = None,
        sharded_sub : typing___Optional[sharding_pb2___Sharding] = None,
        wildcard_expand_type : typing___Optional[global___PathWildCardExpandType] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> GetRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> GetRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"sharded_sub",b"sharded_sub"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"end",b"end",u"exact_range",b"exact_range",u"query",b"query",u"sharded_sub",b"sharded_sub",u"start",b"start",u"versions",b"versions",u"wildcard_expand_type",b"wildcard_expand_type"]) -> None: ...
global___GetRequest = GetRequest

class GetAndSubscribeRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    start = ... # type: builtin___int
    versions = ... # type: builtin___int
    exact_range = ... # type: builtin___bool

    @property
    def query(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[global___Query]: ...

    @property
    def sharded_sub(self) -> sharding_pb2___Sharding: ...

    def __init__(self,
        *,
        query : typing___Optional[typing___Iterable[global___Query]] = None,
        start : typing___Optional[builtin___int] = None,
        versions : typing___Optional[builtin___int] = None,
        exact_range : typing___Optional[builtin___bool] = None,
        sharded_sub : typing___Optional[sharding_pb2___Sharding] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> GetAndSubscribeRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> GetAndSubscribeRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"sharded_sub",b"sharded_sub"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"exact_range",b"exact_range",u"query",b"query",u"sharded_sub",b"sharded_sub",u"start",b"start",u"versions",b"versions"]) -> None: ...
global___GetAndSubscribeRequest = GetAndSubscribeRequest

class SearchRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class Type(builtin___int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: builtin___int) -> builtin___str: ...
        @classmethod
        def Value(cls, name: builtin___str) -> 'SearchRequest.Type': ...
        @classmethod
        def keys(cls) -> typing___List[builtin___str]: ...
        @classmethod
        def values(cls) -> typing___List['SearchRequest.Type']: ...
        @classmethod
        def items(cls) -> typing___List[typing___Tuple[builtin___str, 'SearchRequest.Type']]: ...
        STRING = typing___cast('SearchRequest.Type', 0)
        MAC = typing___cast('SearchRequest.Type', 1)
        IP = typing___cast('SearchRequest.Type', 2)
        COMPLEX = typing___cast('SearchRequest.Type', 3)
    STRING = typing___cast('SearchRequest.Type', 0)
    MAC = typing___cast('SearchRequest.Type', 1)
    IP = typing___cast('SearchRequest.Type', 2)
    COMPLEX = typing___cast('SearchRequest.Type', 3)
    global___Type = Type

    search = ... # type: typing___Text
    search_type = ... # type: global___SearchRequest.Type
    start = ... # type: builtin___int
    end = ... # type: builtin___int
    count_only = ... # type: builtin___bool

    @property
    def query(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[global___Query]: ...

    @property
    def key_filters(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[global___Filter]: ...

    @property
    def value_filters(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[global___Filter]: ...

    def __init__(self,
        *,
        search : typing___Optional[typing___Text] = None,
        search_type : typing___Optional[global___SearchRequest.Type] = None,
        query : typing___Optional[typing___Iterable[global___Query]] = None,
        start : typing___Optional[builtin___int] = None,
        end : typing___Optional[builtin___int] = None,
        count_only : typing___Optional[builtin___bool] = None,
        key_filters : typing___Optional[typing___Iterable[global___Filter]] = None,
        value_filters : typing___Optional[typing___Iterable[global___Filter]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> SearchRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> SearchRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"count_only",b"count_only",u"end",b"end",u"key_filters",b"key_filters",u"query",b"query",u"search",b"search",u"search_type",b"search_type",u"start",b"start",u"value_filters",b"value_filters"]) -> None: ...
global___SearchRequest = SearchRequest

class Filter(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class Operator(builtin___int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: builtin___int) -> builtin___str: ...
        @classmethod
        def Value(cls, name: builtin___str) -> 'Filter.Operator': ...
        @classmethod
        def keys(cls) -> typing___List[builtin___str]: ...
        @classmethod
        def values(cls) -> typing___List['Filter.Operator']: ...
        @classmethod
        def items(cls) -> typing___List[typing___Tuple[builtin___str, 'Filter.Operator']]: ...
        EQ = typing___cast('Filter.Operator', 0)
        NEQ = typing___cast('Filter.Operator', 1)
        GT = typing___cast('Filter.Operator', 2)
        GE = typing___cast('Filter.Operator', 3)
        LT = typing___cast('Filter.Operator', 4)
        LE = typing___cast('Filter.Operator', 5)
        RE = typing___cast('Filter.Operator', 6)
        NRE = typing___cast('Filter.Operator', 7)
        IN = typing___cast('Filter.Operator', 8)
        NIN = typing___cast('Filter.Operator', 9)
        SUB = typing___cast('Filter.Operator', 10)
    EQ = typing___cast('Filter.Operator', 0)
    NEQ = typing___cast('Filter.Operator', 1)
    GT = typing___cast('Filter.Operator', 2)
    GE = typing___cast('Filter.Operator', 3)
    LT = typing___cast('Filter.Operator', 4)
    LE = typing___cast('Filter.Operator', 5)
    RE = typing___cast('Filter.Operator', 6)
    NRE = typing___cast('Filter.Operator', 7)
    IN = typing___cast('Filter.Operator', 8)
    NIN = typing___cast('Filter.Operator', 9)
    SUB = typing___cast('Filter.Operator', 10)
    global___Operator = Operator

    class Value(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        str = ... # type: typing___Text
        int = ... # type: builtin___int
        uint = ... # type: builtin___int
        float = ... # type: builtin___float
        b = ... # type: builtin___bool
        ip = ... # type: typing___Text
        mac = ... # type: typing___Text

        @property
        def comp(self) -> global___Filter.ComponentValue: ...

        @property
        def multi(self) -> global___Filter.MultiValue: ...

        def __init__(self,
            *,
            str : typing___Optional[typing___Text] = None,
            int : typing___Optional[builtin___int] = None,
            uint : typing___Optional[builtin___int] = None,
            float : typing___Optional[builtin___float] = None,
            b : typing___Optional[builtin___bool] = None,
            ip : typing___Optional[typing___Text] = None,
            mac : typing___Optional[typing___Text] = None,
            comp : typing___Optional[global___Filter.ComponentValue] = None,
            multi : typing___Optional[global___Filter.MultiValue] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> Filter.Value: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Filter.Value: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"b",b"b",u"comp",b"comp",u"float",b"float",u"int",b"int",u"ip",b"ip",u"kind",b"kind",u"mac",b"mac",u"multi",b"multi",u"str",b"str",u"uint",b"uint"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"b",b"b",u"comp",b"comp",u"float",b"float",u"int",b"int",u"ip",b"ip",u"kind",b"kind",u"mac",b"mac",u"multi",b"multi",u"str",b"str",u"uint",b"uint"]) -> None: ...
        def WhichOneof(self, oneof_group: typing_extensions___Literal[u"kind",b"kind"]) -> typing_extensions___Literal["str","int","uint","float","b","ip","mac","comp","multi"]: ...
    global___Value = Value

    class ComponentValue(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        class ValueEntry(google___protobuf___message___Message):
            DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
            key = ... # type: typing___Text
            value = ... # type: typing___Text

            def __init__(self,
                *,
                key : typing___Optional[typing___Text] = None,
                value : typing___Optional[typing___Text] = None,
                ) -> None: ...
            if sys.version_info >= (3,):
                @classmethod
                def FromString(cls, s: builtin___bytes) -> Filter.ComponentValue.ValueEntry: ...
            else:
                @classmethod
                def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Filter.ComponentValue.ValueEntry: ...
            def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...
        global___ValueEntry = ValueEntry


        @property
        def value(self) -> typing___MutableMapping[typing___Text, typing___Text]: ...

        def __init__(self,
            *,
            value : typing___Optional[typing___Mapping[typing___Text, typing___Text]] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> Filter.ComponentValue: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Filter.ComponentValue: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"value",b"value"]) -> None: ...
    global___ComponentValue = ComponentValue

    class MultiValue(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

        @property
        def values(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[global___Filter.Value]: ...

        def __init__(self,
            *,
            values : typing___Optional[typing___Iterable[global___Filter.Value]] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> Filter.MultiValue: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Filter.MultiValue: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"values",b"values"]) -> None: ...
    global___MultiValue = MultiValue

    field = ... # type: typing___Text
    op = ... # type: global___Filter.Operator

    @property
    def value(self) -> global___Filter.Value: ...

    def __init__(self,
        *,
        field : typing___Optional[typing___Text] = None,
        op : typing___Optional[global___Filter.Operator] = None,
        value : typing___Optional[global___Filter.Value] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> Filter: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Filter: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"value",b"value"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"field",b"field",u"op",b"op",u"value",b"value"]) -> None: ...
global___Filter = Filter

class PublishRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    sync = ... # type: builtin___bool

    @property
    def batch(self) -> notification_pb2___NotificationBatch: ...

    @property
    def compare(self) -> notification_pb2___Notification.Update: ...

    def __init__(self,
        *,
        batch : typing___Optional[notification_pb2___NotificationBatch] = None,
        sync : typing___Optional[builtin___bool] = None,
        compare : typing___Optional[notification_pb2___Notification.Update] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> PublishRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> PublishRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"batch",b"batch",u"compare",b"compare"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"batch",b"batch",u"compare",b"compare",u"sync",b"sync"]) -> None: ...
global___PublishRequest = PublishRequest

class DatasetsRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    types = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]

    def __init__(self,
        *,
        types : typing___Optional[typing___Iterable[typing___Text]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> DatasetsRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> DatasetsRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"types",b"types"]) -> None: ...
global___DatasetsRequest = DatasetsRequest

class DatasetsResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def datasets(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[notification_pb2___Dataset]: ...

    def __init__(self,
        *,
        datasets : typing___Optional[typing___Iterable[notification_pb2___Dataset]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> DatasetsResponse: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> DatasetsResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"datasets",b"datasets"]) -> None: ...
global___DatasetsResponse = DatasetsResponse

class CreateDatasetRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def dataset(self) -> notification_pb2___Dataset: ...

    def __init__(self,
        *,
        dataset : typing___Optional[notification_pb2___Dataset] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> CreateDatasetRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> CreateDatasetRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"dataset",b"dataset"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"dataset",b"dataset"]) -> None: ...
global___CreateDatasetRequest = CreateDatasetRequest

class SetPermissionRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class Type(builtin___int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: builtin___int) -> builtin___str: ...
        @classmethod
        def Value(cls, name: builtin___str) -> 'SetPermissionRequest.Type': ...
        @classmethod
        def keys(cls) -> typing___List[builtin___str]: ...
        @classmethod
        def values(cls) -> typing___List['SetPermissionRequest.Type']: ...
        @classmethod
        def items(cls) -> typing___List[typing___Tuple[builtin___str, 'SetPermissionRequest.Type']]: ...
        PATH_PERMISSION = typing___cast('SetPermissionRequest.Type', 0)
        INHERIT_PERMISSION = typing___cast('SetPermissionRequest.Type', 1)
        UNINHERIT_PERMISSION = typing___cast('SetPermissionRequest.Type', 2)
        ADMIN_PERMISSION = typing___cast('SetPermissionRequest.Type', 3)
    PATH_PERMISSION = typing___cast('SetPermissionRequest.Type', 0)
    INHERIT_PERMISSION = typing___cast('SetPermissionRequest.Type', 1)
    UNINHERIT_PERMISSION = typing___cast('SetPermissionRequest.Type', 2)
    ADMIN_PERMISSION = typing___cast('SetPermissionRequest.Type', 3)
    global___Type = Type

    class PathPerm(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        class Perm(builtin___int):
            DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
            @classmethod
            def Name(cls, number: builtin___int) -> builtin___str: ...
            @classmethod
            def Value(cls, name: builtin___str) -> 'SetPermissionRequest.PathPerm.Perm': ...
            @classmethod
            def keys(cls) -> typing___List[builtin___str]: ...
            @classmethod
            def values(cls) -> typing___List['SetPermissionRequest.PathPerm.Perm']: ...
            @classmethod
            def items(cls) -> typing___List[typing___Tuple[builtin___str, 'SetPermissionRequest.PathPerm.Perm']]: ...
            NULL_PERM_VALUE = typing___cast('SetPermissionRequest.PathPerm.Perm', 0)
            READ_PERM = typing___cast('SetPermissionRequest.PathPerm.Perm', 1)
            WRITE_PERM = typing___cast('SetPermissionRequest.PathPerm.Perm', 2)
            READ_WRITE_PERM = typing___cast('SetPermissionRequest.PathPerm.Perm', 3)
        NULL_PERM_VALUE = typing___cast('SetPermissionRequest.PathPerm.Perm', 0)
        READ_PERM = typing___cast('SetPermissionRequest.PathPerm.Perm', 1)
        WRITE_PERM = typing___cast('SetPermissionRequest.PathPerm.Perm', 2)
        READ_WRITE_PERM = typing___cast('SetPermissionRequest.PathPerm.Perm', 3)
        global___Perm = Perm

        newPerm = ... # type: global___SetPermissionRequest.PathPerm.Perm
        currentPerm = ... # type: global___SetPermissionRequest.PathPerm.Perm
        exactMatch = ... # type: builtin___bool

        @property
        def path(self) -> global___Path: ...

        def __init__(self,
            *,
            path : typing___Optional[global___Path] = None,
            newPerm : typing___Optional[global___SetPermissionRequest.PathPerm.Perm] = None,
            currentPerm : typing___Optional[global___SetPermissionRequest.PathPerm.Perm] = None,
            exactMatch : typing___Optional[builtin___bool] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> SetPermissionRequest.PathPerm: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> SetPermissionRequest.PathPerm: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"path",b"path"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"currentPerm",b"currentPerm",u"exactMatch",b"exactMatch",u"newPerm",b"newPerm",u"path",b"path"]) -> None: ...
    global___PathPerm = PathPerm

    type = ... # type: global___SetPermissionRequest.Type

    @property
    def dataset(self) -> notification_pb2___Dataset: ...

    @property
    def other(self) -> notification_pb2___Dataset: ...

    @property
    def pathPerms(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[global___SetPermissionRequest.PathPerm]: ...

    def __init__(self,
        *,
        type : typing___Optional[global___SetPermissionRequest.Type] = None,
        dataset : typing___Optional[notification_pb2___Dataset] = None,
        other : typing___Optional[notification_pb2___Dataset] = None,
        pathPerms : typing___Optional[typing___Iterable[global___SetPermissionRequest.PathPerm]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> SetPermissionRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> SetPermissionRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"dataset",b"dataset",u"other",b"other"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"dataset",b"dataset",u"other",b"other",u"pathPerms",b"pathPerms",u"type",b"type"]) -> None: ...
global___SetPermissionRequest = SetPermissionRequest

class PermissionSet(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def permissions(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[global___SetPermissionRequest]: ...

    def __init__(self,
        *,
        permissions : typing___Optional[typing___Iterable[global___SetPermissionRequest]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> PermissionSet: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> PermissionSet: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"permissions",b"permissions"]) -> None: ...
global___PermissionSet = PermissionSet

class ClusterDescription(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    clusterName = ... # type: typing___Text
    epoch = ... # type: builtin___int

    @property
    def timestamp(self) -> google___protobuf___timestamp_pb2___Timestamp: ...

    def __init__(self,
        *,
        timestamp : typing___Optional[google___protobuf___timestamp_pb2___Timestamp] = None,
        clusterName : typing___Optional[typing___Text] = None,
        epoch : typing___Optional[builtin___int] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ClusterDescription: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ClusterDescription: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"timestamp",b"timestamp"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"clusterName",b"clusterName",u"epoch",b"epoch",u"timestamp",b"timestamp"]) -> None: ...
global___ClusterDescription = ClusterDescription

class SetPasswordRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    password = ... # type: typing___Text

    @property
    def dataset(self) -> notification_pb2___Dataset: ...

    def __init__(self,
        *,
        dataset : typing___Optional[notification_pb2___Dataset] = None,
        password : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> SetPasswordRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> SetPasswordRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"dataset",b"dataset"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"dataset",b"dataset",u"password",b"password"]) -> None: ...
global___SetPasswordRequest = SetPasswordRequest

class CreateSessionRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def dataset(self) -> notification_pb2___Dataset: ...

    def __init__(self,
        *,
        dataset : typing___Optional[notification_pb2___Dataset] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> CreateSessionRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> CreateSessionRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"dataset",b"dataset"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"dataset",b"dataset"]) -> None: ...
global___CreateSessionRequest = CreateSessionRequest

class CreateSessionResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    jwtToken = ... # type: typing___Text
    expiry = ... # type: builtin___int

    def __init__(self,
        *,
        jwtToken : typing___Optional[typing___Text] = None,
        expiry : typing___Optional[builtin___int] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> CreateSessionResponse: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> CreateSessionResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"expiry",b"expiry",u"jwtToken",b"jwtToken"]) -> None: ...
global___CreateSessionResponse = CreateSessionResponse
