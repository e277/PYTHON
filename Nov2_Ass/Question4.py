# 4. Print each line of a file in reverse order. (10 marks)
def partA():
    filename_a = 'quest5.txt'
    print()
    print(*(' '.join(l.split()[::-1]) for l in reversed(list(open(filename_a)))), sep='\n')

# Write a program to compute the number of characters, words, and lines in a file.
def partB():
    filename_b = 'quest5.txt'
    num_charc = 0
    num_words = 0
    num_lines = 0
    num_spaces = 0
    with open(filename_b, 'r') as f:
        for line in f:
            num_lines += 1
            word = 'Y'
            for character in line:
                if (character != ' ' and word == 'Y'):
                    num_words += 1
                    word = 'N'
                elif (character == ' '):
                    num_spaces += 1
                    word = 'Y'
                for i in character:
                    if(i !=" " and i !="\n"):
                        num_charc += 1
    print('\nNumber of characters in text file: ', num_charc)
    print("Number of words in text file: ", num_words)
    print("Number of lines in text file: ", num_lines)


def main():
    partA()
    partB()

if __name__ == "__main__":
    main()