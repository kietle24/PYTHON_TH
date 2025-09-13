# task_module.py
def add_task(task_list, name, status):
    task_list.append({"name": name, "status": status})
    return task_list
