'''
__init__ 메서드는 setdata 메서드와 이름만 다르고 모든 게 동일하다. 
단 메서드 이름을 __init__으로 했기 때문에 
생성자로 인식되어 객체가 생성되는 시점에 자동으로 호출되는 차이가 있다.
'''

class Wizard:
    def __init__(self, health, mana, armor):
        self.health = health
        self.mana = mana 
        self.armor = armor

    def attack(self):
        print("파이어볼")

x = Wizard(health = 545, mana = 210, armor = 10)
print(x.health, x.mana, x.armor)
x.attack()
