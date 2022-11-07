# Дескрипторы - 

class Worker:
    def __init__(self, name, surname, hours, rate):
        self.name = name
        self.surname = surname
        self.hours = hours
        self.rate = rate

    def total_pofit(self):
        #Рассчет зарплаты
        return self.hours * self.rate

OBJ = Worker("")

# Геттеры и сеттеры 

