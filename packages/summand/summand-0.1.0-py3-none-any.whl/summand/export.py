import builtins
import os.path
import os
import json
from . import db as database


def export(
    save_path: str,
    filename: str,
    listname: list = None,
    all: bool = False,
    e: bool = False,
    include: bool = False
):
    try:
        if not os.path.exists(save_path):
            os.mkdir(save_path)

        completeName = os.path.join(save_path, filename + ".json")
        if os.path.isfile(completeName):
            return False, "The file already exists."

        else:
            if all:
                status, data = get_data(all=True)
                if status == False:
                    return False, data
                else:
                    with open(completeName, "w") as f:
                        json.dump(data, f, indent=4)

                    return True, completeName
            elif e:
                status, data = get_data(listname=listname, e=True)
                if status == False:
                    return False, data
                else:
                    with open(completeName, "w") as f:
                        json.dump(data, f, indent=4)
                    return True, completeName
            elif include:
                status, data = get_data(listname=listname, include=True)
                if status == False:
                    return False, data
                else:
                    with open(completeName, "w") as f:
                        json.dump(data, f, indent=4)
                    return True, completeName
    except:
        return False, "Path does not exist."


def get_data(
    listname: builtins.list = None,
    all: bool = False,
    e: bool = False,
    include: bool = False,
):
    try:
        if all:
            status, data = database.export(listname, all=True)
        elif e:
            status, data = database.export(listname, e=True)
        elif include:
            status, data = database.export(listname, include=True)
        return status, data
    except:
        return False, "An error occurred while connecting to database"
