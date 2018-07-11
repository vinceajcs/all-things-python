#message = 'Bobby\'s World'
#message = "Bobby's World"

# message = """I love chocolate
# so much"""

message = 'Hello World'

print(len(message))

print(message[10])

# Slicing

# first index is inclusive, second index is not
print(message[0:5])
# same as above
print(message[:5])

# prints world
print(message[6:])

print(message.lower())
print(message.upper())

# returns the number of l's in the string
print(message.count('l'))

# returns 6 because world starts at 6
print(message.find('World'))

# returns -1 if dinos does not exist
print(message.find('dinos'))

newMessage = message.replace('World', 'Universe')
print(newMessage)

greeting = 'Hello'
name = 'Michael'

# combines them together, but there's no space. So we add a space
message = greeting + " " + name
print(message)

#{} -> these are known as placeholders
message = '{}, {}. Welcome!'.format(greeting, name)
print(message)

# returns list of methods for strings
# print(dir(name))

# print(help(str))

# slicing continued
myList = [0, 1, 2, 3, 4, 5, 6, 7, 8]
# prints last element
print(myList[-1])

# list[start:end:step]

# all the ones below are the same
print(myList[1:7])
print(myList[1:-2])
print(myList[-8:-2])

print(myList[2:-1:2])
print(myList[-1:2:-1])

print(myList[::-1])

sample_url = "http://vincentstephenhuang.com"

# reverse the string
print(sample_url[::-1])

# print just the top level domain (i.e. .com)
print(sample_url[-4:])

# print url w/o http://
print(sample_url[6:])

# print url w/o http:// or the top level domain
print(sample_url[7:-4])

# multiplying strings
message2a = 'hello ' * 3
message2b = 'world'

print(message2a + message2b)

# appending
message3 = 'howdy'
message3 += ' '
message3 += 'world'

print(message3)

print(message3[:5].find('d'))
