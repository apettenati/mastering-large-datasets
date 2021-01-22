from functools import reduce

words = ['zebra', 'fever', 'charm', 'mouse', 'hair', 'brill', 'thorn']

def calculate_letter_points(letter):
    points = {
        'z': 10,
        'f': 5,
        'h': 5,
        'v': 5,
        'w': 5,
        'b': 3,
        'c': 3,
        'm': 3,
        'p': 3,
    }
    return points[letter] if letter in points else 1

def calculate_word_points(word):
    word_points_list = map(calculate_letter_points, word)
    return sum(word_points_list)

all_word_points = list(map(calculate_word_points, words))
print(all_word_points)
gt8_points = filter(lambda x: calculate_word_points(x) > 8, words)
print(list(gt8_points))

new_words = ['these', 'are', 'my', 'words']

total_score = reduce(lambda acc, next: acc + next, map(calculate_word_points, new_words))

print(total_score)