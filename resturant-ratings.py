# Initial setup
ratings_file = open("scores.txt")
ratings_dict = {}


# Loop through text file to load dictionary
for line in ratings_file:
    line = line.rstrip()
    word_list = line.split(':')
    ratings_dict[word_list[0]] = word_list[1]

# Sort and print dictionary
sorted_rest = sorted(ratings_dict.keys())

for resturant in sorted_rest:
    print "%s is rated at : %s" % (resturant, ratings_dict[resturant])