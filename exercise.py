def ordinal(num):
    last_digit = num % 10
    if last_digit in [1, 4, 5, 6, 7, 8, 9, 0]:
        return str(num) + 'th'
    elif last_digit == 2:
        return str(num) + 'nd'
    elif last_digit == 3:
        return str(num) + 'rd'
