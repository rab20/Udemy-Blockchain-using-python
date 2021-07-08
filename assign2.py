
# 1) Create a list of names and use a for loop to output the length of each name (len() ).
name_list = ['bharat', 'rohit', 'nikhil', 'sidhart', 'ajay', 'charan']

name_index = 0

for name_index in range(len(name_list)):
    # 2) Add an if  check inside the loop to only output names longer than 5 characters.
    if len(name_list[name_index]) > 5:
        print('The length of ' +
              name_list[name_index] + ' is ' + str(len(name_list[name_index])))
    # 3) Add another if  check to see whether a name includes a “n”  or “N”  character.
    if 'n' in name_list[name_index] or 'N' in name_list[name_index]:
        print('The name ' + name_list[name_index] + ' has N/n in it')

    name_index += 1
# Use a while  loop to empty the list of names (via pop() )
while len(name_list) != 0:
    name_list.pop()
    print('The updated list is ' + str(name_list))
