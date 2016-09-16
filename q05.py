def ngram(n, s):
    char = [s[i:i+n] for i in range(0, len(s), n)]
    word = list()
    for w in s.split(" "):
        word.append(w[:2])

    print(char)
    print(word)

if __name__ == '__main__':
    ngram(2, "I am an NLPer")
