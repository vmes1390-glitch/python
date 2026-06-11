def alpha(word):
    count=0
    for i in word:
        count +=1

    return count

w=input("Enter a word: ")

print(alpha(w))