with open("smallinput.txt") as f:
    data = f.readlines()
available = list(map(lambda x: x if x=='x' else int(x), data[1].strip().split(',')))
idmap = {key:val for val, key in filter(lambda x: x[1]!='x', enumerate(available))}
idlist = [id for id in idmap]

print(available)
print(idmap)
print(idlist)