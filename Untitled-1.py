# PYTHON CODE EXPERIMENTS 1

test_dictionary={"M":9.1,"S":8.8,"J":7.5}
print(test_dictionary.values())
print(test_dictionary)
testlist=[4.5,6.7,2.3]
print(testlist.index(4.5))
print(testlist[1:3])
print(testlist[-1])
print(testlist[-2:])
print(test_dictionary["S"])
print(test_dictionary.keys())

with open ("Desktop\ dogs.txt", "w") as testfile: 
    testfile.write("Bulldog\nShepherd\nShiba")
with open ("Desktop\ dogs.txt", "a+") as testfile:
    testfile.write("\nTerrier\nMalamute")
    testfile.seek(0)
    content=myfile.read()
print(content)
