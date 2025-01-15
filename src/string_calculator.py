def add(numbers):
    if not numbers:
        return 0
    numbers = numbers.replace("\n", ",")
    number_list = numbers.split(",")
    return sum(map(int, number_list))