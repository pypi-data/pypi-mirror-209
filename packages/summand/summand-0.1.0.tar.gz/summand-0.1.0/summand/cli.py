import typer
import json
from typing import Tuple, List, Optional
import builtins
from pathlib import Path
from collections import OrderedDict
import subprocess
import pydoc
from . import db as testdb
from . import utilities as utility
from . import _import_ as i
from . import export as e
import pydoc
import subprocess


app = typer.Typer(
    help="Summand CLI." + "\n" + "https://summand.dev", pretty_exceptions_enable=False
)


def warning(data):
    typer.secho(data, fg=typer.colors.YELLOW, err=True)


def error(data, exit_code=1):
    typer.secho(data, fg=typer.colors.RED, err=True)
    raise typer.Exit(exit_code)


def sucess(data):
    typer.secho(data, fg=typer.colors.GREEN)


@app.command(help="Add New Summand - Summand add <name of your Summand> [options]")
def add(
    name: str = typer.Argument("", help="Name of your Summand."),
    description: str = typer.Option(
        "", "-D", "--description", help="Your Sumamnd description."
    ),
    commands: Optional[List[str]] = typer.Option([[""]], "-C", "--command", help="Sumamnd's command."),
    split: str = typer.Option(",", "-S", "--split", help="Split your commands."),
):
    utility.first_setup()
    if utility.check_for_existence(utility.sha256(name)):
        error("Summand already exists !")

    if not utility.validate_name(name):
        error(
            """
Your entered name is not valid.

Please use the structure below:
A-Z | a-z 
A-Z | a-z 0-9 _ $ # [](){} /

- White spaces is not allowed
- your name should be in the range of 3-100 characters
            """
        )
    else:
        try:
            final_cmds = []

            for command in commands:
                command = command.split(" ")
                final_cmds.append(command)

            testdb.insert_list(name, description, final_cmds, split)
            utility.store_lists(utility.sha256(name))
            sucess(f"Your Summand name is: {name}")
    
        except:
            error(f"An error occurred while adding your Summand.")


# TODO list has #Try
@app.command(help="List all of the Summands.")
def list(
    list: str = typer.Argument("", help="Search... (Regex Supported)"),
    number: bool = typer.Option(
        False, "-N", "--number", help="Numeric print your output."
    ),
    list_name: bool = False,  # typer.Option(False),
    description: bool = typer.Option(
        False, "-D", "--description", help="Show Summand descriptions in output."
    ),
    # reverse: ,
):

    # TODO: Thid Could Be a Function That Give Arguments Then Return The List

    # INFO: Default Sort Is By Added_Time / Sort Types: alphabetical, time_added, / letter, commands

    if testdb.list("") == False:
        error("There's Nothing To show.")

    if list == "":
        data = testdb.all()
        i = 1
        for index in data:
            if number == True:
                if description == True:
                    print(i, index["name"], index["description"])
                else:
                    print(i, index["name"])
            else:
                if description == True:
                    print(index["name"], index["description"])
                else:
                    print(index["name"])

            i = i + 1

    else:
        data = testdb.list(list)
        i = 1
        for index in data:
            if number == True:
                if description == True:
                    print(i, index["name"], index["description"])
                else:
                    print(i, index["name"])
            else:
                if description == True:
                    print(index["name"], index["description"])
                else:
                    print(index["name"])

            i = i + 1


@app.command(help="Run your Summand.")
def run(summand=typer.Argument(None, help="Enter your Summand's name.")):
    if summand == None:
        warning("Nothing specified, nothing ran.")
    summand = testdb.run(summand)
    if summand[0] == True:
        for i in summand[1]:
            subprocess.run(i)
    else:
        error(summand[1])


