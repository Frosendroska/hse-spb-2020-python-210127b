



def solve(instr):
    # answer = ''
    dic_of_answers = {}
    string = instr.split('\n')  # лист строчек
    for s in string[2:-2]:  # s - строчка
        part_of_string = s.split('|')  # лист из двух частей
        key = part_of_string[2]
        key = key.replace(' ', '')
        if key not in dic_of_answers:
            dic_of_answers.update({key: []})  # словарь с ключем в виде ip

    return ', '.join(dic_of_answers.keys())
    # if string.find("Решение"):


"""
196.42.36.56 - Решение №1
54.133.59.123 - Решение №1, Решение №2
8.8.8.8 - 
1.1.1.1 - 
196.42.36.65 - 
196.3.5.44 - 
44.11.23.9 - Решение №2
"""
print(solve("""
+-------------+---------------+
| Решение №1: | 196.42.36.56  |
|             | 54.133.59.123 |
| :           | 8.8.8.8       |
|             | 1.1.1.1       |
|             | 196.42.36.65  |
|             | 196.3.5.44    |
| Решение №2: | 44.11.23.9    |
|             | 54.133.59.123 |
+------------+----------------+
"""))
