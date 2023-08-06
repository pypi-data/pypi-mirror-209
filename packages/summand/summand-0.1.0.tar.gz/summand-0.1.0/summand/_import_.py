import json
from pathlib import Path
import pathlib
from typing import List
import os
import threading
from . import db as database
from . import utilities as utility
from . import utilities

status = []
result = []


def importer(location=Path, ignore: bool = None):  # tuple / optimizing required
    for path in location:
        if path.exists():
            if pathlib.Path(path).suffix == ".json":
                validator = utilities.ValidateJson(path)
                if not validator.validate():
                    return False, f"Your file is corrupted."
                else:
                    with open(path, "r+") as file:
                        try:
                            data = json.loads(file.read())
                            try:
                                for i in data:
                                    if utilities.check_for_existence(
                                        utilities.sha256(i.get("name"))
                                    ):
                                        status.append(False)
                                        result.append(f"{i.get('name')} Existed.")
                                    else:
                                        if database.import_list(i):
                                            utilities.store_lists(
                                                utilities.sha256(i.get("name"))
                                            )
                                            status.append(True)
                                            result.append(f"{i.get('name')} Added.")
                                        else:
                                            status.append(False)
                                            result.append(
                                                f"Something wen't wrong to add {i.get('name')}"
                                            )

                                    return status, result
                            except:
                                return (
                                    False,
                                    "Your Json file has some problem. Key did not found.",
                                )
                        except:
                            return (
                                False,
                                f"Your Json File {os.path.split(path)[1]} Has Some Problem.",
                            )
                    
            else:
                return False, f"Your path {path} does not correct"
        else:
            return False, f"Your path {path} does not exist"


# exit()
# class analizer():
#     outfile = open("file.json", "w")
#     with open("hu.json", "r") as f:
#         all = f.read()
#         # for number,i in enumerate(all):
#         # print(number,i)
#         all = json.loads(all)
#         print(all)

# json.dump(all, outfile, indent=4)
# return json.dumps(all, indent=4)

# header = itertools.islice(all , 1)
# footer = itertools.islice(all , len(all)-1, len(all))

# print(all)
# for i in zip(header,footer):
# if i == ('[', ']'):
# return True
# else:
# return False


# print(analizer())


# def test():
#     f = open("test2.json", "r")
#     file = json.loads(f.read())

#     out_file = open("myfile.json", "w")

#     # json.dump(file, out_file, indent = 4)

#     # out_file.close()
#     json.dump(file, out_file, indent=4)


# test()
# TODO json tree view prety V.1.1
# TODO Add Threading To Analizing Data V.1.2

# class Analizer:
#     def __init__(self , data):
#         self.data = data

#     def JsonValidator(self):
#         try:
#             json.loads(self.data)
#             return True
#         except ValueError as err:
#             return False
#     def analize(self):
#         if self.data == ():
#             pass

# data = open('test.json')
# analize = Analizer(data.read())
# print(analize.JsonValidator())
