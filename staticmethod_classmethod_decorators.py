class Class2:
    def method1(self):
        return "Instance method was called", self

    @classmethod
    def class_method1(cls):
        return "Class method was called", cls

    @staticmethod
    def static_method1():
        return "Static method was called"

# print(Class2.static_method1())
# print(Class2().static_method1())
# object3 = Class2()
# print(object3.static_method1(32))
# print(object3.static_method1())

# object2 = Class2
# object2 = Class2()
# print(object2.class_method1)
# print(object2.class_method1())

# object1 = Class2()
# object1 = Class2
# print(object1.method1())
# print(object1.method1(15))
# print(Class2().method1())
# print(Class2.method1(33))
# print(Class2.method1())
