 # put your code here.
 
fhandle = open("test.txt")
word_count = {}

for line in fhandle:
    line = line.rstrip()
    word_list = line.split(' ')
   
    for word in word_list:
        if word in word_count:
            word_count[word] = word_count[word] + 1
        else:
            word_count[word] = 1  

for word in word_count:
    count = word_count[word]
    print "%s %d" % (word, count) 






