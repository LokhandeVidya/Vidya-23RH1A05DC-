import nltk
import nltk.sentiment
nltk.download('vader_lexicon')
from nltk.sentiment import SentimentIntensityAnalyzer
texts=["I love this movie","It's fantastic",
      "It's okay, not too bad",
      "I hated the movie. Very disappointed"]
sia=SentimentIntensityAnalyzer()
for text in texts:
    print(texts)
    scores=sia.polarity_scores(text)
    compound=scores['compound']
    sentiment=("Positive" if compound>0.05 else
               "Negative" if compound<0.05 else
               "Neutral")
    print(text)
    print(scores)
    print(sentiment)
    