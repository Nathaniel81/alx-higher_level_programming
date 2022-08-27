#!/b/usr/bin/python3

def max_integer(my_list=[]):
    if my_list == []:
        return None

    maxNumber = my_list[0]
    for number in my_list:
        if number > maxNumber:
            maxNumber = number

    return maxNumber
