 # put your code here.
 
fhandle = open("test.txt")
word_count = {}

for line in fhandle:
    line = line.rstrip()
    word_list = line.split(' ')
   
    for word in word_list:
        word_count[word] = word_count.get(word, 0) + 1
        




#       if word in word_count:
#            word_count[word] = word_count[word] + 1
#        else:
#            word_count[word] = 1  

for word, count in word_count.items():
    print "%s %d" % (word, count) 







