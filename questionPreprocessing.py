# TODO:
#   Preprocessing:
#       [x] Make questions and answers list.
#       [x] Tokenize the questions.
#   Question Analysis:
#       [ ]
from nltk.tokenize import RegexpTokenizer

tokenedQuestions = []
corpus_words = {}

with open('questions.txt') as f:
    content = f.readlines()

questions = [x.strip() for x in content]
tokenizer = RegexpTokenizer(r'\w+')
for question in questions:
    question = tokenizer.tokenize(question.lower())
    tokenedQuestions.append(question)

for question in tokenedQuestions:
    for word in question:
        if word not in corpus_words:
            corpus_words[word] = 1
        else:
            corpus_words[word] += 1

print corpus_words
# QUESTIONS_VECTOR = [['what', 'is', 'sugar'], ['who', 'is', 'doing', 'sugar', 'development'], ['does', 'sugar', 'support', 'android'], ['what', 'makes', 'sugar', 'different', 'from', 'other', 'educational', 'software', 'platforms'], ['who', 'can', 'use', 'sugar', 'and', 'how', 'do', 'they', 'benefit'], ['why', 'sugar'], ['does', 'sugar', 'run', 'on', 'gnu', 'linux', 'fedora', 'ubuntu', 'suse', 'mac', 'os', 'windows', 'etc'], ['is', 'there', 'an', 'image', 'of', 'the', 'os', 'that', 'can', 'be', 'run', 'on', 'a', 'pc'], ['does', 'sugar', 'run', 'on', 'an', 'asus', 'eee', 'pc', 'or', 'other', 'ultra', 'mobile', 'or', 'mini', 'pcs'], ['are', 'there', 'any', 'platforms', 'where', 'sugar', 'runs', 'on'], ['what', 'is', 'sugar', 'labs'], ['what', 'is', 'the', 'mission', 'of', 'sugar', 'labs'], ['what', 'are', 'the', 'principles', 'that', 'guide', 'sugar', 'labs'], ['what', 'is', 'the', 'relationship', 'of', 'sugar', 'labs', 'to', 'one', 'laptop', 'per', 'child'], ['what', 'is', 'the', 'standard', 'sugar', 'license'], ['what', 'is', 'a', 'sugar', 'activity'], ['who', 'is', 'upstream', 'for', 'sugar'], ['who', 'is', 'sugar', 'labs'], ['how', 'do', 'i', 'get', 'involved']]
# CORPUS_WORDS = {'and': 1, 'mini': 1, 'suse': 1, 'be': 1, 'doing': 1, 'is': 10, 'child': 1, 'mission': 1, 'an': 2, 'platforms': 2, 'are': 2, 'linux': 1, 'where': 1, 'activity': 1, 'any': 1, 'principles': 1, 'what': 8, 'from': 1, 'fedora': 1, 'for': 1, 'pc': 2, 'pcs': 1, 'support': 1, 'there': 2, 'per': 1, 'sugar': 17, 'how': 2, 'other': 2, 'use': 1, 'android': 1, 'i': 1, 'image': 1, 'can': 2, 'development': 1, 'do': 2, 'run': 3, 'to': 1, 'relationship': 1, 'that': 2, 'who': 4, 'different': 1, 'educational': 1, 'labs': 5, 'eee': 1, 'mac': 1, 'mobile': 1, 'they': 1, 'ubuntu': 1, 'get': 1, 'one': 1, 'why': 1, 'standard': 1, 'upstream': 1, 'a': 2, 'on': 4, 'runs': 1, 'laptop': 1, 'license': 1, 'gnu': 1, 'windows': 1, 'os': 2, 'involved': 1, 'guide': 1, 'etc': 1, 'benefit': 1, 'does': 3, 'of': 3, 'asus': 1, 'the': 5, 'ultra': 1, 'makes': 1, 'or': 2, 'software': 1}
