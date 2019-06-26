class Loupan(object):
    def __init__(self,xiaoqu,price,total):
        self.xiaoqu = xiaoqu  # 小区
        self.price = price  # 单价
        self.total = total  # 总价

    def text(self):
        return self.xiaoqu+","+self.price+","+self.total

