class employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.type = 'full time employee'

    def display(self):
        print('employee Type :  ' + self.type + ' name : ' + self.name + ", age : " + str(self.age))