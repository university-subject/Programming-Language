a_integer = 1
a_string_1 = 'string'
a_string_2 = "string"
a_float = 0.5

a_string_str: str = "string"
a_integer_int: int = 0
a_float_float: float = 0.5

a, b, c = 1, 0.5, "string"

# 元組 tuple
a_tuple = (1, 2, 3)
# 列表 list
a_list = [1, 2, 3]
# 字典 dict
a_dict = {
    'key':'value',
    1 : 0.5
}

print("hello world");print("I love python")

print((lambda x, y: x * y)(3, 3))

def hello():
    print("hello world!")
    while 1:
        if 1 == 1:
            print("1 == 1")
        else:
            print("1 != 1??")

class Object:
    def __init__(self, object=None) -> None:
        if object!=None:
            self = object
        else:
            self.value = 0
    def print_my_value(self):
        print(self.value)

object = Object()
object.print_my_value()
