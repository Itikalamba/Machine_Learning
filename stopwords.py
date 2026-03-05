from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

paragraph = """Natural Language Processing is an exciting field of artificial intelligence that focuses on enabling computers to understand, interpret, and generate human language in a meaningful way. Every day, millions of people interact with digital systems through voice assistants, chatbots, emails, and social media platforms. However, raw text data is often messy, unstructured, and filled with punctuation, special characters, numbers, and irrelevant words. Therefore, text preprocessing becomes an essential step before applying machine learning models. It involves cleaning the data, converting text to lowercase, removing stopwords, performing stemming or lemmatization, and transforming words into numerical representations so that algorithms can analyze them efficiently and accurately."""
stemmer = SnowballStemmer("english")
lemmatizer = WordNetLemmatizer()
sentences = sent_tokenize(paragraph)

for i in range(len(sentences)):
    words = word_tokenize(sentences[i])
    words = [lemmatizer.lemmatize(word.lower(),pos='v') for word in words if word not in set(stopwords.words("english"))]
    # words = [stemmer.stem(word) for word in words if word not in set(stopwords.words("english"))]
    sentences[i] = " ".join(words)

print(sentences)

