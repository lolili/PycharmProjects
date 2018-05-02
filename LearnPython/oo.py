
class Hello:
    def __init__(self,name):
        self.name = name
    def sayHello(self):
        print("Hello Python {0}".format(self.name))

# class Hi(Hello):
#     def __init__(self,name):
#         Hello.__init__(self,name)
#     def sayHi(self):
#         print("Hi Python {0}".format(self.name))

# h = Hello("Jesse")
# h.sayHello()
#
# h1 = Hi("Li")
# h1.sayHi()