"""
Task 3:
Мы сохраняем время присутствия каждого пользователя на уроке  виде интервалов. В функцию передается словарь, содержащий три списка с таймстемпами (время в секундах): — lesson – начало и конец урока
— pupil – интервалы присутствия ученика
— tutor – интервалы присутствия учителя
Интервалы устроены следующим образом – это всегда список из четного количества элементов. Под четными индексами (начиная с 0) время входа на урок, под нечетными - время выхода с урока.
Нужно написать функцию, которая получает на вход словарь с интервалами и возвращает время общего присутствия ученика и учителя на уроке (в секундах).
Будет плюсом: Написать WEB API с единственным endpoint’ом для вызова этой функции.

def appearance(intervals):
  pass

print(appearance({
  'lesson': [1594663200, 1594666800],
  'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
  'tutor': [1594663290, 1594663430, 1594663443, 1594666473]
}))
# >> OUT: 31...

"""


def appearance(intervals):
    a = [el for el in intervals['lesson']]
    b = [el for el in intervals['pupil']]
    c = [el for el in intervals['tutor']]

    count = 0
    for ind_B in range(len(b)):
        for ind_C in range(len(c)):
            if ind_B % 2 == 0 and ind_C % 2 == 0:
                while True:
                    if b[ind_B] >= a[0] and c[ind_C] >= a[0]:
                        if b[ind_B + 1] <= a[1] and c[ind_C + 1] <= a[1]:
                            if b[ind_B + 1] >= c[ind_C] and b[ind_B + 1] <= c[ind_C + 1] and b[ind_B] <= c[ind_C]:
                                count += b[ind_B + 1] - c[ind_C]
                                break
                            elif b[ind_B] <= c[ind_C + 1] and b[ind_B + 1] >= c[ind_C + 1]:
                                count += c[ind_C + 1] - b[ind_B + 0]
                                break
                            elif b[ind_B] <= c[ind_C] and b[ind_B + 1] >= c[ind_C + 1]:
                                count += c[ind_C + 1] - c[ind_C + 0]
                                break
                            elif b[ind_B] >= c[ind_C] and b[ind_B + 1] <= c[ind_C + 1]:
                                count += b[ind_B + 1] - b[ind_B]
                                break
                            else:
                                break
                        else:
                            if b[-1] > a[1]:
                                b[-1] = a[1]
                            elif c[-1] > a[1]:
                                c[-1] = a[1]

                    else:
                        if b[0] < a[0]:
                            b[0] = a[0]
                        elif c[0] < a[0]:
                            c[0] = a[0]

    return count


if __name__ == '__main__':
    print(appearance({
        'lesson': [1594663200, 1594666800],
        'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
        'tutor': [1594663290, 1594663430, 1594663443, 1594666473]
    }))
