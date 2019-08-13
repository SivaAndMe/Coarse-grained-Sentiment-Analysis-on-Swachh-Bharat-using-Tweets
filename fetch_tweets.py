import tweepy
import jsonpickle
import csv
import time
st = time.time()
API_KEY="******************"
API_SECRET="*************************"

auth = tweepy.AppAuthHandler(API_KEY,API_SECRET)
api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
#wait_on_rate_limit – Whether or not to automatically wait for rate limits to replenish
#wait_on_rate_limit_notify – Whether or not to print a notification when Tweepy is waiting for rate limits to replenish
# the sleep mode is automatically enabled with above 2 args


tweetsPerQuery = 100#this is the maximum provided by API
max_tweets = 100000000 # just for the sake of While loop
fName = 'sb_04_08_19.txt' # where i save the tweets

# No sinceId and max_id ..Get whathever you have exhaustively
since_id = None
max_id = -1
tweet_count = 0
print("Downloading the tweeets..takes some time..")

search_query="#SwachhBharat"
x=0
with open(fName,'w') as f:
    print("Downloading hashtag" + search_query)
    while(tweet_count<max_tweets):
        try:
            if(max_id<=0):
                if(not since_id):
                    new_tweets = api.search(q=search_query,count=tweetsPerQuery,lang="en",tweet_mode='extended')

                else:
                    new_tweets = api.search(q=search_query,count=tweetsPerQuery,lang="en",tweet_mode='extended',since_id=since_id)
            else:
                if(not since_id):
                    new_tweets = api.search(q=search_query,count=tweetsPerQuery,lang="en",tweet_mode='extended',max_id=str(max_id-1))
                else:
                    new_tweets = api.search(q=search_query,count=tweetsPerQuery,lang="en",tweet_mode='extended',max_id=str(max_id-1),since_id=since_id)

            # Tweets Exhausted
            if(not new_tweets):
                print("No more tweets found!!")
                break
            # write all the new_tweets to a json file
            for tweet in new_tweets:
                f.write(jsonpickle.encode(tweet._json,unpicklable=False)+'\n')
                tweet_count+=len(new_tweets)
                print("Successfully downloaded {0} tweets".format(tweet_count))
                max_id=new_tweets[-1].id
        # in case of any error
        except tweepy.TweepError as e:
                print("Some error!!:"+str(e))
                break
end = time.time()

print("A total of {0} tweets are downloaded and saved to {1}".format(tweet_count,fName))
print("Total time taken is ",end-st,"seconds.")
