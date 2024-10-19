from abc import ABC, abstractmethod


class Engine(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Vehicle(ABC):
    def __init__(self, implementation: Engine):
        self.implementation = implementation

    @abstractmethod
    def drive(self):
        pass

class Car(Vehicle):
    def drive(self):
        print('Вы сели за руль автомобиля.')
        key = input('В какую сторону прокрутить ключ, вправо или влево?: ')
        if 'вправо' in key or 'Вправо' in key or 'право' in key or 'Право' in key:
            return self.implementation.start()
        elif 'влево' in key or 'Влево' in key or 'лево' in key or 'Лево' in key:
            return self.implementation.stop()
        else:
            print('У вас не вышло. Попробуйте ещё раз.')

class Bike(Vehicle):
    def drive(self):
        print('Вы выкатили велосипед из гаража.')
        selector = input('Вы хотите включить или выключить переключатель на руле вашего велосипеда?: ')
        if 'вкл' in selector or 'Вкл' in selector or 'включить' in selector or 'Включить' in selector:
            return self.implementation.start()
        elif 'выкл' in selector or 'Выкл' in selector or 'выключить' in selector or 'Выключить' in selector:
            return self.implementation.stop()
        else:
            print('У вас не вышло. Попробуйте ещё раз.')

class GasolineEngine(Engine):
    def start(self):
        print('Двигатель внутреннего сгорания заведён.')

    def stop(self):
        print('Двигатель внутреннего сгорания заглушён')

class ElectricEngine(Engine):
    def start(self):
        print('Электрический двигатель включён.')

    def stop(self):
        print('Электрический двигатель выключен.')

class HybridEngine(Engine):
    def start(self):
        print('Гибридный двигатель включён.')

    def stop(self):
        print('Гибридный двигатель выключен.')

def user_usage(abstraction: Vehicle):
    abstraction.drive()


engine1 = ElectricEngine()
vehicle1 = Car(engine1)
user_usage(vehicle1)

engine2 = GasolineEngine()
vehicle2 = Bike(engine2)
user_usage(vehicle2)
