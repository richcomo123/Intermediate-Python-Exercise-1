def get_unique_list(lyst):
    unique_list = []
    for x in lyst:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list



  

my_list=[1,2,3,2,1,4]
unique_list=get_unique_list(my_list)
print(unique_list)