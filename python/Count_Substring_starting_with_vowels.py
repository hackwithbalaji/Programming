# To count number of Substring starting with vowels or consonants or any letter

s = input("Enter String : ")
vowel = "AEIOUaeiou"  # instead of vowel,required letter can be given!
count = 0
for i in range(len(s)):
    if s[i] in vowel:
        count += len(s)-i
print(count)
