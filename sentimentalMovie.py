#import nltk
#nltk.download('punkt')
#nltk.download('stopwords')
#nltk.download('wordnet')
#nltk.download('movie_reviews')

#from nltk.tokenize import word_tokenize
#from nltk.corpus import movie_reviews
#import random

# Create a list of (word_list, category) tuples
#documents = [(list(movie_reviews.words(fileid)), category)for category in movie_reviews.categories()for fileid in movie_reviews.fileids(category)]

# Shuffle the documents for randomness (optional)
#random.shuffle(documents)

#print(documents[:2])***  # Show sample output###




import nltk
nltk.download('punkt')
nltk.download('punkt_tab') #removing special symbols and split words
nltk.download('stopwords') #remove common english words
nltk.download('wordnet') #convert non grammatical word to grammatical
nltk.download('movie_reviews') #it will download datasets of movie reviews
from nltk.corpus import movie_reviews,stopwords
from nltk.tokenize import word_tokenize
import random
#list=[x for x in arr for y in arr.get()]
document=[(list(movie_reviews.words(field)),category) for category in movie_reviews.categories() for field in movie_reviews.fileids(category)]
stop_words=set(stopwords.words('english'))
all_words=nltk.FreqDist(w.lower() for w in movie_reviews.words())
#only 200 words taken
word_features=list(all_words)[:1600]
print(word_features)
