max_items_in_bag = 3


def sb_combos(curr_bag, remaining_items):
    if (len(curr_bag)) == max_items_in_bag:
        # Base case: shopping bag full
        bag_value = 0
        for item in curr_bag:
            bag_value += item['price']
            print(item['name'], ' ', end=' ')
        print('=', bag_value)
    else:
        for index, item in enumerate(remaining_items):
            curr_bag.append(item)
            remaining_items.pop(index)

            sb_combos(curr_bag, remaining_items)

            remaining_items.insert(index, item)
            curr_bag.pop()


items = [
    {
        'name': 'Milk',
        'price': 1.25
    },
    {
        'name': 'Belt',
        'price': 23.55
    },
    {
        'name': 'Toys',
        'price': 19.05
    },
    {
        'name': 'Cups',
        'price': 11.85
    }
]

bag = []
sb_combos(bag, items)
