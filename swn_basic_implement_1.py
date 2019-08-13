import nltk
import numpy
print("HI !!")
from nltk.corpus import sentiwordnet as swn

breakdown    = "hello , you are an amazing person ! I like you"
breakdown = "bad"
n = 'v'
print(swn.senti_synset('breakdown.n.03'))
print(swn.senti_synset.pos_score())
print(list(swn.senti_synsets('slow')))
print(breakdown)
print(breakdown.pos_score())
print(breakdown.neg_score())
print(breakdown.obj_score())
