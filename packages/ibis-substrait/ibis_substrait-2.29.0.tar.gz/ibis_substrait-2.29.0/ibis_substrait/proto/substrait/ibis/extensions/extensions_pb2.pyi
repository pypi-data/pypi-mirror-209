"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
SPDX-License-Identifier: Apache-2.0"""
import builtins
import google.protobuf.any_pb2
import google.protobuf.descriptor
import google.protobuf.message
import sys
if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions
DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class SimpleExtensionURI(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    EXTENSION_URI_ANCHOR_FIELD_NUMBER: builtins.int
    URI_FIELD_NUMBER: builtins.int
    extension_uri_anchor: builtins.int
    'A surrogate key used in the context of a single plan used to reference the\n    URI associated with an extension.\n    '
    uri: builtins.str
    'The URI where this extension YAML can be retrieved. This is the "namespace"\n    of this extension.\n    '

    def __init__(self, *, extension_uri_anchor: builtins.int=..., uri: builtins.str=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['extension_uri_anchor', b'extension_uri_anchor', 'uri', b'uri']) -> None:
        ...
global___SimpleExtensionURI = SimpleExtensionURI

class SimpleExtensionDeclaration(google.protobuf.message.Message):
    """Describes a mapping between a specific extension entity and the uri where
    that extension can be found.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class ExtensionType(google.protobuf.message.Message):
        """Describes a Type"""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        EXTENSION_URI_REFERENCE_FIELD_NUMBER: builtins.int
        TYPE_ANCHOR_FIELD_NUMBER: builtins.int
        NAME_FIELD_NUMBER: builtins.int
        extension_uri_reference: builtins.int
        'references the extension_uri_anchor defined for a specific extension URI.'
        type_anchor: builtins.int
        'A surrogate key used in the context of a single plan to reference a\n        specific extension type\n        '
        name: builtins.str
        'the name of the type in the defined extension YAML.'

        def __init__(self, *, extension_uri_reference: builtins.int=..., type_anchor: builtins.int=..., name: builtins.str=...) -> None:
            ...

        def ClearField(self, field_name: typing_extensions.Literal['extension_uri_reference', b'extension_uri_reference', 'name', b'name', 'type_anchor', b'type_anchor']) -> None:
            ...

    class ExtensionTypeVariation(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        EXTENSION_URI_REFERENCE_FIELD_NUMBER: builtins.int
        TYPE_VARIATION_ANCHOR_FIELD_NUMBER: builtins.int
        NAME_FIELD_NUMBER: builtins.int
        extension_uri_reference: builtins.int
        'references the extension_uri_anchor defined for a specific extension URI.'
        type_variation_anchor: builtins.int
        'A surrogate key used in the context of a single plan to reference a\n        specific type variation\n        '
        name: builtins.str
        'the name of the type in the defined extension YAML.'

        def __init__(self, *, extension_uri_reference: builtins.int=..., type_variation_anchor: builtins.int=..., name: builtins.str=...) -> None:
            ...

        def ClearField(self, field_name: typing_extensions.Literal['extension_uri_reference', b'extension_uri_reference', 'name', b'name', 'type_variation_anchor', b'type_variation_anchor']) -> None:
            ...

    class ExtensionFunction(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        EXTENSION_URI_REFERENCE_FIELD_NUMBER: builtins.int
        FUNCTION_ANCHOR_FIELD_NUMBER: builtins.int
        NAME_FIELD_NUMBER: builtins.int
        extension_uri_reference: builtins.int
        'references the extension_uri_anchor defined for a specific extension URI.'
        function_anchor: builtins.int
        'A surrogate key used in the context of a single plan to reference a\n        specific function\n        '
        name: builtins.str
        'A simple name if there is only one impl for the function within the YAML.\n        A compound name, referencing that includes type short names if there is\n        more than one impl per name in the YAML.\n        '

        def __init__(self, *, extension_uri_reference: builtins.int=..., function_anchor: builtins.int=..., name: builtins.str=...) -> None:
            ...

        def ClearField(self, field_name: typing_extensions.Literal['extension_uri_reference', b'extension_uri_reference', 'function_anchor', b'function_anchor', 'name', b'name']) -> None:
            ...
    EXTENSION_TYPE_FIELD_NUMBER: builtins.int
    EXTENSION_TYPE_VARIATION_FIELD_NUMBER: builtins.int
    EXTENSION_FUNCTION_FIELD_NUMBER: builtins.int

    @property
    def extension_type(self) -> global___SimpleExtensionDeclaration.ExtensionType:
        ...

    @property
    def extension_type_variation(self) -> global___SimpleExtensionDeclaration.ExtensionTypeVariation:
        ...

    @property
    def extension_function(self) -> global___SimpleExtensionDeclaration.ExtensionFunction:
        ...

    def __init__(self, *, extension_type: global___SimpleExtensionDeclaration.ExtensionType | None=..., extension_type_variation: global___SimpleExtensionDeclaration.ExtensionTypeVariation | None=..., extension_function: global___SimpleExtensionDeclaration.ExtensionFunction | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['extension_function', b'extension_function', 'extension_type', b'extension_type', 'extension_type_variation', b'extension_type_variation', 'mapping_type', b'mapping_type']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['extension_function', b'extension_function', 'extension_type', b'extension_type', 'extension_type_variation', b'extension_type_variation', 'mapping_type', b'mapping_type']) -> None:
        ...

    def WhichOneof(self, oneof_group: typing_extensions.Literal['mapping_type', b'mapping_type']) -> typing_extensions.Literal['extension_type', 'extension_type_variation', 'extension_function'] | None:
        ...
global___SimpleExtensionDeclaration = SimpleExtensionDeclaration

class AdvancedExtension(google.protobuf.message.Message):
    """A generic object that can be used to embed additional extension information
    into the serialized substrait plan.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    OPTIMIZATION_FIELD_NUMBER: builtins.int
    ENHANCEMENT_FIELD_NUMBER: builtins.int

    @property
    def optimization(self) -> google.protobuf.any_pb2.Any:
        """An optimization is helpful information that don't influence semantics. May
        be ignored by a consumer.
        """

    @property
    def enhancement(self) -> google.protobuf.any_pb2.Any:
        """An enhancement alter semantics. Cannot be ignored by a consumer."""

    def __init__(self, *, optimization: google.protobuf.any_pb2.Any | None=..., enhancement: google.protobuf.any_pb2.Any | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['enhancement', b'enhancement', 'optimization', b'optimization']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['enhancement', b'enhancement', 'optimization', b'optimization']) -> None:
        ...
global___AdvancedExtension = AdvancedExtension