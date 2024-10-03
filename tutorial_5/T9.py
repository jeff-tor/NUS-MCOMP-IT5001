#
# def is_anagram(word_1: str, word_2: str):
#     ## first pass in the 2 words
#     ## then strip off the words
#
#     alphabet_dict = {
#         'A': 1,
#         'B': 2,
#         'C': 3,
#         'D': 4,
#         'E': 5,
#         'F': 6,
#         'G': 7,
#         'H': 8,
#         'I': 9,
#         'J': 10,
#         'K': 11,
#         'N': 12,
#         'O': 13,
#         'P': 14,
#         'Q': 15,
#         'R': 16,
#         'S': 17,
#         'T': 18,
#         'U': 19,
#         'V': 20,
#         'W': 21,
#         'X': 22,
#         'Y': 23,
#         'Z': 24
#     }
#     word_1 = word_1.strip()
#     word_2 = word_2.strip()
#     value = word_calculator(word_1, alphabet_dict)
#     value_2 = word_calculator(word_2, alphabet_dict)
#
# def word_calculator(word, alphabet_dict):
#     counter = 0
#     for i in word:
#         if alphabet_dict[i] in alphabet_dict:
#             counter += 1
#
#     return counter

# print(is_anagram('anagram', 'ana gram'))


# def is_anagram_ver2(word1,word2):
#     d = {}
#     counter1 = 0
#     for i in word1:
#         if d[i] in d:
#         counter1 += 1


# def to_dict(keyL):
#     dictionary = {}
#     for index, value in enumerate(keyL):
#         print(f' {index}, {value}')
#         dictionary[index] = value
#     return dictionary
#
# def to_list(keyL)
#     ls = []
#     for index, value in keyL:
#         ls.append(value)
#     return ls


def phone_pad(string: str):


    ##convert the index,value enumerate(list)
    ##use the dictionary against the string using "if in dict"
    ##
    phone_numpad = {
        ' ': 1,
        'abc': 2,
        'def': 3,
        'ghi': 3,
        'jkl': 3,
        'mno': 3,
        'pqrs': 3,
        'tuv': 3,
        'wyxz': 3 }

    phone_numpad = {

    }

    for i in string:
        if i in phone_numpad.keys():
            print(i)

    return



print(phone_pad('i luv u'))
# print(to_dict([1,2,3,4,5]))
