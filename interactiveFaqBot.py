# TODO:
#   Preprocessing:
#       [x] Make questions and answers list.
#       [x] Tokenize the questions.
#       [x] Remove common punctuation.
#   Question Analysis:
#       [x] multinomial Bayes Classifyer
#   Answering:
#       [x] IRC Connection.
#       [x] Sending result.
#       [x] A decision tree of responses.


# Imports
import sys
import nltk
import time
import socket
from random import *

# Constants
QUESTIONS_VECTOR = [['what', 'is', 'sugar'], ['who', 'is', 'doing', 'sugar', 'development'], ['does', 'sugar', 'support', 'android'], ['what', 'makes', 'sugar', 'different', 'from', 'other', 'educational', 'software', 'platforms'], ['who', 'can', 'use', 'sugar', 'and', 'how', 'do', 'they', 'benefit'], ['why', 'sugar'], ['does', 'sugar', 'run', 'on', 'gnu', 'linux', 'fedora', 'ubuntu', 'suse', 'mac', 'os', 'windows', 'etc'], ['is', 'there', 'an', 'image', 'of', 'the', 'os', 'that', 'can', 'be', 'run', 'on', 'a', 'pc'], ['does', 'sugar', 'run', 'on', 'an', 'asus', 'eee', 'pc', 'or', 'other', 'ultra', 'mobile', 'or', 'mini', 'pcs'], ['are', 'there', 'any', 'platforms', 'where', 'sugar', 'runs', 'on'], ['what', 'is', 'sugar', 'labs'], ['what', 'is', 'the', 'mission', 'of', 'sugar', 'labs'], ['what', 'are', 'the', 'principles', 'that', 'guide', 'sugar', 'labs'], ['what', 'is', 'the', 'relationship', 'of', 'sugar', 'labs', 'to', 'one', 'laptop', 'per', 'child'], ['what', 'is', 'the', 'standard', 'sugar', 'license'], ['what', 'is', 'a', 'sugar', 'activity'], ['who', 'is', 'upstream', 'for', 'sugar'], ['who', 'is', 'sugar', 'labs'], ['how', 'do', 'i', 'get', 'involved']]

QUESTIONS = ["What is Sugar?", "Who is doing Sugar development?", "Does Sugar support Android?", "What makes Sugar different from other educational software platforms?", "Who can use Sugar and how do they benefit?", "Why Sugar?", "Does Sugar run on {GNU/Linux, Fedora, Ubuntu, SUSE, MAC OS, Windows, etc.}?", "Is there an image of the OS that can be run on a PC?", "Does Sugar run on an ASUS Eee PC (or other 'ultra-mobile' or 'mini' PCs)?", "Are there any platforms where Sugar runs on?", "What is Sugar Labs?", "What is the mission of Sugar Labs?", "What are the principles that guide Sugar Labs?", "What is the relationship of Sugar Labs to One Laptop per Child?", "What is the standard Sugar license?", "What is a Sugar Activity?", "Who is upstream for Sugar?", "Who is Sugar Labs?", "How do I get involved?"]

