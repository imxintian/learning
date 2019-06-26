
# 9-1 餐馆:创建一个名为 Restaurant 的类，
# 其方法__init__()设置两个属性: restaurant_name 和 cuisine_type。
# 创建一个名为 describe_restaurant()的方法和一个 名为 open_restaurant()的方法，其中前者打印前述两项信息，
# 而后者打印一条消息， 指出餐馆正在营业。
# 根据这个类创建一个名为 restaurant 的实例，分别打印其两个属性，再调用前述 两个方法。
# 9-2 三家餐馆:根据你为完成练习 9-1 而编写的类创建三个实例，并对每个实例调 用方法 describe_restaurant()。
# 9-4 就餐人数:在为完成练习 9-1 而编写的程序中，添加一个名为 number_served 的属性，并将其默认值设置为 0。
# 根据这个类创建一个名为 restaurant 的实例;打印有 多少人在这家餐馆就餐过，然后修改这个值并再次打印它。
# 添加一个名为 set_number_served()的方法，它让你能够设置就餐人数。调用这个 方法并向它传递一个值，然后再次打印这个值

# 9-6 冰淇淋小店:冰淇淋小店是一种特殊的餐馆。编写一个名为 IceCreamStand 的 类，
# 让它继承你为完成练习 9-1 或练习 9-4 而编写的 Restaurant 类。
# 这两个版本的 Restaurant 类都可以，挑选你更喜欢的那个即可。
# 添加一个名为 flavors 的属性，用于 存储一个由各种口味的冰淇淋组成的列表。
# 编写一个显示这些冰淇淋的方法。创建一个 IceCreamStand 实例，并调用这个方法。


class Restaurant(object):
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(str(self.restaurant)+'是一个'+str(self.cuisine_type)+'餐厅')

    def set_number_served(self, number_served):
        self.number_served = number_served

    def open_restaurant(self):
        print(self.restaurant+'正在营业！'+'现在有'+str(self.number_served)+'人正在就餐')


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def open_restaurant(self):
        print(self.restaurant+'正在营业！'+'现在有'+str(self.number_served)+'人正在就餐'+'正在吃'+str(self.flavors))


multi_function_restaurant = Restaurant('a', '多功能')
multi_function_restaurant.number_served = 10
multi_function_restaurant.describe_restaurant()
multi_function_restaurant.open_restaurant()

western_restaurant = Restaurant('b', '西式餐厅')
western_restaurant.describe_restaurant()
western_restaurant.set_number_served(12)
western_restaurant.open_restaurant()

chinese_restaurant = Restaurant('c', '中式餐厅')
chinese_restaurant.describe_restaurant()
chinese_restaurant.open_restaurant()

ice_cream_stand = IceCreamStand('d', '冰淇淋小店', '芒果冰淇淋')
ice_cream_stand.describe_restaurant()
ice_cream_stand.set_number_served(12)
ice_cream_stand.open_restaurant()



