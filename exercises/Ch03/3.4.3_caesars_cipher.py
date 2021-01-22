from toolz import compose, pipe

def letter_to_int(letter):
    return ord(letter)

def add_3(int):
    return int + 3

def sub_3(int):
    return int - 3

def int_to_letter(int):
    return chr(int)

def cipher_letter(letter):
    return pipe(letter, letter_to_int, add_3, int_to_letter)

def cipher_word(word):
    return ''.join(list(map(cipher_letter, word)))

def cipher_phrase(phrase):
    word_list = phrase.split(' ')
    ciphered_phrase = map(cipher_word, word_list)
    return ' '.join(list(ciphered_phrase))

def decipher_phrase(phrase):
    word_list = phrase.split(' ')
    deciphered_phrase = []
    for word in word_list:
        decipher_word = compose(int_to_letter, sub_3, letter_to_int)
        deciphered_word = map(decipher_word, word)
        deciphered_phrase.append(''.join(list(deciphered_word)))
    return ' '.join(list(deciphered_phrase))

phrase = 'this is my sentence'
ciphered_phrase = cipher_phrase(phrase)
print(ciphered_phrase)
deciphered_phrase = decipher_phrase(ciphered_phrase)
print(deciphered_phrase)
