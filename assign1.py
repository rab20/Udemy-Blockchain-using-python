name = input('Please enter name : ')
age = input('Please enter age : ')


def get_data():
    print('Name : ' + name + ' ' + 'Age : ' + age)


def get_decade():
    return int(age)//10


get_data()
print("Decades lived : " + str(get_decade()))


def get_input1():
    return input("Please enter string 1 :")


def get_input2():
    return input("Please enter string 2 :")


print(get_input1() + ' ' + get_input2())
