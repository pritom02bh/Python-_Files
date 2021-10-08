Text = "Hi People! Welcome to the Club!"

print(len(Text))
print(Text[0])
print(Text[0:2])
print(Text[:-1])
print(Text[:])


# Escape Sequences:

Text2 = "The main \"Idea\" is organize another party"
Text3 = "The main 'Idea' is organize another party\\Dinner"
print(Text2)
print(Text3)


# Formatted Text:

first = "Pritom"
last = "Bhowmik"
full = f"NAME: {first} {last}"
print(full)

# String Method:

title = '  data scientist  '
print(title.upper())
print(title.strip())
print(title.find("scientist"))\

print("Engineer" in title)
print("data" in title) 