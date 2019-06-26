class A(object):
    @classmethod
    def foo(self):
        print("hello",self)


if __name__ == '__main__':

    A.foo()
