def log_decorator(func):
    def wrapper():
        print("Début de ma fonction wrapper")
        func()
        print("Fin de ma fonction wrapper")
    return wrapper


@log_decorator
def function_test():
    print("Cette fonction ne prend pas d'arguments.")


function_test()
