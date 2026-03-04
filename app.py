from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize,wordpunct_tokenize,TreebankWordTokenizer

corpus = """Hello I am Itika. I am a teacher.
I am teaching in YT! as well as i am a full Stack developer."""

sentences = TreebankWordTokenizer().tokenize(corpus)
print(sentences)

for sentence in sentences:
    # words = word_tokenize(sentence)
    words = TreebankWordTokenizer().tokenize(sentence)
    print(words)