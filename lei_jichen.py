class student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def print_score(self):
        print('student', self.name,':',self.score)

class child(student):
    def __init__(self, name, score, weight):
#        student.__init__(self, name, score)
        super(child, self).__init__(name, score)
        self.weight = weight
    def set_weight(self, value):
        if value<0 or value>100:
            raise ValueError('out of range!!')
    def print_score(self):
        print('child', self.name,':',self.score)
    def __str__(self):
        return 'test __str__ wei dui xiang!'

s = child('Tom',99,175)
print(s)
print(s.set_weight(99))
print(dir(s))

child.weight=200
print(child.weight)

print(getattr(s, 'name'))
super(child, s).print_score()
