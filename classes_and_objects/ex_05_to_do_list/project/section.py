from certifi import where

from classes_and_objects.ex_05_to_do_list.project.task import Task

class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks: list[Task] = []

    def add_task(self, new_task: Task) -> str:
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str) -> str:
        # t = next((t for t in self.tasks if t.name == task_name), None)
        t = next((t for t in self.tasks if t.name == task_name), None)
        if not t:
            return f"Could not find task with the name {task_name}"
        t.completed = True
        return f"Completed task {task_name}"

    def clean_section(self) -> str:
        all_tasks = len(self.tasks)
        self.tasks = [t for t in self.tasks if t.completed == False]
        return f"Cleared {all_tasks - len(self.tasks)} tasks."

    def view_section(self) -> str:
        # result = f"Section {self.name}:\n"
        # for task in self.tasks:
        #     result += f"{task.details()}\n"
        # return result
        tasks_details = "\n".join(t.details() for t in self.tasks)
        return f"Section {self.name}:\n{tasks_details}"