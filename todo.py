#go through existing todo's, list each one and ask if the user completed it
#if completed remove item and if not keep it
try:
    with open("todo.txt","r") as f:
        content = (f.read())
        todo_list = content.split("\n")

except FileNotFoundError:
    with open("todo.txt","w") as f:
        print(f.write(""))

remaining_todo_list = []

for todo in todo_list:
    print(todo)
    user_input = input("completed? (y/n)")
    if user_input != "y":
        remaining_todo_list.append(todo)

while True:
    new_todo = input("Add todo (q to quit): ")
    if new_todo == "q":
        break
    else:
        remaining_todo_list.append(new_todo)

with open("todo.txt", "w") as f:
    output = "\n".join(remaining_todo_list)
    f.write(output)





#ask if user wants to add more todos
#allow them to quit function