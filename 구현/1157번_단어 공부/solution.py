words = input()
words = words.upper()
words_set = list(set(words))


words_count = []
for x in words_set:
    cnt = words.count(x)
    words_count.append(cnt)


if words_count.count(max(words_count)) > 1:
    print("?")
else:
    max_index = words_count.index(max(words_count))
    print(words_set[max_index])
