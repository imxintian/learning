class Bold(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)


@Bold
def hello(name):
    return 'hello %s' %name


print(hello('xiaoming'))


