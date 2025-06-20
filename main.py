#1
"""
def ascii_avr(text):
    if not text:
        return 0
    return sum(ord(x) for x in text) / len(text)

print(ascii_avr('GxssdQ'))
"""
import random

#2
"""
def filter_ascii(text):
    return "".join(filter(lambda x: 65 <= ord(x) <= 122, text))

print(filter_ascii('kdfha@'))
"""

#3
"""
def highest_ascii(text):
    words = text.replace(".", "").split()
    asciis = [sum(ord(x) for x in word) for word in words]
    return words[asciis.index(max(asciis))]

print(highest_ascii('I go to shop every day. Today is beautiful.'))
"""

#4
"""
def divide_ascii(text):
    evens = list(filter(lambda x: ord(x) % 2 == 0, text))
    odds = list(filter(lambda x: ord(x) % 2 != 0, text))
    return f"evens: {evens}\nodds:{odds}"

print(divide_ascii('lasfhasj'))
"""


#5
"""
def cipher(text, n):
    n = n % 26
    new_t = ""
    for i in text:
        if not i.isalpha():
            new_t += i
        else:
            if ord(i) in range(97, 123):
                a = ord(i) + n
                if a in range(97, 123):
                    new_t += chr(a)
                else:
                    new_t += chr(a - 26)

            if ord(i) in range(65, 91):
                a = ord(i) + n
                if a in range(65, 91):
                    new_t += chr(a)
                else:
                    new_t += chr(a - 26)

    return new_t

print((cipher("aalphaBE", 5)))
"""

#6
"""
def difference_ascii(text):
    return [ord(text[i+1]) - ord(text[i]) for i in range(len(text) -1)]

print(difference_ascii('bjald'))


# def asciis(text):
#     return [ord(i) for i in text]
# print(asciis('bjald'))
"""
#7
"""
import random
def password_name(name, surname):
    name_ascii = [str(ord(i)) for i in name]
    surname_ascii = [str(ord(i)) for i in surname]
    full_name = name_ascii + surname_ascii
    random.shuffle(full_name)
    return "".join(full_name)[:8]
print(password_name("Valijon", 'Karimov'))
"""
