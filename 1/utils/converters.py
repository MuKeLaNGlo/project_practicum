# converters.py
import json
from configparser import ConfigParser
from io import StringIO

from dict2xml import dict2xml
from ruamel.yaml import YAML


def convert_to_file(data, file_type):
    if file_type == "yaml":
        return convert_to_yaml(data)
    elif file_type == "xml":
        return convert_to_xml(data)
    elif file_type == "ini":
        return convert_to_ini(data)
    elif file_type == "json":
        return convert_to_json(data)
    else:
        raise ValueError(f"Unsupported file type: {file_type}")


def convert_to_yaml(data):
    yaml_converter = YAML()
    yaml_converter.preserve_quotes = True
    yaml_converter.indent(mapping=2, sequence=4, offset=2)
    yaml_converter.allow_duplicate_keys = True
    yaml_converter.explicit_start = False
    string_stream = StringIO()
    yaml_converter.dump(data, string_stream)
    source_code = string_stream.getvalue()
    string_stream.close()
    return source_code


def convert_to_ini(data):
    config = ConfigParser()

    def add_section(section, values):
        config.add_section(section)
        for key, value in values.items():
            if isinstance(value, dict):
                add_section(f"{section}.{key}", value)
            else:
                config.set(section, key, str(value))

    for section, values in data.items():
        if isinstance(values, dict):
            add_section(section, values)
        else:
            config.set("", section, str(values))

    ini_content = StringIO()
    config.write(ini_content)
    return ini_content.getvalue()


def convert_to_xml(data):
    xml_content = dict2xml(data)
    return xml_content


def convert_to_json(data):
    return json.dumps(data, indent=2)
