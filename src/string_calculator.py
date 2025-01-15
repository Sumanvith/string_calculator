def add(numbers):
    if not numbers:
        return 0
    if numbers.startswith("//"):
        delimiters_section, numbers = numbers[2:].split("\n", 1)
        delimiters = []
        if delimiters_section.startswith("[") and delimiters_section.endswith("]"):
            delimiters = delimiters_section[1:-1].split("][")
        else:
            delimiters = [delimiters_section]
        for delimiter in delimiters:
            numbers = numbers.replace(delimiter, ",")
    numbers = numbers.replace("\n", ",")
    number_list = list(map(int, numbers.split(","))) if numbers else []
    negatives = [n for n in number_list if n < 0]
    if negatives:
        raise ValueError(f"Negatives not allowed: {','.join(map(str, negatives))}")
    number_list = [n for n in number_list if n <= 1000]
    return sum(number_list)