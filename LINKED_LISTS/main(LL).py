from LINKED_LISTS.linked_list import LinkedList
from LINKED_LISTS.node import Node

def main():
    linked_list = LinkedList()
    linked_list.append("Fred")
    linked_list.append("Tom")

    print(linked_list)

    index_to_get = 1
    node = linked_list.get(index_to_get)
    if node:
        print(f"\nNode at index {index_to_get}: {node}")
    else:
        print(f"\nNo node found at index {index_to_get}")

    out_of_bounds_index = 10
    node = linked_list.get(out_of_bounds_index)
    if node:
        print(f"\nNode at index {out_of_bounds_index}: {node}")
    else:
        print(f"\nNo node found at index {out_of_bounds_index}")

if __name__ == '__main__':
    main()


