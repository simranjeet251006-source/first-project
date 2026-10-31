lists = []

while True:
    user_action = input("Type add, show, edit, complete or exit: ")


    match user_action:
        case "add":
            todo = input("Enter a todo: ")
            lists.append(todo)
            print(f"Added {todo} to the list.")

        case "show":
            print("Your todos:")
            for index, item in enumerate(lists, start=1):
                print(f"{index}. {item}")

        case "edit":
            index = int(input("Enter the number of the todo to edit: ")) - 1
            if 0 <= index < len(lists):
                new_todo = input("Enter the new todo: ")
                lists[index] = new_todo
                print(f"Updated todo {index + 1} to {new_todo}.")
            else:
                print("Invalid index.")

        case "complete":
            index = int(input("Enter the number of the todo to complete: ")) - 1
            if 0 <= index < len(lists):
                completed_todo = lists.pop(index)
                print(f"Completed and removed {completed_todo} from the list.")
            else:
                print("Invalid index.")

        case "exit":
            print("Exiting the program.")
            break

        case _:
            print("Unknown command. Please try again.")