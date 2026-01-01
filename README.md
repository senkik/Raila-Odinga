# 🇰🇪 Raila Odinga Legacy: Twitter Sentiment Analysis

An NLP-driven data science project analyzing the public discourse and sentiment surrounding the legacy of the late Raila Odinga. This project uses real-time data from the X (Twitter) API to explore how the "Baba" persona is remembered and discussed in 2026.

## 🚀 Overview
- **Goal**: To quantify public sentiment (Positive, Negative, Neutral) regarding Raila Odinga's political legacy.
- **Data Source**: X API v2 (Recent Search & Stream).
- **Key Techniques**: Sentiment Analysis (TextBlob), Data Cleaning (Regex), and Social Network Visualization.

## 🛠️ Tech Stack
- **Language**: Python 3.10+
- **Libraries**: `tweepy`, `pandas`, `textblob`, `matplotlib`, `seaborn`
- **Environment**: Virtual Environment (`venv`)

## 📋 Installation & Setup
1. **Clone the repo**:
   ```bash
   git clone [https://github.com/senkik/Raila-Odinga.git](https://github.com/senkik/Raila-Odinga.git)
   cd Raila-Odinga
2.Setup Environment:
   PowerShell:
   
   ```python
   python -m venv raila_env
.\raila_env\Scripts\activate
pip install -r requirements.txt
```
API Configuration: Create a config.yaml file in the root directory (this is ignored by Git for security):

YAML

keys:
  bearer_token: "YOUR_TOKEN_HERE"

## 📊 Methodology
Data Collection: Filtering tweets using keywords like #RailaOdinga, Agwambo, and Tinga.

Preprocessing:

Removing RTs, @mentions, and URLs.

Normalizing text (lowercasing and removing emojis).

Sentiment Scoring: Using TextBlob to assign Polarity scores (-1 to +1).

## 📊 Results

### Sentiment Analysis
![Sentiment Distribution](./images/sentiment_analysis_chart.png)
*Figure 1: Distribution of Positive, Neutral, and Negative sentiments from recent tweets.*

### Topic Visualization
![Word Cloud](./images/raila_wordcloud.png)
*Figure 2: Trending keywords associated with the discourse.*


