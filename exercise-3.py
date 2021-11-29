def func_1 (list_in):
    list_out = ["Element", "start"]
    for i in list_in:
        list_out.append(i)
    list_out.append("finish")
    return list_out
print(func_1(['hello', 5, 'John', ]))

def func_2 (*args):
    list_out = []
    counter = 1
    for i in args:
        list_out.append({i:counter})
        counter += 1
    return list_out
print(func_2('x', 5, 'John'))

def func_3 (input):
    list_odd = []
    list_even = []
    list_temp = []
    for i in input:
        list_temp.append(i)
    for i in list_temp:
        if i % 2 == 0:
            list_even.append(i)
        else:
            list_odd.append(i)
    return list_odd, list_even
a, b = func_3((1,2,3,4,5))
print(a) #[2, 4]
print(b) #[1, 4, 9, 16, 25]