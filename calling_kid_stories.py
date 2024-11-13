with open('All_Topics.txt', 'r') as file:
    content = file.readlines()

# print(content)

for name in content:
    name = name.rstrip()
    print(name)
    print("-----------")
print(type(content))
