with open('answers.txt') as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
print [x.strip() for x in content]
