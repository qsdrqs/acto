from abc import abstractmethod
from schema import AnyOfSchema, ArraySchema, BaseSchema, BooleanSchema, IntegerSchema, ObjectSchema, StringSchema, extract_schema


class K8sField():

    def __init__(self, path, schema) -> None:
        self.path = path
        self.custom_schema = schema


class K8sSchema:

    def __init__(self, path: list, schema: dict) -> None:
        super().__init__(path, schema)

    def __init__(self, schema_obj: BaseSchema) -> None:
        super().__init__(schema_obj.path, schema_obj.raw_schema)

    @abstractmethod
    def Match(schema) -> bool:
        pass


class K8sStringSchema(K8sSchema, StringSchema):

    def Match(schema: StringSchema) -> bool:
        return isinstance(schema, StringSchema)


class K8sObjectSchema(K8sSchema, ObjectSchema):

    def Match(schema: ObjectSchema) -> bool:
        return isinstance(schema, ObjectSchema)


class K8sArraySchema(K8sSchema, ArraySchema):

    def Match(schema: ArraySchema) -> bool:
        return isinstance(schema, ArraySchema)


class K8sIntegerSchema(K8sSchema, IntegerSchema):

    def Match(schema: IntegerSchema) -> bool:
        return isinstance(schema, IntegerSchema)


class K8sBooleanSchema(K8sSchema, BooleanSchema):

    def Match(schema: BooleanSchema) -> bool:
        return isinstance(schema, BooleanSchema)


class K8sAnyOfSchema(K8sSchema, AnyOfSchema):

    def Match(schema: AnyOfSchema) -> bool:
        return isinstance(schema, AnyOfSchema)