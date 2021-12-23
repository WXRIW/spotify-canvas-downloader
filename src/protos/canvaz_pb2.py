# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: canvaz.proto
"""Generated protocol buffer code."""
import protos.canvazmeta_pb2 as canvaz__meta__pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor.FileDescriptor(
    name="canvaz.proto",
    package="com.spotify.canvazcache",
    syntax="proto3",
    serialized_options=b"\n\022com.spotify.canvazH\002",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x0c\x63\x61nvaz.proto\x12\x17\x63om.spotify.canvazcache\x1a\x11\x63\x61nvaz-meta.proto"3\n\x06\x41rtist\x12\x0b\n\x03uri\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0e\n\x06\x61vatar\x18\x03 \x01(\t"\xe1\x02\n\x14\x45ntityCanvazResponse\x12\x46\n\x08\x63\x61nvases\x18\x01 \x03(\x0b\x32\x34.com.spotify.canvazcache.EntityCanvazResponse.Canvaz\x12\x16\n\x0ettl_in_seconds\x18\x02 \x01(\x03\x1a\xe8\x01\n\x06\x43\x61nvaz\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\x12\x0f\n\x07\x66ile_id\x18\x03 \x01(\t\x12&\n\x04type\x18\x04 \x01(\x0e\x32\x18.com.spotify.canvaz.Type\x12\x12\n\nentity_uri\x18\x05 \x01(\t\x12/\n\x06\x61rtist\x18\x06 \x01(\x0b\x32\x1f.com.spotify.canvazcache.Artist\x12\x10\n\x08\x65xplicit\x18\x07 \x01(\x08\x12\x13\n\x0buploaded_by\x18\x08 \x01(\t\x12\x0c\n\x04\x65tag\x18\t \x01(\t\x12\x12\n\ncanvas_uri\x18\x0b \x01(\t"\x88\x01\n\x13\x45ntityCanvazRequest\x12\x45\n\x08\x65ntities\x18\x01 \x03(\x0b\x32\x33.com.spotify.canvazcache.EntityCanvazRequest.Entity\x1a*\n\x06\x45ntity\x12\x12\n\nentity_uri\x18\x01 \x01(\t\x12\x0c\n\x04\x65tag\x18\x02 \x01(\tB\x16\n\x12\x63om.spotify.canvazH\x02\x62\x06proto3',
    dependencies=[
        canvaz__meta__pb2.DESCRIPTOR,
    ],
)

_ARTIST = _descriptor.Descriptor(
    name="Artist",
    full_name="com.spotify.canvazcache.Artist",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="uri",
            full_name="com.spotify.canvazcache.Artist.uri",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="name",
            full_name="com.spotify.canvazcache.Artist.name",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="avatar",
            full_name="com.spotify.canvazcache.Artist.avatar",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=60,
    serialized_end=111,
)

_ENTITYCANVAZRESPONSE_CANVAZ = _descriptor.Descriptor(
    name="Canvaz",
    full_name="com.spotify.canvazcache.EntityCanvazResponse.Canvaz",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="id",
            full_name="com.spotify.canvazcache.EntityCanvazResponse.Canvaz.id",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="url",
            full_name="com.spotify.canvazcache.EntityCanvazResponse.Canvaz.url",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="file_id",
            full_name="com.spotify.canvazcache.EntityCanvazResponse.Canvaz.file_id",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="type",
            full_name="com.spotify.canvazcache.EntityCanvazResponse.Canvaz.type",
            index=3,
            number=4,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="entity_uri",
            full_name="com.spotify.canvazcache.EntityCanvazResponse.Canvaz.entity_uri",
            index=4,
            number=5,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="artist",
            full_name="com.spotify.canvazcache.EntityCanvazResponse.Canvaz.artist",
            index=5,
            number=6,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="explicit",
            full_name="com.spotify.canvazcache.EntityCanvazResponse.Canvaz.explicit",
            index=6,
            number=7,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="uploaded_by",
            full_name="com.spotify.canvazcache.EntityCanvazResponse.Canvaz.uploaded_by",
            index=7,
            number=8,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="etag",
            full_name="com.spotify.canvazcache.EntityCanvazResponse.Canvaz.etag",
            index=8,
            number=9,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="canvas_uri",
            full_name="com.spotify.canvazcache.EntityCanvazResponse.Canvaz.canvas_uri",
            index=9,
            number=11,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=235,
    serialized_end=467,
)

_ENTITYCANVAZRESPONSE = _descriptor.Descriptor(
    name="EntityCanvazResponse",
    full_name="com.spotify.canvazcache.EntityCanvazResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="canvases",
            full_name="com.spotify.canvazcache.EntityCanvazResponse.canvases",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="ttl_in_seconds",
            full_name="com.spotify.canvazcache.EntityCanvazResponse.ttl_in_seconds",
            index=1,
            number=2,
            type=3,
            cpp_type=2,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[
        _ENTITYCANVAZRESPONSE_CANVAZ,
    ],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=114,
    serialized_end=467,
)

_ENTITYCANVAZREQUEST_ENTITY = _descriptor.Descriptor(
    name="Entity",
    full_name="com.spotify.canvazcache.EntityCanvazRequest.Entity",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="entity_uri",
            full_name="com.spotify.canvazcache.EntityCanvazRequest.Entity.entity_uri",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="etag",
            full_name="com.spotify.canvazcache.EntityCanvazRequest.Entity.etag",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=564,
    serialized_end=606,
)

_ENTITYCANVAZREQUEST = _descriptor.Descriptor(
    name="EntityCanvazRequest",
    full_name="com.spotify.canvazcache.EntityCanvazRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="entities",
            full_name="com.spotify.canvazcache.EntityCanvazRequest.entities",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[
        _ENTITYCANVAZREQUEST_ENTITY,
    ],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=470,
    serialized_end=606,
)

_ENTITYCANVAZRESPONSE_CANVAZ.fields_by_name[
    "type"].enum_type = canvaz__meta__pb2._TYPE
_ENTITYCANVAZRESPONSE_CANVAZ.fields_by_name["artist"].message_type = _ARTIST
_ENTITYCANVAZRESPONSE_CANVAZ.containing_type = _ENTITYCANVAZRESPONSE
_ENTITYCANVAZRESPONSE.fields_by_name[
    "canvases"].message_type = _ENTITYCANVAZRESPONSE_CANVAZ
_ENTITYCANVAZREQUEST_ENTITY.containing_type = _ENTITYCANVAZREQUEST
_ENTITYCANVAZREQUEST.fields_by_name[
    "entities"].message_type = _ENTITYCANVAZREQUEST_ENTITY
DESCRIPTOR.message_types_by_name["Artist"] = _ARTIST
DESCRIPTOR.message_types_by_name[
    "EntityCanvazResponse"] = _ENTITYCANVAZRESPONSE
DESCRIPTOR.message_types_by_name["EntityCanvazRequest"] = _ENTITYCANVAZREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Artist = _reflection.GeneratedProtocolMessageType(
    "Artist",
    (_message.Message, ),
    {
        "DESCRIPTOR": _ARTIST,
        "__module__": "canvaz_pb2"
        # @@protoc_insertion_point(class_scope:com.spotify.canvazcache.Artist)
    },
)
_sym_db.RegisterMessage(Artist)

EntityCanvazResponse = _reflection.GeneratedProtocolMessageType(
    "EntityCanvazResponse",
    (_message.Message, ),
    {
        "Canvaz":
        _reflection.GeneratedProtocolMessageType(
            "Canvaz",
            (_message.Message, ),
            {
                "DESCRIPTOR": _ENTITYCANVAZRESPONSE_CANVAZ,
                "__module__": "canvaz_pb2"
                # @@protoc_insertion_point(class_scope:com.spotify.canvazcache.EntityCanvazResponse.Canvaz)
            },
        ),
        "DESCRIPTOR":
        _ENTITYCANVAZRESPONSE,
        "__module__":
        "canvaz_pb2"
        # @@protoc_insertion_point(class_scope:com.spotify.canvazcache.EntityCanvazResponse)
    },
)
_sym_db.RegisterMessage(EntityCanvazResponse)
_sym_db.RegisterMessage(EntityCanvazResponse.Canvaz)

EntityCanvazRequest = _reflection.GeneratedProtocolMessageType(
    "EntityCanvazRequest",
    (_message.Message, ),
    {
        "Entity":
        _reflection.GeneratedProtocolMessageType(
            "Entity",
            (_message.Message, ),
            {
                "DESCRIPTOR": _ENTITYCANVAZREQUEST_ENTITY,
                "__module__": "canvaz_pb2"
                # @@protoc_insertion_point(class_scope:com.spotify.canvazcache.EntityCanvazRequest.Entity)
            },
        ),
        "DESCRIPTOR":
        _ENTITYCANVAZREQUEST,
        "__module__":
        "canvaz_pb2"
        # @@protoc_insertion_point(class_scope:com.spotify.canvazcache.EntityCanvazRequest)
    },
)
_sym_db.RegisterMessage(EntityCanvazRequest)
_sym_db.RegisterMessage(EntityCanvazRequest.Entity)

DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)