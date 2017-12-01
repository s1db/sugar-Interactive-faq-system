# TODO:
#   Preprocessing:
#       [x] Make questions and answers list.
#       [x] Tokenize the questions.
#       [x] Remove common punctuation.
#   Question Analysis:
#       [x] multinomial Bayes Classifyer
#   Answering:
#       [x] IRC Connection.
#       [ ] Sending result.
#       [ ] A decision tree of responses.


# Imports
import nltk
import socket

# Constants
QUESTIONS_VECTOR = [['what', 'is', 'sugar'], ['who', 'is', 'doing', 'sugar', 'development'], ['does', 'sugar', 'support', 'android'], ['what', 'makes', 'sugar', 'different', 'from', 'other', 'educational', 'software', 'platforms'], ['who', 'can', 'use', 'sugar', 'and', 'how', 'do', 'they', 'benefit'], ['why', 'sugar'], ['does', 'sugar', 'run', 'on', 'gnu', 'linux', 'fedora', 'ubuntu', 'suse', 'mac', 'os', 'windows', 'etc'], ['is', 'there', 'an', 'image', 'of', 'the', 'os', 'that', 'can', 'be', 'run', 'on', 'a', 'pc'], ['does', 'sugar', 'run', 'on', 'an', 'asus', 'eee', 'pc', 'or', 'other', 'ultra', 'mobile', 'or', 'mini', 'pcs'], ['are', 'there', 'any', 'platforms', 'where', 'sugar', 'runs', 'on'], ['what', 'is', 'sugar', 'labs'], ['what', 'is', 'the', 'mission', 'of', 'sugar', 'labs'], ['what', 'are', 'the', 'principles', 'that', 'guide', 'sugar', 'labs'], ['what', 'is', 'the', 'relationship', 'of', 'sugar', 'labs', 'to', 'one', 'laptop', 'per', 'child'], ['what', 'is', 'the', 'standard', 'sugar', 'license'], ['what', 'is', 'a', 'sugar', 'activity'], ['who', 'is', 'upstream', 'for', 'sugar'], ['who', 'is', 'sugar', 'labs'], ['how', 'do', 'i', 'get', 'involved']]
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = 'chat.freenode.net' #irc server
PORT = 6665 #port
NICK = 'faqsbot'
USERNAME = 'faqsbot'
REALNAME = 'Sidhant Bhavnani'

# Functions
def Classifyer(sentence, QUESTIONS_VECTOR=QUESTIONS_VECTOR):
    score = 0.0
    highest_class = ['', 0.0]
    secondHighest_class = ['', 0.0]
    thirdHighest_class = ['', 0.0]
    # tokenize each word in our new sentence
    sentence = nltk.word_tokenize(sentence)
    for c in QUESTIONS_VECTOR:
        for word in sentence:
            # check to see if the stem of the word is in any of our classes
            if word in c:
                # treat each word with same weight
                score += 1.0
            relativescore = score/len(c)
        if relativescore > highest_class[1]:
            highest_class[0] = c
            highest_class[1] = relativescore
        elif relativescore > secondHighest_class[1]:
            secondHighest_class[0] = c
            secondHighest_class[1] = relativescore
        elif relativescore > thirdHighest_class[1]:
            thirdHighest_class[0] = c
            thirdHighest_class[1] = relativescore
        score = 0.0
    return (highest_class, secondHighest_class, thirdHighest_class)

# IRC Connection
print('soc created |', s)
remote_ip = socket.gethostbyname(HOST)
print('ip of irc server is:', remote_ip)


s.connect((HOST, PORT))

print('connected to: ', HOST, PORT)

nick_cr = ('NICK ' + NICK + '\r\n').encode()
s.send(nick_cr)
usernam_cr= ('USER megadeath megadeath megadeath :rainbow pie \r\n').encode()
s.send(usernam_cr)
s.send('JOIN #sugar-newbies \r\n'.encode()) #chanel

#IRC Communication
while 1:
    data = s.recv(4096).decode('utf-8')
    if data.find('PING') != -1:
        s.send(str('PONG ' + data.split(':')[1] + '\r\n').encode())
        print('PONG sent \n')
    if data.find('faqsbot') != -1:
        print(data.split()[2])
        s.send((str('PRIVMSG ' + data.split()[2]) + ' Hi! \r\n').encode())

s.close()
