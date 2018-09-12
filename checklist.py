# coding: utf8
checklist = list()

# adding item to the array
def create(item):
    checklist.append(item)

# reading specicif item of the array using its index
def read(index):
    item = checklist[index]
    return item

# overriding array using an index of specicic item
def update(index, item):
    checklist[index] = item

# removing the last item of the array
def destroy(index):
    checklist.pop(index)

# displaying the entire array

def list_all_items():
    index = 0
    for list_item in checklist:
        # yellow output
        print('\033[33m' + "{} {}".format(index, list_item))
        index += 1
    return index

def mark_completed(index):
    # green output
    print('\033[32m' + '√ ' + checklist[index])


def user_input(prompt):
    user_input = input(prompt)
    return user_input

def select(function_code):

    # Create item
    if function_code == "A":
        input_item = user_input("Insert item to the list >>> ")
        create(input_item)

     # Print all items
    elif function_code == "P":
        list_all_items()

    # Read item
    elif function_code == "R":
        item_index = user_input("Insert Index Number of an Item >>> ")

        if checklist == list():
            # green output
            print ('\033[32m' + "The list is empty")
            running = True
        else:
            print(read(int(item_index)))

    # mark as completed
    elif function_code == "C":
        marked_item = user_input("Insert Index of an Item to be marked as completed >>> ")
        mark_completed(int(marked_item))

    # delete
    elif function_code == "D":
        del_item = user_input("Insert Index of an Item to delete >>> ")

        if checklist == list():
            # yellow output
            print ('\033[33m' + "The list is empty")
            running = True
        else:
            # red output
            print('\033[31m' + read(int(del_item)) + " - deleted now")
            destroy(int(del_item))

    elif function_code == "Q":
        # This is where we want to stop our loop
        return False

    # Catch all
    else:
        # magenta output
        print('\033[35m' + "Unknown Option")
    return True

running = True
while running:
    selection = user_input('\033[0m'
        "Press A to add to list, R to Read from list, P to display list, C to mark as completed, D to delete an item and Q to quit >>> ")
    running = select(selection)
