task = 'Самостоятельная работа по уроку "Распаковка позиционных параметров", Домашнее задание по уроку "Распаковка позиционных параметров"'
avtor = 'Студент Крылов Эдуард Васильевич'
thanks = 'Благодарю за внимание :-)'
print()
print(task)
print(avtor)
print()


def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


volue_list = [5.45, 'Hello', 6]
values_dict = {'a': 'Ed', 'b': 45, 'c': False}
values_list_2 = [54.32, 'Строка' ]

print_params()
print_params(b = 25)
print_params(c = [1,2,3])
print_params(*volue_list)
print_params(**values_dict)
print_params(*values_list_2, 42)
print()
print(thanks)