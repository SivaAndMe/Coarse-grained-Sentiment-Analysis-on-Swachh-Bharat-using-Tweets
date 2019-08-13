import json
import csv


f = open('som1.csv','a',encoding='utf-8')
csvWriter = csv.writer(f)
headers=['full_text','retweet_count','user_followers_count','favorite_count','place','coordinates','geo','created_at','id_str']
csvWriter.writerow(headers)

for inputFile in ['sb_15_07_19.txt','sb_24_07_19.txt','sb_04_08_19.txt']:#all the text-file names you want to convert to Csv in the sae folder as this code
    tweets = []
    for line in open(inputFile, 'r'):
        tweets.append(json.loads(line))

    print('HI',len(tweets))
    count_lines=0
    for tweet in tweets:
        try:
            csvWriter.writerow([tweet['full_text'],tweet['retweet_count'],tweet['user']['followers_count'],tweet['favorite_count'],tweet['place'],tweet['coordinates'],tweet['geo'],tweet['created_at'],str(tweet['id_str'])])
            count_lines+=1
        except Exception as e:
            print(e)
    print(count_lines)
