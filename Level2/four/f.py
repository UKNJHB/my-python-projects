class Human():
    def __init__(self):
        self.energe=100

    def walk(self):
        print('i am now walking')
class Athlete(Human):
    def __init__(self):
        super().__init__()
    def run(self):
        print("i'm now running fast")
    def walk(self):
        super().walk()
        print("i'm walk very fast. i am faster than a bullet")
runner=Athlete()
runner.run()
runner.walk()