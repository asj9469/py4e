
commands = [
    "goto A",
    "create fileA",
    "create fileB",
    "goto B",
    "create fileA",
    "create fileB",
    "create fileC",
    "goto A",
    "create fileA",
    "create fileB",
    "goto B",
    "create fileB",
    "create fileD",
    "create fileC",
]

currDir = ""
entireDir = [] # [[directory, set()]]
newFile = ""

for c in commands:
    if c.startswith("goto"):
        currDir = c[5:]
        if not currDir in entireDir:
            entireDir.append([currDir, set()])
    else:
        newFile = c[8:]
        for i in range(len(entireDir)):
            if entireDir[i][0] == currDir:
                entireDir[i][1].add(newFile)

most = 0
name = ""
for i in range(len(entireDir)):
    if most < len(entireDir[i][1]):
        name = entireDir[i][0]

print(name)