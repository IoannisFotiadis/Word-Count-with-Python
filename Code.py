text_file = open("C:\\Users\\Ioannis\\Desktop\\hamlet.txt", mode='r')     # open the file for reading

words_dict = {}
for line in text_file:
    for word in line.lower().split():   # split line into a list of words
        word = word.strip("'?,.;!-/\"")
        if word not in words_dict:
            words_dict[word] = 0
        else:
            words_dict[word] = words_dict[word] + 1

text_file.close()
word_list=sorted(words_dict)
#for word in word_list:
    #print(word, words_dict[word])

for word in sorted(words_dict, key=words_dict.get, reverse=True):
  print(word, words_dict[word])
