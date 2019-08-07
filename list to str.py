def concatenate_list_date(list):
    result=""
    for elements in list:
       result+=str(elements)
    return result
print(concatenate_list_date([1,5,15,2]))