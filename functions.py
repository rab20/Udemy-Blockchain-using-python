# Unpacking function argumaent using a *

def unlimited_arguments(*args):
    # * will convert the values into a tuple
    print(args)
    for argument in args:
        print(argument)


unlimited_arguments(1, 2, 3, 4, 5)

unlimited_arguments([1, 2, 3, 4, 5])

unlimited_arguments(*[1, 2, 3, 4, 5])

# Unpacking a dictionary using **


def unlimited_arguments_dict(**keyword_args):
    print(keyword_args)
    for k, argument in keyword_args.items():
        print(k, argument)


unlimited_arguments_dict(name='Bharat', age=28)

# * gives a tuple and ** give a dictionary
