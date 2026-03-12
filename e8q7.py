def count_vowel(str):
    vow = 0
    vowels="AEIOUaeiou"
    for s in str:
        if s in vowels:
            vow = vow+1
        return vow
str = input("enter the strng :")
count = count_vowel(str)
print(f"the no of vowels in string are : {count}")