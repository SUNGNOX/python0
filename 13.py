class student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def print_score(self):
        print(self.name,':',self.score)

class child(student):
    def __init__(self, name, score, weight):
        student.__init__(self, name, score)
#        super(child, self).__init__(name, score)
        self.weight = weight
s = child('Tom',99,175)
print(s.name)