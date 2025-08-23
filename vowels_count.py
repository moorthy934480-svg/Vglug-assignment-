vowels = "aeiouAEIOU"
vcount = 0
ccount = 0
a = input("Enter a string: ")
for char in a:
if char.isalpha(): # only check
  if char in vowels:
    vcount += 1
 else:
ccount += 1
print("Vowels:", vcount)
print("Consonants:", ccount)
