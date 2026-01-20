# path = input().split("\\")
# file_name_split = path[-1].split(".")
file_name, file_extension = input().split("\\")[-1].split(".")
file_name, file_extension = file_name_split[0], file_name_split[1]
print(f"File name: {file_name}\nFile extension: {file_extension}")
