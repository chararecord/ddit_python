class Xi:
    def __init__(self):
        self.index_look = 10
    
    def corona(self):
        self.index_look -= 1
    
class Trump:
    def __init__(self):
        self.money = 2
    
    def youfire(self):
        self.money += 1

class Kim:
    def __init__(self):
        self.nuclear = 20
    
    def aoji(self):
        self.nuclear += 2

class ParkInSoo(Xi,Trump, Kim):
    def __init__(self):
        Xi.__init__(self)
        Trump.__init__(self)
        Kim.__init__(self)
        
if __name__ == '__main__':
    insoo = ParkInSoo()
    
    print("index_look",insoo.index_look)
    print("money",insoo.money)
    print("nuclear",insoo.nuclear)
    print("~~~~~~~~corona ~ youfire ~ aoji~~~~~~~~")
    
    insoo.corona()
    insoo.youfire()
    insoo.aoji()
    
    print("index_look",insoo.index_look)
    print("money",insoo.money)
    print("nuclear",insoo.nuclear)
