In this python program, we use the twint library to get the twitter tweets.

Twint is an advanced Twitter scraping tool written in Python that allows for scraping Tweets from Twitter profiles without using Twitter's API.

Twint utilizes Twitter's search operators to let you scrape Tweets from specific users, scrape Tweets relating to certain topics, 
hashtags & trends, or sort out sensitive information from Tweets like e-mail and phone numbers. I find this very useful, and you 
can get really creative with it too.

Twint also makes special queries to Twitter allowing you to also scrape a Twitter user's followers, 
Tweets a user has liked, and who they follow without any authentication, API, Selenium, or browser emulation.


After getting the tweets saved in a csv file we take the tweets one by one, 
1. Clean the text for sentiment analysis.
2. Do sentiment analysis using textblob library
3. Save the tweet and it's sentiment to a new output csv file.


