# import pickle
# list = ["ming","yue","a"]
# listb =pickle.dumps(list)
# # print listb
#
# listc = pickle.loads(listb)
# # print listc
#
# f1 = file('1.pk1','wb')
# pickle.dump(list,f1,True)
# f1.close()
#
# f2 = file('1.pk1','rb')
# t = pickle.load(f2)
# print t
# f2.close()
#
# a=range(1,5,2)
# print a

class Human(object):
    def run(self):
        print 'Human is running...'

class Student(Human):
    def __init__(self, name = 'Mr.A', score = 100):
        self.__name = name
        self.__score = score
    def print_score(self):
        print '%s: %s, %s' % (self.__name, self.__score, self.__scor)
    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >=60:
            return 'B'
        else:
            return 'C'
    def run(self):
        print 'Student is running...'

class Teacher(Human):
    def run(self):
        print 'Teacher is running...'
def run(human):
    human.run()

s = Student('je', 80)
print s.get_grade()
#print s.__score
s._Student__scor=1
s.print_score()

run(Student())