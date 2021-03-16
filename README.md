##Решение тестовых заданий для устройства на работу.
###Решия в файлах и папках с соответствующими названиями.
Задания:
============================ 
Task 1:
Дан массив чисел, состоящий из некоторого количества подряд идущих единиц, за которыми следует какое-то количество подряд идущих нулей: 111111111111111111111111100000000. 
Найти индекс первого нуля (то есть найти такое место, где заканчиваются единицы, и начинаются нули)

Какова сложность вашего алгоритма?

`def task(array): 
  pass 

print(task("111111111111111111111111100000000")) 
>> OUT: 25... `
============================ 
Task 2:
В нашей школе мы не можем разглашать персональные данные пользователей, но чтобы преподаватель и ученик смогли объяснить нашей поддержке, кого они имеют в виду (у преподавателей, например, часто учится несколько Саш), мы генерируем пользователям уникальные и легко произносимые имена. Имя у нас состоит из прилагательного, имени животного и двузначной цифры. В итоге получается, например, "Перламутровый лосось 77". Для генерации таких имен мы и решали следующую задачу:
Получить с русской википедии список всех животных (Категория:Животные по алфавиту) и вывести количество животных на каждую букву алфавита. Результат должен получиться в следующем виде:
 А: 642
Б: 412
В:....

============================ 
Task 3:
Мы сохраняем время присутствия каждого пользователя на уроке  виде интервалов. В функцию передается словарь, содержащий три списка с таймстемпами (время в секундах): — lesson – начало и конец урока 
— pupil – интервалы присутствия ученика 
— tutor – интервалы присутствия учителя 
Интервалы устроены следующим образом – это всегда список из четного количества элементов. Под четными индексами (начиная с 0) время входа на урок, под нечетными - время выхода с урока.
Нужно написать функцию, которая получает на вход словарь с интервалами и возвращает время общего присутствия ученика и учителя на уроке (в секундах). 
Будет плюсом: Написать WEB API с единственным endpoint’ом для вызова этой функции.

`def appearance(intervals): 
  pass 

`print(appearance({ 
  'lesson': [1594663200, 1594666800], 
  'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472], 
  'tutor': [1594663290, 1594663430, 1594663443, 1594666473] 
})) 
 >> OUT: 31... `
