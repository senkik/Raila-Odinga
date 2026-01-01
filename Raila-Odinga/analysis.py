import pandas as pd
import re
from textblob import TextBlob

# For now, let's use a sample of what you just saw to keep working
data = {
    'date': ['2026-01-01 09:20:32', '2026-01-01 09:19:54'],
    'text': ['@Kenyans ODM kwisha😂😂', 'RT @TruthDefenders_: "Uddhav Thackeray brought...']
}

df = pd.DataFrame(data)

# ---------------------------------------------------------
# Step 2: The Cleaning Function (Crucial for Data Science)
# ---------------------------------------------------------
def clean_tweet(text):
    text = re.sub(r'RT\s+', '', text)          # Remove RT prefix
    text = re.sub(r'@[A-Za-z0-9_]+', '', text) # Remove @mentions
    text = re.sub(r'http\S+', '', text)        # Remove links
    text = re.sub(r'#', '', text)               # Remove hashtag symbol but keep the word
    text = text.encode('ascii', 'ignore').decode('ascii') # Remove emojis
    return text.strip().lower()

df['clean_text'] = df['text'].apply(clean_tweet)

# ---------------------------------------------------------
# Step 3: Sentiment Scoring
# ---------------------------------------------------------
df['polarity'] = df['clean_text'].apply(lambda x: TextBlob(x).sentiment.polarity)
df['sentiment'] = df['polarity'].apply(lambda x: 'Positive' if x > 0 else ('Negative' if x < 0 else 'Neutral'))

print(df[['text', 'clean_text', 'sentiment']])