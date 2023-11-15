from io import StringIO
from configparser import ConfigParser
import json
import os
from utils.utils import read_file
import xmltodict
import yaml
from ruamel.yaml import YAML


def parse_file_to_types(file_path):
    _, extension = os.path.splitext(file_path)
    extension = extension[1:].lower()

    if extension == "yaml":
        return parse_yaml_to_types(file_path)
    elif extension in ["ini", "xml", "json"]:
        parser_function = globals().get(f"parse_{extension}_to_types")
        if parser_function:
            return parser_function(file_path)

    return None


def parse_ini_to_types(file_path):
    config_object = ConfigParser()
    with open(file_path, "r") as file:
        config_object.read_file(file)
        output_dict = {
            s: dict(config_object.items(s)) for s in config_object.sections()
        }
        return output_dict


def parse_xml_to_types(file_path):
    content = read_file(file_path)
    data = xmltodict.parse(content)
    return data


def parse_yaml_to_types(file_path):
    content = read_file(file_path)
    return yaml.safe_load(content)


def parse_json_to_types(file_path):
    content = read_file(file_path)
    return json.loads(content)


def parse_yaml(file_path):
    yaml_parser = YAML()
    yaml_parser.preserve_quotes = True
    yaml_parser.indent(mapping=2, sequence=4, offset=2)
    yaml_parser.allow_duplicate_keys = True
    yaml_parser.explicit_start = False
    try:
        with open(file_path, "r") as file:
            data = yaml_parser.load(file)
            string_stream = StringIO()
            yaml_parser.dump(data, string_stream)
            source_code = string_stream.getvalue()
            string_stream.close()
            return source_code
    except Exception as e:
        print(f"Error parsing YAML: {e}")
        return None
