# Author fuyuan: fuyuan360@qq.com
# Created on 2025/7/17
class Car:
    def __init__(self, make, model, year, **kwargs):
        self.make = make
        self.model = model
        self.year = year
        self.atteributes = kwargs

    def __getattr__(self, item):
        try:
            return self.atteributes[item]
        except KeyError:
            raise AttributeError(f"当前Car实例没有属性 {item}")


benzi = Car("benzi", "benz", 2020, color="red", price=100000)
print(benzi.make)
print(benzi.atteributes["color"])
print(benzi.name)
