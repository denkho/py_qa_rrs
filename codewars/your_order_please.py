def order(sentence):
    return sorted(sentence.split(), key=min)
    # answer = []
    # sentence = sentence.split()
    # for i in range(1, 10):
    #     for word in sentence:
    #         if str(i) in word:
    #             answer.append(word)
    # return ' '.join(answer)

print(order("is2 Thi1s T4est 3a"))