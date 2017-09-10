class Student(object):
    def __init__(self,name,score):
        self.__name = name
        self.score = score

    SiB = 56

    def __len__(self):
        return 100

    def print_score(self):
        print('%s:%s' % (self.__name, self.score) )
