menulist=( "1. Print the list",
        "2. Add a name to the list",
        "3. Remove a name from the list",
        "4. Change an item in the list",
        "9. Quit")

list=("johny","tom","kim","tim","jim")

target=input("Pick an item from the menu:")
 while (target in list):
     if target="1"
        print list
    elif target="2"
        Addname=input("Type in a name to add:")
        list=list.insert(Addname)
            print menulist()
    elif target="3"
        Removename=input("What name would you like to remove:")
        list=list.remove(Removename)
            print menulist()
    elif target="4"
        Changename=input(What name would you like to change:")
        changetoname=input("What is the new name:")
        list=list.replace('Changename','changetoname')
            print menulist()
    elif target="9"
            print"good bye"
