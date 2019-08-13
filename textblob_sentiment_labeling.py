
#TextBlob SENTIMENT LABELING
from textblob import TextBlob
count_total=0
count_pos=0
count_neg=0
count_neut=0

li_tb = []
for i in range(len(df.index)):
    sent = TextBlob(str(df.loc[i]['full_text']))
    if(sent.sentiment.polarity>0):
        count_pos=count_pos+1
        count_total=count_total+1
        li_tb.append(1)
    elif(sent.sentiment.polarity<0):
        count_neg=count_neg+1
        count_total=count_total+1
        li_tb.append(-1)
    else:
        li_tb.append(0)
        count_neut+=1

        count_total=count_total+1


#         print(df.loc[i]['full_text'])
#         print(sent.sentiment)
print("Total tweets:",len(df.index))
print("Total tweets with sentiment:",count_total)
print("positive tweets:",count_pos)
print("negative tweets:",count_neg)
print("neutral tweets:",count_neut)
