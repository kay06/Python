tags= [ 'python', 'development', 'tutorials', 'code']

number_of_tags = len(tags)
#len(list_name) will grab the number of elements in your list_name starting from 1
print(number_of_tags)

last_items = tags[-1]
#list_name[neg_number] will start from the end
print(last_items)

index_of_last_item = tags.index(last_items)
#list_name.index(element) will return the index of the specified element
print(index_of_last_item)