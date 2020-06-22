# recursive functions


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def cumulative_sum(n):
    if n == 0:
        return 0
    else:
        return n + cumulative_sum(n - 1)


def reverse_list(my_list, start_index, end_index):
    if start_index >= end_index:
        return
    else:
        pass  # swap elements at start_index and end_index
        reverse_list(my_list, start_index + 1, end_index - 1)


number = int(input('Enter number: '))

print('Factorial of %d' % factorial(number))
print('Cumulative sum of %d' % cumulative_sum(number))
