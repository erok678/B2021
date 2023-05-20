import random
class Student:
    def  __init__(self,name):
        self.name=name
        self.gladness=50
        self.progress=0
        self.alive=True
        self.stipuha=0
        self.zarplata=0
    def to_study(self):
        print('Час навчатись!')
        self.progress+=0.12
        self.gladness-=3
        self.stipuha += 100
    def to_chill(self):
        print('Час відпочити!')
        self.progress +=0.1
        self.gladness -=5
    def to_sleep(self):
        print('Час спати!')
        self.gladness += 3
    def is_alive(self):
        if self.progress<-0.5:
            print("Відрахували")
            self.alive=False
        elif self.gladness<0:
            print("Дипресія...")
            self.alive = False
        elif self.progress>5:
            print("Закінчив екстерном")
            self.alive=False
    def end_of_day(self):
        print(f"Gladness -{self.gladness}")
        print(f"Stipuha -{self.stipuha}")
        print(f"Zarplata -{self.zarplata}")
        print(f"Progress - {round(self.progress,2)}")
    def live(self,day):
        day="Day"+ str(day) + "of "+ self.name + "life"
        print(f"{day:=^50}")
        live_cub = random.randint(1, 3)
        if live_cub==1:
            self.to_study()
        elif live_cub==2:
            self.to_sleep()
        elif live_cub==3:
            self.to_chill()
        self.end_of_day()
        self.is_alive()

nick = Student(name="Nick")
for day in range(365):
    if nick.alive == False:
        break
    nick.live(day)
