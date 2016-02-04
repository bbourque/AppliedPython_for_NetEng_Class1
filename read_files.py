#!/usr/bin/env python

import yaml
import json


with open("some_file.yml") as f:
    new_yaml_list = yaml.load(f)
print 'This is the yaml list'
print new_yaml_list


with open("some_file.json") as f:
    new_json_list = json.load(f)
print 'This is the json list'
print new_json_list
