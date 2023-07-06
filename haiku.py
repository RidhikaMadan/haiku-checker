import re
from pysyllables import get_syllable_count

line1 = input("Enter the first line of your poem: ")
line2 = input("Enter the second line of your poem: ")
line3 = input("Enter the third line of your poem: ")

def count_syllables_in_line(line):
    words = re.sub(r'[^\w\s]', '', line).split()
    count = 0
    for word in words:
        word_syllable_count = get_syllable_count(word)
        if word_syllable_count != None:
            count += word_syllable_count
    return count

line1count = count_syllables_in_line(line1)
line2count = count_syllables_in_line(line2)
line3count = count_syllables_in_line(line3)

def check_five(line):
    syllables = count_syllables_in_line(line)
    if syllables == 5:
        return True
    else:
        return False

def check_seven(line):
    syllables = count_syllables_in_line(line)
    if syllables == 7:
        return True
    else:
        return False


def haiku_checker():
    line1_check = check_five(line1)
    line2_check = check_seven(line2)
    line3_check = check_five(line3)

    if line1_check and line2_check and line3_check:
        print("HAIKU! You have 5-7-5 syllables.")
    else:
        print("UH-OH! Not a haiku.")
        if not line1_check:
            print("Line 1 has " + str(line1count) + " instead of 5 syllables.")
        if not line2_check:
            print("Line 2 has " + str(line2count) + " instead of 7 syllables.")
        if not line3_check:
            print("Line 3 has " + str(line3count) + " instead of 5 syllables.")

haiku_checker()
