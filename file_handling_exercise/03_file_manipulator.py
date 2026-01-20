import os

while (user_input := input()) != "End":
    command, file_name = user_input.split("-")[0:2]
    # print(command, file_name)
    if command == "Create":
        open(file_name, "w").close()
    elif command == "Add":
        file_content = user_input.split("-")[2]
        with open(file_name, "a") as file:
            file.write(f"{file_content}\n")
    elif command == "Replace":
        old_string, new_string = user_input.split("-")[2:4]
        # print(old_string, new_string)
        if os.path.exists(file_name):
            text = ""
            # print("file exists")
            with open(file_name, "r+") as file:
                text = file.read()
                # print(f"File content is: {text}")
                text = text.replace(old_string, new_string)
                # print(f"New content is: {text}")
            with open(file_name, "w+") as file:
                file.write(text)
                # print("write completed")
        else:
            print("An error occurred")
    elif command == "Delete":
         if os.path.exists(file_name):
             os.remove(file_name)
         else:
             print("An error occurred")



