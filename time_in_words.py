def time_in_words(h, m):

    numbers = {
        0: 'zero',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'quarter',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
        20: 'twenty',
        21: 'twenty one',
        22: 'twenty two',
        23: 'twenty three',
        24: 'twenty four',
        25: 'twenty five',
        26: 'twenty six',
        27: 'twenty seven',
        28: 'twenty eight',
        29: 'twenty nine',
        30: 'half'
    }

    if m > 60:
        return 'minutes cannot be more than 60'
    if h > 12:
        return 'hours must be in 12 hour format'

    # past the hour
    if m == 0:
        return f'{numbers[h]} o\' clock'
    elif m == 60 and h == 12:
        return f'{numbers[h - 11]} o\' clock'
    elif m == 60 and h != 12:
        return f'{numbers[h + 1]} o\' clock'
    elif m < 30 and m != 15 and m == 1:
        return f'{numbers[m]} minute past {numbers[h]}'
    elif m < 30 and m != 15 and m != 1:
        return f'{numbers[m]} minutes past {numbers[h]}'
    elif m < 30 and m == 15:
        return f'{numbers[m]} past {numbers[h]}'
    elif m == 30:
        return f'{numbers[m]} past {numbers[h]}'

    # to the hour
    elif m > 30 and m != 45 and m != 59:
        return f'{numbers[60 - m]} minutes to {numbers[h + 1]}'
    elif m > 30 and m == 45:
        return f'{numbers[60 - m]} to {numbers[h + 1]}'
    elif m == 59:
        return f'{numbers[60 - m]} minute to {numbers[h + 1]}'


if __name__ == '__main__':
    res = time_in_words(5, 32)
    print(res)
