def calculate_total(items_purchased, grocery_list):
    item_prices = {
        "milk": 2.50,
        "eggs": 3.25,
        "bread": 1.21,
        "cheese": 3.50,
        "apples": 7.44,
        "bananas": 3.88,
        "carrots": 3.89,
        "lettuce": 1.12,
        "potatoes": 32.21,
        "cereal": 5.99,
    }

    # Don't touch above this line

    # A list of all the item names in grocery_list that weren't found in items_purchased in order.
    unpurchased_items = grocery_list

    for item in items_purchased:
        if item in grocery_list:
            unpurchased_items.remove(item)

    print(unpurchased_items)
    print('*')
    #receipt: A dictionary containing all the items Emma purchased, even stuff not on her list. The keys are the item names and the values are their respective prices from the item_prices dictionary.

    receipt = {}

    for item in items_purchased:
        receipt[item] = item_prices[item]

    print(receipt)
    print('**')

    total = 0

    for item in receipt:
        total = total + receipt[item]

    print(total)
    print('***')

    return unpurchased_items, receipt, total


