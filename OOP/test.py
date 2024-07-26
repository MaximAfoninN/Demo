def my_dicarator(func):
    def wrapper():
        print("Begin")
        func()
        print("end")
    return wrapper


@my_dicarator
def say_hello():
    print("Hello")

say_hello()