class Mammal:
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex
        self.num_eyes = 2

    def breathe(self):
        print(self.name + "在呼吸...")

    def poop(self):
        print(self.name + "在拉屎...")

#super调用父类方法
class Human(Mammal):
    def __init__(self, name, sex):
        super().__init__(name, sex)
        self.has_tail = False

    def read(self):
        print(self.name + "在阅读...")


class Animal(Mammal):
    def __init__(self, name, sex):
        super().__init__(name, sex)
        self.has_tail = True

    def scratch(self):
        print(self.name + "在进行动物行为...")

