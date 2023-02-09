# Задание 1
# Создать класс TrafficLight (светофор).
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд,
# второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.


from time import sleep


class TrafficLight:
    __color = {'красный': 7, 'желтый': 2, 'зеленый': 5}

    @staticmethod
    def running():
        for key, value in TrafficLight.__color.items():
            print(f'Светофор {key}')
            sleep(value)


TL = TrafficLight()
TL.running()

