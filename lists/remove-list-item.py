list_to_clean = [1, 2, 3, 4, 5]

def remove_first_and_last (list_to_clean):
    first, *middle_content, last = list_to_clean
    return middle_content

print(remove_first_and_last(list_to_clean))