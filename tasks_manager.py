
def display_list():
    print('_____________________________________________ \n TASKS |  DEADLINE   |   PRIORITY   |   STATUS')
    with open("tasks.txt", "r") as tasks:
        print(tasks.readlines)


ext_state = False
while not ext_state:
    usr_in = input("choose any: \n   1-view,\n   2-delete,\n   3-edit,\n   4-exit\n ")
    match usr_in:
        case "1": 
            print("VIEW")
            display_list()
        case "2":
            print("DEL")
        case "3":
            print("EDIT")
        case "4":
            print("EXIT")
            ext_state = True
        case _ :
            print('Please enter valid input, (1, 2, 3 or 4)')
