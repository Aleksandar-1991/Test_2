import os
from ctypes import oledll
from dataclasses import field

while (user_input := input()) != "End":
    command, file_name, *args = user_input.split("-")
    if command == "Create":
        open(file_name, "w").close()
    elif command == "Add":
        content = args[0]
        with open(file_name, "a") as file:
            file.write(f"{content}\n")
    elif command == "Replace":
        old_string, new_string = args[0], args[1]
        # if os.path.exists(file_name):
        #     with open(file_name, "r") as file:
        #         text = file.read()
        #     text = text.replace(old_string, new_string)
        #     with open(file_name, "w") as file:
        #         file.write(f"{text}\n")
        # else:
        #     print("An error occurred")
        try:
            with open(file_name, "r+") as file:
                content = file.read()
                file.seek(0)
                file.truncate(0)
                file.write(content.replace(old_string, new_string))
        except FileNotFoundError:
            print("An error occurred")


    elif command == "Delete":
        if os.path.exists(file_name):
            os.remove(file_name)
        else:
            print("An error occurred")