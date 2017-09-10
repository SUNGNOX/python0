import modual_
from class_ import Student
modual_.par_num()


one = Student('Bob', '78')
one.print_score()
print(one._Student__name)
print(one.SiB)
print(len(one))
print(getattr(one, 'score'))
setattr(one, 'SiB', 18)
print(one.SiB)

one.SiB = 10
print(one.SiB) #实例属性
print(Student.SiB) #类属性


def prove_score(self, age):
    self.age = age
    print('done')
print(one.score)
from types import MethodType
one.prove_score = MethodType(prove_score, one)
one.prove_score(25)
print(one.age)