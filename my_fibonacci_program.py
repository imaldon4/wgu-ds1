# my fibonacci program


def fibonacci(index):
    if index == 0:
        return 0
    elif index == 1:
        return 1
    else:
        return fibonacci(index - 1) + fibonacci(index - 2)


num = int(input('Enter a number:')) # Max number is ~35
print(fibonacci(num))
