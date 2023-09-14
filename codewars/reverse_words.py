def reverse_words(text):
    if len(text.split()) == 1:
        return text[::-1]
    space = text.count(' ') // (len(text.split()) - 1)
    s = ' ' * space
    return s.join([x[::-1] for x in text.split()])

print(reverse_words('The quick brown fox jumps over the lazy dog.'))
print(reverse_words('double  spaced  words'))
print(reverse_words('apple'))