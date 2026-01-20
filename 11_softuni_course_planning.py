
def Add(lessons: list, new_lesson: str) -> list:
    if new_lesson not in lessons:
        lessons.append(new_lesson)
        return lessons

def Insert(lessons: list, new_lesson: str, idx: int) -> list:
    if new_lesson not in lessons:
        lessons.insert(idx, new_lesson)
    return lessons

def Remove(lessons: list, new_lesson: str) -> list:
    new_lesson_index = lessons.index(new_lesson)
    if (lessons[new_lesson_index+1] in range(len(lessons))) and  (lessons[new_lesson_index+1]==f"{new_lesson}-Exercise"):
        lessons.pop(lessons[new_lesson_index+1])
    if new_lesson in lessons:
        lessons.remove(new_lesson)
    return lessons

def Swap(lessons: list, first_title: str, second_title: str) -> list:
    if first_title in lessons and second_title in lessons:
        first_title_position = lessons.index(first_title)
        second_title_position = lessons.index(second_title)
        first_title_has_exercise = False
        second_title_has_exercise = False
        if first_title_position+1 in range(len(lessons)):
            first_title_has_exercise = f"{first_title}-Exercise" in lessons[first_title_position+1]
        if second_title_position+1 in range(len(lessons)):
            second_title_has_exercise = f"{second_title}-Exercise" in lessons[second_title_position+1]
        #First swap lessons
        lessons[first_title_position], lessons[second_title_position] = (
            lessons[second_title_position], lessons[first_title_position])
        #Time for swap exercises
        if first_title_has_exercise and second_title_has_exercise:
            lessons[first_title_position+1], lessons[second_title_position+1] = (
                lessons[second_title_position+1], lessons[first_title_position+1])
        elif first_title_has_exercise and not second_title_has_exercise:
            lessons.insert(second_title_position+1, lessons.pop(first_title_position+1))
        elif not first_title_has_exercise and second_title_has_exercise:
            lessons.insert(first_title_position+1, lessons.pop(second_title_position+1))

    # if first_title in lessons and second_title in lessons:
    #     lessons[first_title_position], lessons[second_title_position] = \
    #         lessons[second_title_position], lessons[first_title_position]
    # if (f"{first_title}-Exercise" in lessons) and lessons[second_title_position+1] != f"{first_title}-Exercise":
    #     lessons.insert(lessons[second_title_position+1], lessons.pop(first_title_position+1))
    # if (f"{second_title}-Exercise" in lessons) and lessons[first_title_position+1] != f"{second_title}-Exercise":
    #     lessons.insert(first_title_position+1, lessons.pop(second_title_position+1))
    return lessons

def Exercise(lessons: list, title: str) -> list:
    exercise_name = f"{title}-Exercise"
    if title in lessons and exercise_name not in lessons:
        title_index = lessons.index(title)
        lessons.insert(title_index+1,exercise_name)
    elif title not in lessons:
        lessons.append(title)
        lessons.append(exercise_name)
    return lessons

list_of_lessons = input().split(', ')
command = input().split(':')

while command[0] != 'course start':
    action_name = command[0]
    lesson_name = command[1]

    if  action_name=='Add':
        list_of_lessons=Add(list_of_lessons,lesson_name)
    elif  action_name=='Insert':
        list_of_lessons=Insert(list_of_lessons, lesson_name, int(command[2]))
    elif  action_name=='Remove':
        list_of_lessons=Remove(list_of_lessons, lesson_name)
    elif  action_name=='Swap':
        second_name=command[2]
        list_of_lessons = Swap(list_of_lessons, lesson_name, second_name)
    elif  action_name=='Exercise':
        list_of_lessons = Exercise(list_of_lessons, lesson_name)

    command=input().split(":")

for index, lesson in enumerate(list_of_lessons):
    print(f"{index+1}.{lesson}")

