#q2

def remove(phrase, word):
    newword = word.replace(phrase, "")
    return newword

print(remove("ABCDEFG", "EFG"))

#q8
def reverse(word):
    newword = ""
    for i in range(len(word)):
        newword += word[len(word)-i-1]
    return newword



def mirror(word):
    return word + reverse(word)


print(mirror("dog"))