from collections import Counter

def comparative_sentiment(articles):
    sentiments = [article['sentiment'] for article in articles]
    sentiment_counts = Counter(sentiments)
    
    comparison = {
        "Sentiment Distribution": sentiment_counts,
        "Most Common Sentiment": max(sentiment_counts, key=sentiment_counts.get)
    }
    
    return comparison
