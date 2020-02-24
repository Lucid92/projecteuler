import math

def is_triangle_number(n):
    # tn = (1/2) * n * (n + 1)
    # 2tn = n^2 + n
    # n^2 + n - 2tn = 0
    # Therefore if (-1 +- sqrt(1 - 4 * (-2tn))) / 2 is an integer, n is a triangular number.

    v1 = (-1 + math.sqrt(1 - 4 * (-2 * n))) / 2

    return v1.is_integer() and v1 > 0

def letter_value(letter):
    return ord(letter) - 64 #ord('A') - 1

def word_value(word):
    val = 0
    for letter in word:
        val += letter_value(letter)

    return val

with open("p042_words.txt", "r") as f:
    words = f.readline().split(",")

    words = [w.replace('"', '') for w in words]

tri_words = []

for word in words:
    if is_triangle_number(word_value(word)):
        tri_words.append(word)

print(len(tri_words))