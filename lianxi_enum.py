from enum import Enum, unique
M = Enum('M',('A','B','C'))
print(M(1))
print(M.A.name)
print(M.A.value)
print(M.__members__.keys())
print(dir(M.__members__))
print(M.__members__.items())
for name, member in M.__members__.items():
    print(name,'=>',member,': ',member.value)


#自定义值
@unique
class Alpha(Enum):
    A=0
    B=1
    C=2

print(Alpha.__members__.items())
#
print(Alpha(1))
