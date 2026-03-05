import nltk
nltk.download('words')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker_tab')

sentence = """I am Itika. I am a teacher. I am teaching in YT! as well as i am a full Stack developer.
My hometown is yamunanagar. I am 24years old. I have earned around 6lakhs and my target is to earn 1 crore before 30 years of age.
"""
sentences = nltk.sent_tokenize(sentence)
for sent in sentences:
    words = nltk.word_tokenize(sent)
    words = [word for word in words if word not in set(nltk.corpus.stopwords.words("english"))]
    pos_tags = nltk.pos_tag(words)
    ans =nltk.ne_chunk(pos_tags)

ans.draw()