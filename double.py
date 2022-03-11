def doubler(func):
    def d():
        func()
        func()
    return d


@doubler
def final():
    print("Hello World")


final()
