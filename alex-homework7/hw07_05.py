def find_ind_max(tpl):
    max_index = 0
    max_num = tpl[0]
    for i, el in enumerate(tpl):
        if el > max_num:
            max_num, max_index = el, i
    print(f'Максимальное число {max_num} имеет индекс - {max_index}')


test = tuple([float(i) for i in input('Введите строку чисел через запятую - ').split(',')])
find_ind_max(test)
