#

## Commands

`-- help`

`--version --new_version --current_version`

`... list --sort [a-z 0-9 r(stands for reverse)] --search [keyword] --edit [list_name new_list_name] --delete [list_name] --add [command] --reset [delete_all_lists] --commands[show_list_commands] --help`

`... reset {{{ newversions --time [from_time to_time] --list [delete_all] --commands [delete_everyting_except_list_names]--help`

`... add --list [list_name] --description [list_name,Description] --command [list,command] --split --help`

`... workflow --new --description --help`

`... import [location]`

`... export [location] --list [list_name] --split [spliter] --except [list_name] --all [bool] [-r,-remove] [col_name like description]` if -e [bool] added after list_name it means except

`... activate {{new_version}|sql|tinydb --help`

`... run [list_name] ~ number of commands`

`... edit --list_name [list_name new_list_name] --list_description [list_name new_description] --list_commands [list_name , command, new_commnad] --workflow_name [workflow_name new_workflow_name] --workflow_description [workflow_name new_description] --workflow_items [item_name new_item_name] --help`

`... delete --list_name list_name --commands [list_name, command_name] --workflow [workflow_name]`

`... execute --list_name [list_name] --command [command_name] --help`

`... merge filename1 filename2 ... filename_n`

define your info into command

Logfile

## TODO

- [x] add command to list
- [x] execute command
-[x] Test For Work On `.exe`
-[ ] Test Files
-[x] output for linux

JSON file for help

### Updates

- make a feature that allows use variable in the command and you can use the list name and variable value in the command
- make private directory (values work in private directory) with this you can have many list with same name but in different directories

### Helpful links

- [Initialize Required Packages](https://github.com/cientgu/VQ-Diffusion/blob/main/install_req.sh#L2)

Today:
Complete Export / Done
Git Python / Some Exprince

verions 1.
add
list
import
export
delete
edit
run
reset
help
version bug report conf file

### Idea @Mazdakdev

 1. Add multiple commands from a bash script file
 2. rename **Delete** to **Remove**
 3. run summands without using run option
