import nltk 
nltk.download('punkt') #punctuation
nltk.download('punkt_tab') #tokenization
nltk.download('stopwords') #remove common english words
nltk.download('wordnet') #convert no grammatical words into grammatical words
from nltk.tokenize import word_tokenize #method
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string

text="""Machine learing ,Deep learning and natural language processing in are following the better
     algorithm  playing role in AL concepts"""

#slpitting sentence into words
words= word_tokenize(text)
print(words)

#stopwords remove english common words and store in another list
stop_words=set(stopwords.words('english'))
filtered=[w for w in words if w.lower() not in stop_words] #w indicates each and every word it check
print(filtered)

#for removing punctuations(special symbols)
#import string
remove_pun=[w for w in filtered if w not in string.punctuation]
print(remove_pun)

#lemmatization
lemmatizer=WordNetLemmatizer()
convert_words=[w lemmatizer.lemmatize(w) for word in remove_pun]
print(convert_words)


