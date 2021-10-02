name = input("Enter file name:")
fhand = open(name)

counts = {}
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

Bigcount = 0
Bigword = None
for word,count in counts.items():
    if word == None or count > Bigcount:
        Bigword = word
        Bigcount = count

print(Bigword,Bigcount)