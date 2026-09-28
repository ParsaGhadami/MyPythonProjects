print("=========================")
print("=     TEXT ANALYZER     =")
print("=========================")


sentences = input("Please Enter Your Sentence : ")
charecters_count = len(sentences)
print(f"Charecter Numbers: {charecters_count}")
clean_sentences = sentences.lower().replace("!" , " ")
words_list = clean_sentences.split()
words_count = len(words_list)
print(f"Words Number: {words_count}")
unique_words_count = len(set(words_list))
print(f"Unique Words: {unique_words_count}")
longest_word = ""
for word in words_list:
    if len(word) > len(longest_word):
        longest_word = word
print(f"Longest Word is {longest_word}")
most_common_words = ""
max_count = 0
for word in words_list:
    count = words_list.count(word)
    if count > max_count:
        max_count = count
        most_common_words = word
print(f"Most Common Word: {most_common_words}")