@app.command(help="Edit your existing list.")
def edit(
    summand: str = typer.Argument(
        ..., help="Enter your summand that you want to edit."
    ),
    command: Tuple[str, str] = typer.Option(
        (None, None), help="Enter your command and new_command"
    ),
    description: str = typer.Option(
        None,
        help="Enter your new desired description.",
    ),
    name: str = typer.Option(None, help="Change your Summand's name."),
    split: str = typer.Option(" ", help="Split your input with custom splitter."),
):

    command, cmd = command
    
    if command and cmd:
        command = command.split(split)
        cmd = cmd.split(split)

    if utility.check_for_existence(utility.sha256(summand)):
        if command != None:  # Verified
            # print("hii")
            # if not utility.check_for_existence(utility.sha256(command)):
            # index = utility.find_keys(utility.sha256(summand))
            # print(index)
            # with open("app.json", "r") as f:
            # j = testdb.exact_search(summand)
            commands = testdb.exact_search(summand)[0]["Command"]
            # print(commands)

            # if commands.count(command).empty:
            # error(f"There's no command in {summand}")

            if commands.count(command) <= 1:
                try:
                    position = commands.index(command)
                    commands[position] = cmd
                    testdb.remove_command(summand, commands)
                except:
                    error(f"Command [{command}] is not exist!")
            else:
                try:
                    indices = [i for i, x in enumerate(commands) if x == command]
                    if utility.detect_shell()[0] in ["powershell","cmd"]:                                             
                        pydoc.pipepager(
                            (
                                utility.list_to_str(
                                    builtins.list(
                                        OrderedDict.fromkeys(
                                            utility.get_command_pallete(commands, indices)
                                        )
                                    )
                                )
                            ),
                            cmd="more",
                        )

                    else:
                        pydoc.pipepager(
                            (
                                utility.list_to_str(
                                    builtins.list(
                                        OrderedDict.fromkeys(
                                            utility.get_command_pallete(commands, indices)
                                        )
                                    )
                                )
                            ),
                            cmd="less",
                        )

                    which = input(
                        "Which line do you wan't to edit (* for all matches, C for cancel)?"
                    )

                    if len(which) == 1 and which == "*":
                        for i in indices:
                            commands[int(i) - 1] = cmd
                        else:
                            testdb.remove_command(summand, commands)
                    elif str(which).lower() == "c":
                        exit()
                    else:
                        which = which.split(",")
                        result = True
                        for i in which:
                            if int(i) - 1 in indices:
                                commands[int(i) - 1] = cmd
                            else:
                                result = False
                        if result:
                            testdb.remove_command(summand=summand, command=commands)
                        else:
                            error("Your line didn't found.")
                except ValueError:
                    error("You should enter a line number.")

        if name != None:  # name verified
            if not utility.check_for_existence(utility.sha256(name)):
                j_status, j_save = utility.edit_list(
                    utility.sha256(summand), utility.sha256(name)
                )
                db_status, db_save = testdb.edit_list(summand, name)
                sucess(j_save)
            else:
                error("Your new Summand name is already existed.")

        if description != None:
            testdb.update_description(summand, description)
    else:
        error("Your desired Summmand didn't found.")

    # else:
    # error("")


# INFO: list is optional, when removing a command if Tuple:command has just commands it should read the list name from str:list
@app.command(help="Remove your summand.")
def remove(
    summand: str = typer.Argument(None, help="Choose the Summand."),
    command: str = typer.Option(
        None, "-C", "--command", help="Remove your commands from specific Summand."
    ),
    description: bool = typer.Option(
        False, "-D", "--description", help="Remove the summand description."
    ),
    split: str = typer.Option(",", "-S", "--split", help="Split your inputs."),
):

    if summand == None:
        warning("Nothing specified, nothing removed.")

    if utility.check_for_existence(utility.sha256(summand)):
        if command != None:
            cmd = command.split(split)
            commands = testdb.exact_search(summand)[0]["Command"]

            cmd = set(cmd)
            for i in cmd:
                if commands.count(i) <= 1:
                    try:
                        commands.remove(i)
                        testdb.remove_command(summand, commands)
                        # commands

                    except:
                        error("Your command did not ")
                if commands.count(i) > 1:
                    indices = [c for c, x in enumerate(commands) if x == i]

                    if utility.detect_shell()[0] in ["powershell", "cmd"]:
                        pydoc.pipepager(
                            (
                                utility.list_to_str(
                                    builtins.list(
                                        OrderedDict.fromkeys(
                                            utility.get_command_pallete(commands, indices)
                                        )
                                    )
                                )
                            ),
                            cmd="more",
                        )

                    else:
                        pydoc.pipepager(
                            (
                                utility.list_to_str(
                                    builtins.list(
                                        OrderedDict.fromkeys(
                                            utility.get_command_pallete(commands, indices)
                                        )
                                    )
                                )
                            ),
                            cmd="less",
                        )
                    
                    which = input(
                        "Which line do you wan't to edit (* for all matches, C for cancel)?"
                    )

                    if len(which) == 1 and which == "*":
                        for i in sorted(indices, reverse=True):
                            del commands[i]
                        else:
                            testdb.remove_command(summand, commands)
                    elif str(which).lower() == "c":
                        exit()
                    else:
                        try:
                            which = which.split(",")
                            for i in sorted(which, reverse=True):
                                if i in indices:
                                    del commands[int(i) - 1]
                                else:
                                    status = False
                                    break
                            else:
                                if status:
                                    testdb.remove_command(summand, commands)
                                else:
                                    error(
                                        "Your line is not consisting the selected command."
                                    )
                        except:
                            error("Problem parsing your input.")

        if command == None and description == False:
            try:
                a = utility.delete_list(utility.sha256(summand))
                b = testdb.delete(summand)
                if a == True and b == True:
                    sucess(f"Summand removed successfully. Summand's Name: {summand}")
                else:
                    error("Something went wrong")
            except:
                error("Error Occurred.")
        if description != False:
            try:
                testdb.update_description(summand)
                sucess("Description removed.")
            except:
                error("Something went wrong.")
    else:
        error("Summan did not found.")


# TODO This Should Have --listname --listitems --listdescription


@app.command()
def help(
    summand: str = typer.Argument("", help="Command to get help for."),
    number: bool = typer.Option(
        False, "-N", "--number", help="numeric print your output."
    ),
):
    utility.first_setup()

    if utility.check_for_existence(utility.sha256(summand)):
        data = testdb.get_command(summand)
        if data[0] == True:
            if data[1] != [""]:
                for n, i in enumerate(data[1]):
                    if number == True:
                        print(n, i)
                    else:
                        print(i)
            else:
                error("No Summands we re found.")
        else:
            error(data[1])
    else:
        error("Your desired Summand was not found.")


