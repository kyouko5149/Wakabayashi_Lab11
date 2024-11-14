list_names = []
length_word = []
num = 1

for i in range(10):
    example = input(f"Enter a word {num}: ")
    list_names.append(example)
    num += 1
    
length = int(input("Enter a number/length: "))

for example in list_names:
    if len(example) >= length:
        length_word.append(example)
    else:
        continue
print(f"These are the words you have entered that have {length} letters: {length_word}")