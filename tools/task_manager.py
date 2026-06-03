import os

TASK_FILE = "data/tasks.txt"

os.makedirs("data", exist_ok=True)

if not os.path.exists(TASK_FILE):
    with open(TASK_FILE, "w") as f:
        pass


def add_task(task):
    with open(TASK_FILE, "a", encoding="utf-8") as f:
        f.write(task + "\n")

    return f"Task added: {task}"


def list_tasks():

    with open(TASK_FILE, "r", encoding="utf-8") as f:
        tasks = [line.strip() for line in f.readlines()]

    if not tasks:
        return "No tasks available."

    result = ""

    for i, task in enumerate(tasks, start=1):
        result += f"{i}. {task}\n"

    return result


def delete_task(index):

    with open(TASK_FILE, "r", encoding="utf-8") as f:
        tasks = [line.strip() for line in f.readlines()]

    try:
        removed_task = tasks.pop(index - 1)

        with open(TASK_FILE, "w", encoding="utf-8") as f:
            for task in tasks:
                f.write(task + "\n")

        return f"Deleted task: {removed_task}"

    except:
        return "Invalid task number"