# Imagine an accounting routine used in a book shop. It works on a list with sublists, which look like this: 

# Order Number	Book Title and Author	Quantity	Price per Item
# 34587	Learning Python, Mark Lutz	4	40.95
# 98762	Programming Python, Mark Lutz	5	56.80
# 77226	Head First Python, Paul Barry	3	32.95
# 88112	Einführung in Python3, Bernd Klein	3	24.99


# Write a Python program, which returns a list with 2-tuples. Each tuple consists of a the order number and the product of the price per items and the quantity. The product should be increased by 10,- € if the value of the order is less than 100,00 €. 
# Write a Python program using lambda and map.

orders = [34587, 98762, 77226, 88112]
book_titles = ['Learning Python, Mark Lutz', 'Programming Python, Mark Lutz', 'Head First Python, Paul Barry',
               'Einführung in Python3, Bernd Klein']
quantity = [4, 5, 3, 3]
price_per_item = [40.95, 56.80, 32.95, 24.99]

book_store = [
    orders,
    book_titles,
    quantity,
    price_per_item
]

r = map(lambda l1, l2: l1 * l2 + 10 if l1 * l2 < 100 else l1 * l2, book_store[2], book_store[3])


print(list(r))
