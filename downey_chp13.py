# @author: Kristin Dahl
# January 3, 2021
# Think Python, 2nd ed., Chapter 513

import string

word_dict = {}
total_words = 0


def cleanup(word):
    word = word.translate(str.maketrans("", "", string.punctuation))
    word = word.translate(str.maketrans("", "", string.whitespace))
    word = word.lower()

    global word_dict
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1

    return word


def file_convert(in_file):
    result_list = []
    header = True
    global word_dict
    global total_words

    with open(in_file, encoding="utf-8") as reader:
        for line in reader:
            if header:
                if "*** START OF THIS PROJECT GUTENBERG EBOOK" in line:
                    header = False
            else:
                words = line.split()
                total_words += len(words)
                #print(words)
                result_list.append(list(map(cleanup, words)))
                map(cleanup, result_list)

    print("Total number of words: " + str(total_words))

    sort_orders = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)

    for i in range(0,19, 1):
        item = sort_orders[i]
        print(item[0], item[1])

    return result_list


in_file = "C:\\Users\\dahl0\\Repos\\Exercises\\wonderland.txt"
print("File is: " + in_file)

file_convert(in_file)
