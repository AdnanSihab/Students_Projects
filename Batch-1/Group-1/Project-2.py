def see_list(tlist):
    print("your to do list:")
    index = 1
    for i in tlist:
        print(f"{index}.{i}")
        index += 1
    print("\n")
def add_task(tlist):
    add = input("Do you want to add any task to your list?\n(yes/no): ")
    if add.lower() == "yes":
        add_lst=input("task to add:")
        tlist.append(add_lst)
        print(f"'{add_lst}' is added to the list!")
    else:
        print()

def remove_task(tlist):
    rem = input("Do you want to remove any task?\n(yes/no): ")
    if rem.lower() == "yes":
        task_to_remove = input("task to remove: ")
        if task_to_remove in tlist:
            tlist.remove(task_to_remove)
            print(f"{task_to_remove} is remove from the list!")
        else:
            print("Task not found in the list.")
    else:
        print()

def main():
    tlist = []

    while True:
        question = input("What do you want to do?\n1. See my list\n2. Add task\n3. Remove task\n4. Exit\nAnswer: ")

        if question == "1":
            see_list(tlist)
        elif question == "2":
            add_task(tlist)
        elif question == "3":
            remove_task(tlist)
        elif question == "4":
            print("Exiting the program.")
            break

main()