#类装饰器
def Dec(Class):
    class Zsq:
        def __init__(self, fish, water):
            self.Raw = Class(fish)
            self.water = water
        def show(self):
            self.Raw.show()
            print(self.water)
    return Zsq


@Dec
class River:
    def __init__(self, fish):
        self.__fish = fish
    def show(self):
        print(self.__fish)

if __name__=='__main__':
    c = River('yu', 'shui')
    c.show()
