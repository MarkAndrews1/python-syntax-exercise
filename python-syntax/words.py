def print_upper_words(words):
    """It should print each word on a separate line uppercased"""
    for word in words:
        print(word.upper())

def print_upper_only_e(words):
    '''It should print each word on a separate line uppercased that starts with e'''
    for word in words:
        if word.startswith('e') or word.startswith('E'):
            print(word.upper())

def print_upper_words_general(words, start_letter):
    '''It should print each word on a separate line uppercased that starts with what the user is passing in'''
    for word in words:
        for letter in start_letter:
            if word.startswith(letter):
                print(word.upper())
                break