#Візьміть файл, в якому є багато англійських слів у рядках. 
#Порахуйте частоту зустрічі кожного слова та видрукуйте відсортовано.
f = open('text.txt','r')
d = dict()
for line in f:
    for word in line.split():
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
f.close()
mostpopularword = ''
num = 0
for word in d:
    if d[word] > num:
        num = d[word]
        mostpopularword = word
print(f'word "{mostpopularword}" is the most popular ({num} times)')
