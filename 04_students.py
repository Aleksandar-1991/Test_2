students = list()

while ':' in (command := input()):
    name, id_, course = commmand.split(':')
    temp_dict = dict()
    temp_dict['name'] = name
    temp_dict['id_']  = id_
    temp_dict['course'] = course
    students.append(temp_dict)

course_required_raw_format = command
course_required = course_required_raw_format.replace('_', ' ')
for student in students:
    if student['course'] == course_required:
        print(f"{student['name']} - {student['id_']}")
