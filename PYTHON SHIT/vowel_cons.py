
word = input("Enter a word: ").lower();


vowel_count = 0
consonant_count = 0

for letter in word:
	if (letter =="a" or letter =="e" or letter =="i" or letter =="o" or letter =="u" ):
		vowel_count +=1
	else:
		consonant_count += 1

print("vowel are", vowel_count)
print("consonant are", consonant_count)
