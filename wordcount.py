
def word_counting (filename):
    file_to_open = open(filename)
    
    words_count = {}
    for line in file_to_open:
        test_file = line.rstrip().split(" ")

        for word in test_file:
            words_count[word] = words_count.get(word, 0) + 1

    print words_count



word_counting("test.txt")

