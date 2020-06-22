# linear search


def search_linearly(the_list, key):
    for index, i in enumerate(the_list):
        if i == key:
            return index


my_list = [12, 23, 4, 42, 54, 33, 2, 342, 45, 54, 6, 78, 56, 78, 96, 43, 22, 89]
for index, i in enumerate(my_list):
    print('%d : %d' % (index, i))
print()
print('index at: %d' % search_linearly(my_list, 56))
