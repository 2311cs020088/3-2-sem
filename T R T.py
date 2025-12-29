texts = ["I love NLP", "NLP is fun"]

from sklearn.feature_extraction.text import CountVectorizer
bow = CountVectorizer()
print("BoW:", bow.fit_transform(texts).toarray())

from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer()
print("TF-IDF:", tfidf.fit_transform(texts).toarray())

ngram = CountVectorizer(ngram_range=(2,2))
print("N-grams:", ngram.fit_transform(texts).toarray())

import numpy as np
words = list(set(" ".join(texts).split()))
print("One-Hot for NLP:", np.eye(len(words))[words.index("NLP")])