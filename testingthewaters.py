#https://www.fastcompany.com/90697405/using-these-8-common-phrases-can-ruin-your-credibility
#https://www.huffpost.com/entry/phrases-not-say-during-argument_n_5aba7beee4b03e2a5c76d26c
#https://bestlifeonline.com/one-word-never-say-argument-news/
#https://www.linkedin.com/pulse/things-you-should-never-say-do-during-argument-hicks-i0k-plus-/
#https://www.nytimes.com/2016/05/01/opinion/sunday/stop-saying-i-feel-like.html


q1 = ['to be honest',
    'my oppinion',
    'my experience',
    'i think',
    'you may already know this',
    "i'm not sure",
    'i could be wrong',
    'just a thought',
    "if you don't mind",
    'everyone thinks',
    'would agree with me',
    'always happens',
    'they do',
    'always',
    'never',
    'all the time',
    'for 30 years',
    'stupid',
    'dumb',
    'idiot',
    'i feel like',
    'i feel',
    'i',
    ]

# opening a text file
file1 = open("transcript.txt", "r")
  
# read file content
readfile = file1.read()
  
# checking condition for string found or not
if any(x in readfile.lower() for x in q1):
    for i in range(len(q1)):
        if readfile.count(q1[i]) > 0:
            print(f'Phrase "{q1[i]}" Found In File', readfile.count(q1[i]), 'times')
else: 
    print('Strings not Found') 
  
# closing a file
file1.close() 
