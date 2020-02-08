word_map = {
    1 : "one",
    2 : "two",
    3 : "three",
    4 : "four",
    5 : "five",
    6 : "six",
    7 : "seven",
    8 : "eight",
    9 : "nine",
    10 : "ten",
    11 : "eleven",
    12 : "twelve",
    13 : "thirteen",
    14 : "fourteen",
    15 : "fifteen",
    16 : "sixteen",
    17 : "seventeen",
    18 : "eighteen",
    19 : "nineteen",
    20 : "twenty",
    30 : "thirty",
    40 : "forty",
    50 : "fifty",
    60 : "sixty",
    70 : "seventy",
    80 : "eighty",
    90 : "ninety"
}

def num_to_word(num):
    if (num < 20):
        return word_map[num]
    
    if (20 <= num < 100):
        tens = num // 10 * 10
        ones = num % 10

        return f'{word_map[tens]} {word_map[ones]}' if ones != 0 else word_map[tens]

    if (100 <= num < 1000):
        hundreds = num // 100
        remainder = num % 100

        return f'{word_map[hundreds]} hundred and {num_to_word(remainder)}' if remainder != 0 else f'{word_map[hundreds]} hundred'

    return "one thousand"


letter_count = 0
for i in range(1, 1001):
    letter_count += len(num_to_word(i).replace(' ', ''))

print(letter_count)