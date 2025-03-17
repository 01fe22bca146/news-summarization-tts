from fastapi import FastAPI
from news_scraper import fetch_news
from sentiment_analysis import analyze_sentiment
from comparative_analysis import comparative_sentiment
from tts import generate_tts

app = FastAPI()

@app.get("/get-news/{company}")
def get_news(company: str):
    articles = fetch_news(company)
    for article in articles:
        article["sentiment"] = analyze_sentiment(article["title"])
    
    comparison = comparative_sentiment(articles)
    return {"company": company, "articles": articles, "comparison": comparison}

@app.get("/generate-tts/{company}")
def get_tts(company: str):
    news_data = get_news(company)
    summary_text = f"News Summary for {company}: {news_data['comparison']}"
    audio_file = generate_tts(summary_text)
    return {"audio": audio_file}
