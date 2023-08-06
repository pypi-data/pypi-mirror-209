import builtins
import os
from typing import Optional, Union
from tinydb import TinyDB, Query
import re

db = TinyDB("app.json")

Command = Query()


def checkforexistence():
    # exit()
    database = os.path.exists("app.json")
    list = os.path.exists("lists.json")
    if database == True and list == True:
        data = db.all()
        if data != []:
            return True, "200"
        else:
            return False, "It seems your database is empty."
    else:
        return False, "There's a problem for finding your database."


def insert_list(list, description, command, split: str):
    try:
        db.insert(
            {
                "name": list,
                "description": description,
                "Command": command,
                "run": [],
            }
        )
        return True
    except:
        return False


def command_insert():
    pass


def delete_all_data():
    db.truncate()


def list(q):
    if q == "":
        list = []
        all_rows = db.all()
        for row in all_rows:
            list.append(row["name"])
        if list == []:
            list = False
        return list
    else:
        return db.search(Command.name.matches(q))


def edit_list(from_name, to_name):
    try:
        db.update({"name": to_name}, Command.name == from_name)
        return True , "Summand edited successfully"
    except:
        return False, "Something went wrong."


def time():
    pass


def delete(value):
    try:
        db.remove(Command.name == value)
        return True
    except:
        return False


def remove_command(summand: str, command: list, a = True):
    if a != True:
    # try:
        commands = get_command(summand)
        if commands[0] == True:
            commands = commands[1]

        for i in command:
            if commands.count(i) == 1:
                commands.remove(i)
                db.update({"Command": commands}, Command.name == summand)
                return True

            elif commands.count(command[-1]) > 1:
                a = duplicate_commmand(commands, command)
                final = []
                for i in a:
                    if i - 1 < 0:
                        final.extend([i, i + 1, i + 2])
                    elif i + 1 > len(commands) - 1:
                        final.extend([i - 2, i - 1, i])
                    else:
                        final.extend([i - 1, i, i + 1])

                for n, s in enumerate(final):
                    if (n) % 3 == 0:
                        print()
                        print(f"[{int(n/3)}]" + command[-1])
                    print(str(s) + " " + commands[s])
                print(a)
                number = input("Which One Do You Want To Remove?")
                if int(number) > len(a) - 1 or int(number) < 0:
                    print("wrong Number")
                # elif number==0:
                # list(filter((a[-1]).__ne__, commands))
                # db.update({"Command": commands}, Command.name == summand)
                else:
                    commands.pop(a[int(number)])
                    db.update({"Command": commands}, Command.name == summand)

            elif commands.count(command) < 1:
                return (
                    (False, "Your command was not found.")
                    if len(command) == 1
                    else (False, "Your commands was not found.")
                )
    elif a:
        db.update({"Command": command}, Command.name == summand)


def duplicate_commmand(commands: builtins.list, command: builtins.list):

    final = []
    duplicate = []

    for n, i in enumerate(commands):
        for a in command:
            if i == a:
                final.append(i)
                duplicate.append(n)

    return duplicate


def get_command(summand: str):
    try:
        return True, db.search(Command["name"] == summand)[0]["Command"]
    except:
        return False, "Value Error"


def update_description(summand, description = "False"):
    try:
        if description == "False":
            db.update({"description": ""}, Command.name == summand)
        else:
            db.update({"description": description}, Command.name == summand)
        return True
    except:
        return False


def run(summand: str):
    status = checkforexistence()
    if status[0] == False:
        return False, str(status[1])
    try:
        result = db.search(Command.name == summand)[0]
    except:
        return False, "Error while getting your commands."

    if result["Command"] != [""]:
        return True, result["Command"]
    else:
        return False, "It seems your Summand does not have any command."


def export(
    listname: Union[str, builtins.list],
    all: bool = False,
    e: bool = False,
    include: bool = False,
) -> builtins.list:
    result = []
    first_time = first()
    if first_time == False:
        if all:
            try:
                result = db.all()
                status = True
            except:
                result = "An Error Happened :("
                status = False
        elif e:
            commands = getFieldData("name")
            c = [x for x in commands if x not in listname]

            for i in c:
                try:
                    a = db.get((Command.name == i))
                    result.append(a)
                    status = True
                except:
                    status = False
                    result = "An Error Happened :("
        elif include:
            for i in listname:
                try:
                    a = db.get((Command.name == i))
                    if not a:
                        pass
                    else:
                        result.append(a)
                    status = True
                except:
                    status = False
                    result = "An Error Happened"
    elif first_time == True:
        result = "This Is Your First Time Use And There Isn't Any Data To Export."
        status = False
    else:
        result = first_time
        status = False
    return status, result


def import_list(list):
    try:
        db.insert(list)
        return True
    except:
        return False


def first():
    try:
        data = db.all()
        if len(data) == 0:
            return True
        else:
            return False
    except:
        return "An error happened while connecting to Database"


def getFieldData(fieldName):
    result = [r[fieldName] for r in db.all()]
    return result


def all():
    return db.all()



def exact_search(summand):
    result = db.search(Command.name.search(rf"\b{summand}\b"))

    return result

# print(exact_search("test"))
# TODO: app.json
# TODO: db.json
# TODO: if they were empty

# print(export(listname=['list2','list22']))
# TODO try except and return true / Fixed
# TODO Bug #1: DB Search And DB Get Are Not True.
# TODO Bug #1.1: Somewhere Has list[0] but when we change search to get search return list get return dict
