from serialization_tool.types.json.json import JsonSerialization
from serialization_tool.types.xml.xml import XmlSerialization

# import constants as const
from .constants import *

class SerializationFactory:
    def get_serializer(ext: str):
        if ext == JSON_EXT:
            return JsonSerialization()
        elif ext == XML_EXT:
            return XmlSerialization()
        else:
            print("Unknown type to parse")
                