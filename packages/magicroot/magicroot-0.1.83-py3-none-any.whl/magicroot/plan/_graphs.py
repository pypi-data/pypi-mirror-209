from ._tasks import ProjectTasks


def graph(folder_mang):
    ProjectTasks().build(input=folder_mang, output=folder_mang, clear_effort=False, update_tasks=False,
                         update_graphs=True)




