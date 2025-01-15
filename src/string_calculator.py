def add(numbers):
    if not numbers:
        return 0
    if numbers.startswith("//"):
        delimiter, numbers = numbers[2:].split("\n", 1)
        numbers = numbers.replace(delimiter, ",")
    numbers = numbers.replace("\n", ",")
    number_list = list(map(int, numbers.split(",")))
    negatives = [n for n in number_list if n < 0]
    if negatives:
        raise ValueError(f"Negatives not allowed: {','.join(map(str, negatives))}")
    return sum(number_list)
