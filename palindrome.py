a = input("Enter a String:") 
rev=""
for char in a:
rev=char+rev
print(rev)
if a==rev:
print("Palindrome")
else:
print("Not a Palindrome")
