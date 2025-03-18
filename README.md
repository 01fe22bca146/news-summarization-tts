News Summarization and Text-to-Speech Application
A web-based application that extracts key details from multiple news articles related to a given company, performs sentiment analysis, conducts a comparative analysis, and generates a Hindi text-to-speech (TTS) audio summary of the news. Users can input a company name and receive a structured sentiment report along with an audio summary.

Table of Contents
Overview
Features
Project Structure
Setup and Installation
API Endpoints
Model Details and Libraries
Deployment
Assumptions & Limitations
Contribution Guidelines
License
Contact

Overview
This project creates an end-to-end system for news summarization and sentiment analysis. The application:
Scrapes at least 10 unique news articles about a specified company.
Extracts article titles, summaries, and metadata.
Performs sentiment analysis (Positive, Negative, Neutral) on the news content.
Compares sentiments across the articles.
Converts the summarized sentiment report into Hindi speech using a TTS model.
Provides a simple user interface built with Streamlit and exposes backend functionality via FastAPI.

Features
News Extraction: Scrapes non-JavaScript-enabled news websites using BeautifulSoup.
Sentiment Analysis: Uses VADER to classify the sentiment of each article.
Comparative Analysis: Provides a breakdown of the sentiment distribution and highlights key differences between articles.
Text-to-Speech (TTS): Generates a Hindi speech output summarizing the sentiment report using gTTS.
Web Interface: User-friendly interface built with Streamlit.
API-Driven: Frontend and backend communicate via REST APIs built with FastAPI.
Deployment: Ready to be deployed on Hugging Face Spaces.

Project Structure
├── api.py                    # FastAPI backend handling news extraction and TTS generation
├── app.py                    # Streamlit frontend application
├── news_scraper.py           # Module to fetch and parse news articles
├── sentiment_analysis.py     # Module to perform sentiment analysis using VADER
├── comparative_analysis.py   # Module for comparing sentiments across articles
├── tts.py                    # Module to generate Hindi TTS audio using gTTS
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation (this file)

Setup and Installation
Prerequisites
Python 3.7 or higher
Git
(Optional) A Hugging Face account for deployment on Hugging Face Spaces
Local Setup

Clone the Repository:
git clone https://github.com/yourusername/news-summarization-tts.git
cd news-summarization-tts

Create and Activate a Virtual Environment:
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows

Install Dependencies:
pip install -r requirements.txt

Run the FastAPI Backend:
uvicorn api:app --reload
The backend API will be available at http://127.0.0.1:8000.

Run the Streamlit Frontend:
Open a new terminal (with the virtual environment activated) and run:
streamlit run app.py
Then, open the URL (typically http://localhost:8501) in your browser.

API Endpoints
GET /get-news/{company}
Description: Fetches 10 news articles related to the specified company and performs sentiment analysis.

Response Format:
{
  "company": "Tesla",
  "articles": [
    {
      "title": "Article Title",
      "link": "Article URL",
      "sentiment": "Positive/Negative/Neutral"
    },
    ...
  ],
  "comparison": {
    "Sentiment Distribution": {
      "Positive": 5,
      "Negative": 3,
      "Neutral": 2
    },
    "Most Common Sentiment": "Positive"
  }
}
GET /generate-tts/{company}
Description: Generates a Hindi TTS audio summary of the news sentiment report.
Response: Returns the path to the generated audio file (e.g., "output.mp3").
Model Details and Libraries
News Extraction:
Uses requests and BeautifulSoup (bs4) for web scraping.

Sentiment Analysis:
Utilizes VADER from the vaderSentiment library to classify sentiment.

Text-to-Speech (TTS):
Implements gTTS to convert text summaries into Hindi speech.

User Interface:
Built with Streamlit for a simple web interface.

API Development:
Powered by FastAPI to handle backend logic and provide RESTful endpoints.

Deployment
Deploying on Hugging Face Spaces

Push Your Code to GitHub:
git add .
git commit -m "Initial commit"
git push origin main

Create a New Space on Hugging Face:
Visit Hugging Face Spaces.
Create a new Space and select the appropriate interface (Streamlit or Gradio).
Link your GitHub repository to the Space.

Deploy:
Follow the instructions provided by Hugging Face to complete the deployment.
Once deployed, share your Hugging Face Spaces URL as part of your submission.
Assumptions & Limitations

Scraping:
The scraper only targets non-JS-enabled links; dynamic content might not be captured.

Sentiment Analysis:
VADER is optimized for social media and may not perfectly capture the nuances of news articles.

Text-to-Speech:
The quality of the TTS output depends on gTTS and may require optimization for longer summaries.

Summarization:
The project currently uses article titles and available metadata; further development might be needed for in-depth content summarization.



Contact
For any queries or further information, please contact:
Nayeem Patwegar
nayeempatwegar1@gmail.com

