#documentation from https://www.youtube.com/watch?v=p8hG8MhzoYc AND ALSO https://medium.com/dataseries/how-to-scrape-millions-of-tweets-using-snscrape-195ee3594721
import snscrape.modules.twitter as twitterScraper

scraper = twitterScraper.TwitterSearchScraper('"YOUR SEARCH PHRASE" since:2021-11-18 until:2021-11-19') #modify dates as you wish

tweet_list = []

for i,tweet in enumerate(scraper.get_items()):
    if i > 1000: #if you want to fetch more tweets, just increase the number before the break
        break
    tweet_list.append(tweet.content)
    
x = len(tweet_list)
print("There are {} tweets on the list".format(x))
print(tweet_list)
