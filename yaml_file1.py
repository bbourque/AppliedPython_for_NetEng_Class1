#!/usr/bin/env python

import yaml

my_list = range (8)
my_list.append('A String')
my_list.append('Another String')
my_list.append({})
my_list[-1]['attribs'] = range (8)
my_list[-1]['string1'] = 'Test String'
print my_list
with open("some_file.yml", "w") as f:
    f.write(yaml.dump(my_list, default_flow_style=False))
