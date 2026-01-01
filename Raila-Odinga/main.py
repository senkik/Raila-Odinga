import tweepy
import yaml
import pandas as pd
import re

# 1. Load credentials from YAML
with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

# 2. Authenticate with Twitter API v2
client = tweepy.Client(bearer_token=config['keys']['bearer_token']
                       ,wait_on_rate_limit=True)

# 3. Search for recent tweets (last 7 days)
print(f"Searching for: {config['search_params']['query']}...")
response = client.search_recent_tweets(
    query=config['search_params']['query'],
    max_results=10,
    tweet_fields=['created_at', 'lang', 'public_metrics']
)

# 4. Convert to a Pandas DataFrame for analysis
if response.data:
    tweets_data = []
    for tweet in response.data:
        tweets_data.append({
            'date': tweet.created_at,
            'text': tweet.text,
            'retweets': tweet.public_metrics['retweet_count']
        })
    
    df = pd.DataFrame(tweets_data)
    print("\n--- Data Preview ---")
    print(df.head())
else:
    print("No tweets found or check your API permissions.")
    
def clean_tweet(text):
    # 1. Remove "RT " prefix
    text = re.sub(r'^RT\s+', '', text)
    # 2. Remove @mentions
    text = re.sub(r'@[A-Za-z0-9_]+', '', text)
    # 3. Remove URLs
    text = re.sub(r'https?://\S+', '', text)
    # 4. Remove emojis/special characters (optional but helpful for basic NLP)
    text = text.encode('ascii', 'ignore').decode('ascii')
    # 5. Remove extra whitespace
    return text.strip()
df['clean_text'] = df['text'].apply(clean_tweet)

from textblob import TextBlob

def get_sentiment(text):
    analysis = TextBlob(text)
    return analysis.sentiment.polarity

df['sentiment'] = df['clean_text'].apply(get_sentiment)

# Label the sentiment
df['label'] = df['sentiment'].apply(lambda x: 'Positive' if x > 0 else ('Negative' if x < 0 else 'Neutral'))

# After getting your response:
if response.data:
    df.to_csv("raila_tweets_raw.csv", index=False)
    print("Data saved! You can now stop calling the API.")