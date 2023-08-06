import hashlib
import json
import os
import builtins
import re
import concurrent.futures
import tempfile
from itertools import groupby
import pydoc
import shellingham

def detect_shell():
    try:
        shell = shellingham.detect_shell()
    except shellingham.ShellDetectionFailure:
        shell = provide_default()
    return shell
  
def provide_default():
    if os.name == 'posix':
        return os.environ['SHELL']
    elif os.name == 'nt':
        return os.environ['COMSPEC']
    raise NotImplementedError(f'OS {os.name!r} support not available')

def sha256(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def store_lists(data):
    if "lists.json" not in os.listdir():
        with open("lists.json", "w") as file:
            json.dump(data, file)
    else:
        with open("lists.json", "r") as file:
            all = json.load(file)

        all[str(len(all) + 1)] = data

        with open("lists.json", "w") as file:
            json.dump(all, file)

def lists_json_reset():
    with open("lists.json", "w") as file:
        json.dump({}, file)

def check_for_existence(value):
    with open("lists.json", "r") as file:
        all = json.load(file)
    if value in all.values():
        return True
    else:
        return False

def empty(value):
    if value == None:
        return True
    else:
        return False


def first_setup():
    if "lists.json" not in os.listdir():
        with open("lists.json", "w") as file:
            json.dump({}, file)


def edit_list(from_list, to_list):
    with open("lists.json", "r+") as f:
        data = json.load(f)
        try:
            a = builtins.list(data.keys())[
                builtins.list(data.values()).index(from_list)
            ]
            data[a] = to_list
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()
            return True, "Your Summand was edited successfully."
        except:
            return False,"No List Were Found With This Value"


def find_keys(value):
    with open("lists.json", "r+") as file:
        data = json.load(file)

        key_list = builtins.list(data.keys())
        val_list = builtins.list(data.values())
        position = val_list.index(value)
        return key_list[position]

def get_command_pallete(command_:list, indices:list):
    final:list = []
    lenth = len(command_)
    for i in indices:
        if i == 0:
            if i in indices:
                final.append(f'{i+1}' + '\t' + command_.__getitem__(i) + '*\n')  
            else:
                final.append(f'{i+1}' + '\t' + command_.__getitem__(i) + '\n')

            if i+1 in indices:
                final.append(f'{i+2}' + '\t' + command_.__getitem__(i+1) + '*\n')  
            else:
                final.append(f'{i+2}' + '\t' + command_.__getitem__(i+1) + '\n')

        elif i == lenth - 1:
            if i-1 in indices:
                final.append(f'{i}' + '\t' + command_.__getitem__(i-1) + '*\n') 
            else:
                final.append(f'{i}' + '\t' + command_.__getitem__(i-1) + '\n')
            
            if i in indices:
                final.append(f'{i+1}' + '\t' +  command_.__getitem__(i) + '*\n')
            else: 
                final.append(f'{i+1}' + '\t' +  command_.__getitem__(i) + '\n')


        else:
            if i-1 in indices:
                final.append(f'{i}' + '\t' + command_.__getitem__(i-1) + '*\n')  
            else: 
                final.append(f'{i}' + '\t' + command_.__getitem__(i-1) + '\n')
            
            if i in indices:
                final.append(f'{i+1}' + '\t' + command_.__getitem__(i) + '*\n')  
            else:
                final.append(f'{i+1}' + '\t' + command_.__getitem__(i) + '\n')

            if i+1 in indices:
                final.append(f'{i+2}' + '\t' + command_.__getitem__(i+1) + '*\n')  
            else: 
                final.append(f'{i+2}' + '\t' + command_.__getitem__(i+1) + '\n')
    return final

def delete_list(value):
    with open("lists.json", "r+") as file:
        data = json.load(file)
        try:
            data.pop(find_keys(value))
            file.seek(0)
            json.dump(data, file, indent=4)
            file.truncate()
            return True
        except:
            return False

def time():
    return

def list_to_str(d:list):
    final:str = ""
    for i in d:
        final += i
    return final

# Optimized https://stackoverflow.com/a/3844832/10859114
def all_equal(iterable):
    if type(iterable) == list:
        g = groupby(iterable)
        return next(g, True) and not next(g, False)
    else:
        pass

ADD_REGEX = "^[A-Za-z][A-Za-z0-9_\-#${}()\/\[\]]{2,99}$"


def validate_name(name):
    x = re.search(ADD_REGEX, name)

    if x:
        return True
    return False


class ValidateJson:
    def __init__(self, path):
        tmp = tempfile.NamedTemporaryFile(mode="w+")
        with open(path, "r") as file:
            tmp.write(file.read())

        tmp.seek(0)
        self.json = tmp.read()

    def validate_json_file(self):
        try:
            json.loads(self.json)
            return True
        except ValueError:
            return False

    def validate_parameters(self):
        j = json.loads(self.json)
        arr = []
        for n in j:
            if "name" in n:
                arr.append(True)
            else:
                arr.append(False)

            if "description" in n:
                arr.append(True)
            else:
                arr.append(False)

            if "Command" in n:
                arr.append(True)
            else:
                arr.append(False)

            if "run" in n:
                arr.append(True)
            else:
                arr.append(False)

        return all(element for element in arr)

    def validate_values(self):
        j = json.loads(self.json)
        arr = []
        for n in j:
            if validate_name(n["name"]):
                arr.append(True)
            else:
                arr.append(False)

            if len(n["description"]) <= 250 and isinstance(n["description"], str):
                arr.append(True)
            else:
                arr.append(False)

            if isinstance(n["Command"], list):
                arr.append(True)
            else:
                arr.append(False)

        return all(element for element in arr)

    def validate(self):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            test_one = executor.submit(self.validate_json_file)
            test_one_ = test_one.result()
            test_two = executor.submit(self.validate_parameters)
            test_two_ = test_two.result()
            test_three = executor.submit(self.validate_values)
            test_three_ = test_three.result()

            return all([test_one_, test_two_, test_three_])
