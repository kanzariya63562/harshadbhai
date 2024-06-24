# Write a Python program to combine values in python list of dictionaries. Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, o {'item': 'item1', 'amount': 750}] Expected Output: Counter ({'item1': 1150, 'item2': 300}).





def combine_values(data):
    
    combined_amounts = Counter()

   
    for entry in data:
        item = entry['item']
        amount = entry['amount']
        combined_amounts[item] += amount

    return combined_amounts


data = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]


result = combine_values(data)

print("Counter:", result)