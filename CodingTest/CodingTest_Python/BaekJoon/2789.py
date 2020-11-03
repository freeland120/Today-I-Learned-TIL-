



word = ['C','A','M','B','R','I','D','G','E']

target_word = list(input())

for i in word:
    for j in range(len(target_word)):
        if i == target_word[j]:
            #target_word.remove(i)
            target_word[j] = ""
        else:
            continue

for i in target_word:
    print(i,end="")
