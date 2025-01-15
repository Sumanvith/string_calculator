def add(numbers):
    if not numbers:
        return 0
    number_list = numbers.split(",")
    return sum(map(int, number_list))
