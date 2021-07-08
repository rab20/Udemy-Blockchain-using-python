# 1) Write a normal function that accepts another function as an argument. Output the result of that other function in your “normal” function.

simple_list = [1, 2, 3, 4, 5]


def multiply_2(in_list):
    new_list = [el * 2 for el in in_list]
    return (new_list)


def multiply_3(in_list):
    new_list = [el * 3 for el in in_list]
    return (new_list)


def multiply_5(el):
    return el*5


def normal_function(func):
    valid_op = func(simple_list)
    print(valid_op)


def normal_function_map(func, *args):
    valid_op = (list(map(func, *args)))
    # 4) Format the output of your “normal” function such that numbers look nice and are centered in a 40 character column.
    print('The output values are : {:^40}'.format(str(valid_op)))


normal_function(multiply_2)                         # without using map
normal_function(multiply_3)                         # without using map
normal_function_map(multiply_5, simple_list)        # using map


# 2) Call your “normal” function by passing a lambda function – which performs any operation of your choice – as an argument.

normal_function_map(lambda el: el*10, simple_list)

# 3) Tweak your normal function by allowing an infinite amount of arguments on which your lambda function will be executed.

normal_function_map(lambda el: el*20, (1, 2, 3, 4, 5, 6, 7, 8))
