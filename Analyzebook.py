fp= open("book.txt.", encoding="utf8")
 # print(fp.read())
 # we need to read the book, line by line
character = "Gatsby"
sum = 0
for line in fp:
     # I am on single line inside the iteration
    sum = sum + line.count(character)
print(f"The character {character} shows up {sum} times")
