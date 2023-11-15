from configparser import ConfigParser
from io import StringIO

import xmltodict
import yaml
import json
from dict2xml import dict2xml
from ruamel.yaml import YAML


def read_file(file_path):
    with open(file_path, "r") as file:
        return file.read()


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


def save_content(file_path, content):
    try:
        with open(file_path, "w") as file:
            file.write(content)
        print(f"Content successfully saved to {file_path}")
    except Exception as e:
        print(f"Error saving content to {file_path}: {e}")


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