@app.command(help="Reset your database.")
def reset():
    typer.echo("Are You Sure You Want To Reset The Database? (y/n)")
    if input() in ["Y", "y", "yes", "Yes", "YES"]:
        testdb.delete_all_data()
        sucess("The database was reset successfully.")
        utility.lists_json_reset()
    else:
        typer.echo("The database cannot be reset.")


# from rich import print

# TODO: except list_name / Done
# except command description times and ...
# New Versions Custom Suffix Html,Md File, Text,
# TODO: Feature : listname not defined do you want to continue? / Done
# TODO: git log.
@app.command(help="Export your lists.")
def export(
    dir: Path = typer.Argument(...),
    summand: str = typer.Option(
        None, "--summand"
    ),  # Required typing.Union but typer doesn't soppurt it.
    all: bool = typer.Option(False, "-A", "--all"),
    include: bool = typer.Option(False, "-I", "--include"),
    exclude: bool = typer.Option(False, "-E", "--exclude"),
    filename: str = typer.Option(..., prompt=True),
    split: str = typer.Option(",", "-S", "--split"),
):

    if all:
        status, save = e.export(save_path=dir, filename=filename, all=all)
    elif include:
        if exclude:
            status, save = False, "You cannot use both include and exclude simultaneously."
        else:
            if summand != None:
                try:
                    summand = summand.split(split)

                    exist = []
                    not_exist = []

                    for i in summand:
                        if utility.check_for_existence(utility.sha256(i)):
                            exist.append(i)
                        else:
                            not_exist.append(i)

                        status, save = e.export(
                            save_path=dir,
                            filename=filename,
                            include=True,
                            listname=exist,
                        )
                except:
                    status, save = (
                        False,
                        "There's a problem with splitting your Summands.",
                    )
            else:
                status, save = (
                    False,
                    "You should specify your summand/s to include or exclude it.",
                )
    elif exclude:
        if summand != None:
            try:
                summand = summand.split(split)
                exist = []
                not_exist = []
                for i in summand:
                    if utility.check_for_existence(utility.sha256(i)):
                        exist.append(i)
                    else:
                        not_exist.append(i)

                status, save = e.export(
                    save_path=dir, filename=filename, listname=exist, e=True
                )

            except ValueError:
                status, save = False, "There's a problem with splitting your Summands."

    else:
        status, save = e.export(save_path=dir, filename=filename, all=True)

    if status:
        sucess(save)
    else:
        error(save)


@app.command("import", help="Import external Summands from a file.")
def cli_import_list(
    location: List[Path],
    ignore: bool = typer.Option(False, "-I", "--ignore"),
    show=None,
):

    status, data = i.importer(location, ignore)
    if utility.all_equal(status):
        if status[0] == True:
            status = True
        else:
            status = False

    if status == True:
        typer.echo("All Summands imported successfully :)")
    elif status == False:
        typer.secho(data, fg=typer.colors.RED, err=True)
    else:
        typer.echo("Some Summands were already existed in your database.")
        print(data)


if __name__ == "__main__":
    app()

# TODO Add Category
# TODO Add a way to add a new item to a list
# TODO Some Short Commands Helper
# TODO Add Description
# TODO Add Tables
# TODO Relationships
# TODO Add add Worflows
# TODO white space acceptance in add command
# Bug: when edit a list that doesn't edit in lists.json
# TODO Description
# ... list --sort [a-z 0-9 r(stands for reverse)] --search [keyword] --edit [list_name new_list_name] --delete [list_name] --add [list_name]--reset [delet_all_lists] --help
# ... reset {{{ newversions --time [from_time to_time] --list [delete_all] --commands [delete_everyting_except_list_names]--help
# ... add --list [list_name] --description [list_name,Description] --command [list,command] --help
# ... workflow --new
# ... import [location]
# ... export [location]
# ... activate
# ... run [list_name] run time save
# History
# --changelog --version [report -b {bug_decription} -f {feature_description} https://typer.tiangolo.com/tutorial/options/autocompletion/
# Run Git For Version Controlling and Each (Delte,Edit,Add) Should Track

# TODO Today:
# Add Time Of Add
# edit / Done
# Delete / Done
# Sort / Working
# import / Done

# Import / Export
# Usage: Can Use For Setup Invironment
# Fix Bug #1 : When DB Edit lists.json should edit / Fixed
# Fix Bug #2 : Block Edit With Same Name/ Fixed
# Fix Bug #3 : database reset yes option should accept [Y,y,yes,YES,Yes] / Fixed
# Bug #4: First Time Use And Database Error Are The Same In db.py>export() / Fixed

# TODO Done:
# Delete List
# Edit List
# Add List
# List And Serach
# Reset
# Description
# time
# Command
# run
# Callback / not done
# export / not done / list name export
# Merge Exported Files
