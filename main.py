def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
# 1
print_params(b = 25)
print_params(c = [1,2,3])
# 2
values_list = ['Привет, Genny', 333, [7, 8, 9]]
values_dict = {'a': [7, 8, 9], 'b': 'Привет, Genny', 'c': 333}
print_params(*values_list)
print_params(**values_dict)
# 3
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)