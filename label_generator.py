import pathlib
from ruamel.yaml import YAML

path = pathlib.Path('data.yaml')
names = YAML().load(path)['names']

with open('label.py', 'w') as file:
    file.write('from enum import Enum\n\n')
    file.write('class Label(Enum):\n')
    for index, name in enumerate(names):
        file.write(f'    {name}={index}\n')
