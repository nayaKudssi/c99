usersentence=input("Any sentence:")
print(usersentence)
characterCount=0
wordCount=1
for i in usersentence:
    characterCount=characterCount+1
    if(i==' '):
        wordCount=wordCount+1
print("Number of characters are: ")
print(characterCount)
print("Number of words are:")
print(wordCount)
