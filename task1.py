"""
Task 1:
Дан массив чисел, состоящий из некоторого количества подряд идущих единиц,
за которыми следует какое-то количество подряд идущих нулей: 111111111111111111111111100000000.
Найти индекс первого нуля (то есть найти такое место, где заканчиваются единицы, и начинаются нули)

Какова сложность вашего алгоритма?

def task(array):
  pass

print(task("111111111111111111111111100000000"))
# >> OUT: 24...
"""
"""Algorithm complexity O(n)"""


def task(array):
    for ind in range(len(array)):
        if ind + 1 == len(array):
            return f'OUT: no such index'
        if array[ind] != array[ind + 1]:
            return f'OUT:{ind}'


if __name__ == '__main__':
    print(task("111111111111111111111111100000000"))
    print(task("1111111111111100000"))
    print(task("11111111111111111"))
    print(task("000"))
    print(task("010"))
    print(task([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]))
