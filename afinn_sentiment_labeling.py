# Afinn sentiment LABELING
from afinn import Afinn
af = Afinn()
count_total=0
count_pos=0
count_neut=0

count_neg=0
li_af = []
for i in range(len(df.index)):
    sent = str(df.loc[i]['full_text'])
    if(af.score(sent)>0):
        count_pos=count_pos+1
        count_total=count_total+1
        li_af.append(1)
    elif(af.score(sent)<0):
        count_neg=count_neg+1
        count_total=count_total+1
        li_af.append(-1)
    else:
        li_af.append(0)
        count_total=count_total+1
        count_neut+=1



#         print(df.loc[i]['full_text'])
#         print(sent.sentiment)
print("Total tweets:",len(df.index))
print("Total tweets with sentiment:",count_total)
print("positive tweets:",count_pos)
print("negative tweets:",count_neg)
print("neutral tweets:",count_neut)
