#Задание 1
first = 'Мама мыла раму'
second = 'Рамена мало было'

print(list(map(lambda x, y: x == y, first, second)))



#Задание 2
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        file = open(file_name, "w", encoding="utf-8")
        for elem in data_set:
            file.write(str(elem))
        file.close()


    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])




#Задание 3
from random import choice

class MysticBall:

    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное')

print(first_ball())
print(first_ball())
print(first_ball())