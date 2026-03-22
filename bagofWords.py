# using pandas to read the data
import pandas as pd;
messages = pd.read_csv('../SMSSpamCollection', sep='\t', names=['label','message'])
# print(messages)
# data cleaning and preprocessing
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()
corpus =[]
for i in range(0, len(messages)):
    review = re.sub('[^a-zA-Z]',' ',messages['message'][i])
    review = review.lower()
    review = review.split()
    review =[ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)

# here also we can optimize it using snowballstemmer or lemmitizer 
# creating bag of words model
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=100, binary=True)
x = cv.fit_transform(corpus).toarray()
print(x)

