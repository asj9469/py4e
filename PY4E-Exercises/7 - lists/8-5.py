# 8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message).
# Then print out a count at the end.
# Hint: make sure not to include the lines that start with 'From:'. Also look at the last line of the sample output to see how to print the count.

# Desired Output:
# stephen.marquard@uct.ac.za
# louis@media.berkeley.edu
# ... [more emails]
# cwen@iupui.edu
# cwen@iupui.edu
# There were 27 lines in the file with From as the first word

fhand = input("Enter file name: ")
fh = open(fhand)
emails = []
count = 0

for line in fh:
    line.strip()
    if line.startswith("From "):
        words = line.split()
        emails.append(words[1])
        count += 1

for email in emails:
    print(email)

print("There were", count, "lines in the file with From as the first word")