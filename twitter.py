name = "twitter"
result = name

vowels = ('a', 'i', 'u', 'e', 'o')

for x in name.lower():
    if x in vowels:
        result = result.replace(x,"")
        
print("twitter after removed vowels it becomes :", result)