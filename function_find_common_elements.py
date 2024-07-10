def find_common_elements(list1, list2):
    common_elements = [element for element in list1 if element in list2]
    unique_to_list1 = [element for element in list1 if element not in list2]
    unique_to_list2 = [element for element in list2 if element not in list1]
    
    if common_elements:
        return common_elements, unique_to_list1, unique_to_list2
    else:
        return []

# 示例
list1 = ['cat']
list2 = ['lion', 'cat']



if find_common_elements(list1, list2):
    common_elements, unique_to_list1, unique_to_list2 = find_common_elements(list1, list2)
    print(f"Common elements: {common_elements}")
    print(f"unique elements in list1: {unique_to_list1}")
    print(f"unique elements in list1: {unique_to_list2}")
else:
    print("No common elements found.")