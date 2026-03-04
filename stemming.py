from nltk.stem import PorterStemmer,RegexpStemmer,SnowballStemmer
ps = PorterStemmer()
rg = RegexpStemmer('ing$|s$|e$|able$', min=4)
# this has various language support like french and germen as well
sb = SnowballStemmer("english")

words=["program","programs","programmer","programming","programmers",
       "ran","run","running","runs","congratulations"]

# for word in words:
#     print(word + "----> " + ps.stem(word))

# for word in words:
#     print(word + "----> " + rg.stem(word))

for word in words:
    print(word + "----> " + sb.stem(word))