def multiply_by_3(list1,list2):

    new_list = map(lambda x,y: x-y ,list1,list2)

    return new_list


print(list(multiply_by_3([4, 5, 2, 9])))