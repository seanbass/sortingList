my_list = [67, 45, 2, 13, 1, 998]
new_list = []

while my_list:
    minimum = my_list[0]
    for x in my_list:
        if x < minimum:
            minimum = x

            new_list.append(minimum)
            my_list.remove(minimum)

print (my_list)


    

my_list2 = [89, 23, 33, 45, 10, 12, 45, 45, 45,]
new_list2 = []

while my_list2:
    minimum2 = my_list2[0]
    for i in my_list2:
        if i < minimum2:
            minimum2 = i

            new_list2.append(minimum2)
            my_list2.remove(minimum2)

print (my_list2)    