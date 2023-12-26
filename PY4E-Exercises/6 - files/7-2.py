# 7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:

# X-DSPAM-Confidence: 0.8475

# Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below.
# Do not use the sum() function or a variable named sum in your solution.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.

## my approach (trying to apply as many concepts as possible)
def extractFloat(str):
    colonPos = str.find(":")
    extractedFloat = str.find(" ", colonPos) #get index of first space after colon
    stringFloat = str[extractedFloat: ]
    return float(stringFloat)

def computeAvg(count, total):
    return total/count

#get file name
fname = input("Enter file name: ")
count = total = 0 #this is a way of assigning multiple variables to one value

#check if file name is valid & open
try:
    fhandle = open(fname)
except:
    print("File cannot be opened:", fname)

for line in fhandle:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue

    line = line.rstrip()
    count += 1
    total += extractFloat(line)

print("Average spam confidence:", computeAvg(count, total))