ANSWERS = ['Sugar is an educational software platform built with the Python programming language and based on the principles of cognitive and social constructivism. See What is Sugar?.', 'Sugar is a community project where all work is done by volunteers. You can get an idea of the people involved from the Development Team/Release/Modules page.', 'Not at this time, although there are some developers working to change that situation. See this mailing list thread.', "See Website sandbox.<br>The Sugar interface, in its departure from the desktop metaphor for computing, is the first serious attempt to create a user interface that is based on both cognitive and social constructivism: learners should engage in authentic exploration and collaboration. It is based on three very simple principles about what makes us human: (1) everyone is a teacher and a learner; (2) humans by their nature are social beings; and (3) humans by their nature are expressive. These are the pillars of a user experience for learning.<br>Sugar also considers two aphorisms: (1) you learn through doing, so if you want more learning, you want more doing; and (2) love is a better master than duty\xe2\x80\x94you want people to engage in things that are authentic to them, things that they love.<br>The presence of other people is inherent to the Sugar interface: collaboration is a first-order experience. Students and teachers engage in a dialog with each other, support each other, critique each other, and share ideas.<br>Sugar is also discoverable: it can accommodate a wide variety of users, with different levels of skill in terms of reading, language, and different levels of experience with computing. It is easy to approach, and yet it doesn't put an upper bound on personal expression; one can peel away layers and go deeper and deeper, with few restrictions.<br>Sugar is based on Python, an interpreted language, allowing the direct appropriation of ideas: in whatever realm the learner is exploring\xe2\x80\x94music, browsing, reading, writing, programming, graphics, etc.\xe2\x80\x94they are able to drill deeper; they are not going to hit a wall, since they can, at every level, engage in debugging both their personal expression and the very tools that they use for that expression.", 'Sugar is a free software project, freely available to anyone who wants to use it or improve upon it.<br>The Sugar platform was designed for young children (K\xe2\x80\x936), but it is finding applicability in a number of different venues where the simplicity of design maps is an enabler, e.g., mobile applications, the elderly, etc.', 'Why Sugar? Sugar will engage even the youngest learner in the use of computation as a powerful "thing to think with." They will quickly become proficient in using the computer as a tool to engage in authentic problem-solving. Sugar users develop skills that help them in all aspects of life.<br>Sugar comes with hundreds of tools for discovery through exploring, expressing, and sharing: browsing, writing, rich media, etc.<br>Sugar comes with a built-in collaboration system: peer-to-peer learning; always-on support; and single-click sharing.<br>Sugar comes with built-in tools for reflection; a built-in portfolio assessment tool that serves as a forum for discussion between children, their parents, and their teachers.<br>The Sugar learning platform is discoverable: it uses simple means to reach to complex ends with no upper bound on where you can reach.<br>Sugar is designed for local appropriation: it has built-in tools for making changes and improvements and a growing global community of support.<br>Sugar puts an emphasis on learning through doing and debugging: more engaged learners are to tackle authentic problems.<br>Sugar is available in a wide variety of forms: as part of GNU/Linux distributions; LiveUSB/CD; and in virtual machines or emulation.<br>There is a further summary of the Sugar benefits here.', 'Please refer to the Supported systems page for an up-to-date list of supported systems.', 'You can download a Live USB image at Sugar on a Stick and a Live CD version of Sugar at http://wiki.laptop.org/go/LiveCd, or run Sugar natively on a supported system. (The language can be set from the Sugar-control-panel or My Settings link on the avatar panel.)', 'Yes. If it can run GNU/Linux and GNOME, it can run Sugar. Try Sugar on a Stick as a way to get started, but you should be able install it natively as well.', 'The Sugar Learning Platform is a leading learning platform that began in the famous One Laptop Per Child project. It is used every day by nearly 3 million children around the world. Sugarizer is a web implementation of the platform and runs on every device - from tiny Raspberry Pi computers to small Android and iOS phones to tablets and to laptops and desktops. It has 3 broad components:<br>1. Web Application: a web application that runs in modern web browsers<br>2. Application: an installable app for every operating system<br>3. Server: a nodejs/express server for applications to connect with<br>Enjoy the experience and help us reach every child on every device in every country.', 'Sugar Labs, a non-profit foundation, serves as a support base and gathering place for the community of educators and software developers who want to extend the Sugar platform and who have been creating Sugar-compatible applications.', 'The overarching mission of Sugar Labs is to support the Sugar platform through software development, and community outreach and support. The purpose of the Sugar platform is provide a software and content environment that enhances learning. Towards this end, Sugar is designed to facilitate learners to \xe2\x80\x9cexplore, express, debug, and critique.\xe2\x80\x9d', 'Sugar Labs subscribes to principle that learning thrives within a culture of freedom of expression, hence it has a natural affinity with the free software movement (Please see Principles page in this wiki for more details). The core Sugar platform has been developed under a GNU General Public License (GPL); individual activities may be under different licenses.', 'Sugar was originally developed as the user interface (UI) for the One Laptop per Child (OLPC) XO-1 laptop. Sugar Labs was established as an independent entity in order to facilitate the growth of Sugar beyond any single hardware platform. While Sugar Labs has a cooperative working relationship with OLPC, it is by no means an exclusive or proprietary relationship. Sugar Labs is not bound to any specific hardware platform or Linux distribution (Please see Supported systems).', 'Materials created by the Sugar Labs contributors are usually shared on GNU GPL free software license.', 'Activity is a small educational application (like this one) built into Sugar. Anyone can create an activity, you too...!', 'Sugar Labs is the upstream for the Sugar project.', 'Sugar is a community project, so it is the sum of those of you who participate. Sugar Labs was started by some Sugar-community members: Walter Bender, Christoph Derndorfer, Bert Freudenberg, Marco Pesenti Gritti, Bernardo Innocenti, Aaron Kaplan, Simon Schampijer, and Tomeu Vizoso. We have rules of governance that have been vetted by a process of public discussion.', 'Please see the Getting Involved page in this wiki.']

# IRC Constants
HOST = 'chat.freenode.net' #irc server
PORT = 6665 #port
NICK = 'faqsbot' # Uncomment for testing: + str(randint(1,1000))
CHANNEL = '#sugar'

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

def message(msg): #function for sending messages to the IRC chat
    irc.send('PRIVMSG ' + CHANNEL + ' : ' + msg + '\r\n')

#Establish connection
irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
irc.connect((HOST,6667))
irc.setblocking(False)
time.sleep(1)
irc.send("USER "+NICK+" "+NICK+" "+NICK+" :Hello! I am a test bot!\r\n")
time.sleep(1)
irc.send("NICK "+NICK+"\n")
time.sleep(1)
irc.send("JOIN "+CHANNEL+"\n")

message("To use try: @faqsbot 'YOUR-QUESTION'")
#IRC Communication
while 1:
    time.sleep(0.5)
    try:
        text=irc.recv(2040)
        print(text)
    except Exception:
        pass
    if text.find("PING")!=-1:
        irc.send("PONG "+text.split()[1]+"\r\n")
    try:
        if text.lower().find(":@faqsbot")!=-1:
            raw_response = Classifyer(text)
            indexValue = int(QUESTIONS_VECTOR.index(raw_response[0][0]))
            question = QUESTIONS[indexValue]
            answer = ANSWERS[indexValue]
            message('Question #1: ' + question)
            message(answer)
            message("Incase this isn't the question you were looking for, respond with '!next'.")
            text = text.replace(":@faqsbot", "")
    except Exception:
        none
    try:
        if text.lower().find(":!next")!=-1:
            indexValue = int(QUESTIONS_VECTOR.index(raw_response[1][0]))
            question = QUESTIONS[indexValue]
            answer = ANSWERS[indexValue]
            message('Question #2: ' + question)
            message(answer)
            message("Incase this isn't the question you were looking for, respond with '!!next'.")
            text = text.replace(":!next", "")
    except Exception:
        none
    try:
        if text.lower().find(":!!next")!=-1:
            indexValue = int(QUESTIONS_VECTOR.index(raw_response[2][0]))
            question = QUESTIONS[indexValue]
            answer = ANSWERS[indexValue]
            message('Question: ' + question)
            message(answer)
            text = text.replace(":!!next", "")
    except Exception:
        none

irc.close()
