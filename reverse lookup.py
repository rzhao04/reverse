def reverseLookup(dictionary, value):
    list = []
    for key in dictionary.keys():
        if value == dictionary[key]:
            list.append(key)
    return list
numList= {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}
value = 1, 2, 3, 4, 5
value = input("value: ")
answer = reverseLookup(numList, value)
print (answer)