class Ligt():
    def __init__(self):
        self.energe=100
    def ligt(self):
        print('the light on')
    def off(self):
        print('off light')
class Iln(Ligt):
    def __init__(self):
        super().__init__()
    def int(self):
        print('the light is conncting with internet')
    def off(self):
        super().off()
        print('the light is off after 5secont')
 
ruun=Iln()
ruun.off()
ruun.ligt()