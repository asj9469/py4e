# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

# Desired Output: cwen@iupui.edu 5

fileName = input("Enter File Name: ")
if len(fileName) < 1:
    name = "mbox-short.txt"
fh = open(fileName)
emailCount = dict()

# count all the emails
for line in fh:
    if line.startswith("From "):
        words = line.split()
        emailCount[words[1]] = emailCount.get(words[1], 0) + 1

# loop to iterate through and find the max count of email
max = 0
mostFrequent = ""
for email, count in emailCount.items():
    if max < count:
        max = count
        mostFrequent = email

print(mostFrequent, max)