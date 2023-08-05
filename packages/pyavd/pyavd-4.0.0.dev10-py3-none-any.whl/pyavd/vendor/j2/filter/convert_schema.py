from __future__ import annotations


from pyavd.vendor.errors import AristaAvdError
from pyavd.vendor.schema.avdschema import AvdSchema
from pyavd.vendor.schema.avdtodocumentationschemaconverter import AvdToDocumentationSchemaConverter
from pyavd.vendor.schema.avdtojsonschemaconverter import AvdToJsonSchemaConverter


def convert_schema(schema_id: str, type: str):
    """
    The `arista.avd.convert_schema` filter will convert AVD Schema to a chosen output format.

    TODO: Split into separate filters or lookups for each type.

    Parameters
    ----------
    schema_id : str, ["eos_cli_config_gen" , "eos_designs"]
        ID of AVD Schema
    type : str, ["documentation", "jsonschema"]
        Type of schema to convert to

    Returns
    -------
    dict | list
        Schema of the requested type

    Raises
    ------
    AvdSchemaError, AvdValidationError
        If the input schema is not valid, exceptions will be raised accordingly.
    """
    avdschema = AvdSchema(schema_id=schema_id)
    if type == "documentation":
        return AvdToDocumentationSchemaConverter(avdschema).convert_schema()

    elif type == "jsonschema":
        return AvdToJsonSchemaConverter(avdschema).convert_schema()

    else:
        raise AristaAvdError(f"Filter arista.avd.convert_schema requires type 'documentation' or 'jsonschema'. Got {type}")


class FilterModule(object):
    def filters(self):
        return {
            "convert_schema": convert_schema,
        }
