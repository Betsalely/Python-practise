tasks = []

def display_tasks():
    if len(tasks) > 0:
        for i, task in enumerate(tasks):
                print(f"{i + 1}: {task}")
        print("\n")

while True:
    display_tasks()
    user_input = input('Add a task by typing anything but a number or tick off a task by typing its number: ')
    try:
        val = int(user_input)

        tasks.pop(val-1)
    except ValueError:
        tasks.append(user_input)