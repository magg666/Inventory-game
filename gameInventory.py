# This is the file where you must work. Write code in the functions, create new functions,
# so they work according to the specification
import csv
# Displays the inventory.


def display_inventory(inventory):
    print("Inventory:")
    for key, value in sorted(inventory.items()):
        print(value, key)
        total = sum(inventory.values())
        print("Total numbers of items: ", total)


# Adds to the inventory dictionary a list of items from added_items.
def add_to_inventory(inventory, added_items):
    for item in added_items:
        if item in inventory:
            inventory[item] += 1
        if item not in inventory:
            inventory[item] = 1


# Takes your inventory and displays it in a well-organized table with
# each column right-justified. The input argument is an order parameter (string)
# which works as the following:
# - None (by default) means the table is unordered
# - "count,desc" means the table is ordered by count (of items in the inventory)
#   in descending order
# - "count,asc" means the table is ordered by count in ascending order
def print_table(inventory, order=None):
    a = (max(len(key) for key in inventory.keys()))+2
    b = (max(len(str(value)) for value in inventory.values()))+4
    print("\nInventory:")
    print('{:>{b}}''{:>{a}}'.format("count", "item name", b=b, a=a))
    print("-" * (a+b))
    if order == "count,desc":
        for value in sorted(inventory, key=inventory.get, reverse=True):
            print('{:>{b}}''{:>{a}}'.format(inventory[value], value, b=b, a=a))
    elif order == "count,asc":
        for value in sorted(inventory, key=inventory.get):
            print('{:>{b}}''{:>{a}}'.format(inventory[value], value, b=b, a=a))
    elif order is None:
        for key, value in sorted(inventory.items()):
            print('{:>{b}}''{:>{a}}'.format(value, key, b=b, a=a))
    else:
        exit()
    print("-" * (a+b))
    total = sum(inventory.values())
    print("Total numbers of items: ", total)


# Imports new inventory items from a file
# The filename comes as an argument, but by default it's
# "import_inventory.csv". The import automatically merges items by name.
# The file format is plain text with comma separated values (CSV).
def import_inventory(inventory, filename="import_inventory.csv"):
    with open(filename, 'r') as file:
        for line in file.readlines():
            file_treasure = line.split(",")
            for item in file_treasure:
                if item in inventory:
                    inventory[item] += 1
                if item not in inventory:
                    inventory[item] = 1
# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "export_inventory.csv". The file format is the same plain text
# with comma separated values (CSV).


def export_inventory(inventory, filename="export_inventory.csv"):
    l3 = []
    l1 = []
    l2 = []
    l4 = []
    for value in inventory:
        l3.append((value,) * inventory[value])
    for n in range(len(l3)):
        l1.append(','.join(l3[n]))
    for i in l1:
        l2.append(i.split(','))
    for line in l2:
        for item in line:
            l4.append(item)
    with open(filename, 'w') as file:
        wr = csv.writer(file)
        wr.writerow(l4)


def make_list_all(file_name):
    with open(file_name, 'r') as file:
        set_of_all = file.read()
        set_of_all = set_of_all.replace('\n', '\t')
        set_of_all = set_of_all.split('\t')
        del set_of_all[-1]
        return set_of_all
