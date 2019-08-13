import nltk
from nltk.corpus import sentiwordnet as swn
from textblob import TextBlob



words_tagged = [('good','a'),('bad','a'),('walk','v'),('fire','n'),('siva','n')]
words_tagged = [('I','n'),('love','v'),('this','a'),('movie','n')]

for word,tag in words_tagged:
    print(word+':'+tag+"  ")
    concat = word+'.'+tag+'.01'
    text = TextBlob(concat)
    if(swn.senti_synset(concat).pos_score()==swn.senti_synset(concat).neg_score()==0):
    # they both should be zero
        print(text.sentiment)
    else:
        print(swn.senti_synset(concat))
    # just write if pos_score > neg_score tag it as ppositive else negative
    # Before this if assign by senti and then textblob ASSIGN ANYWAY
# words_tagged = [('I','n'),('love','v'),('this','a'),('movie','n')]
# for word,tag in words_tagged:
#     print(word+':'+tag+"  ")
#     concat = word+'.'+tag+'.01'
# print(swn.senti_synset(concat))
