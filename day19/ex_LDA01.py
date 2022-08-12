# pip install nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import gensim
import nltk  # 자연어처리 라이브러리

doc1 = "Brocolli is good to eat. My brother likes to eat good brocolli, but not my mother."
doc2 = "My mother spends a lot of time driving my brother around to baseball practice."
doc3 = "Some health experts suggest that driving may cause increased tension and blood pressure."
doc4 = "I often feel pressure to perform well at school, but my mother never seems to drive my brother to do better."
doc5 = "Health professionals say that brocolli is good for your health."

word_tokenizer = RegexpTokenizer(r'\w+')
nltk.download('stopwords')
en_stop = set(stopwords.words('english'))
p_stemmer = PorterStemmer()
doc_set = [doc1, doc2, doc3, doc4, doc5]
texts = []
for i in doc_set:
    raw = i.lower()
    word_token = word_tokenizer.tokenize(raw)
    stop_tokens = [i for i in word_token if not i in en_stop]
    stem = [p_stemmer.stem(i) for i in stop_tokens]
    texts.append(stem)
print(texts)
from gensim import corpora

word_dictionary = corpora.Dictionary(texts)
corpus = [word_dictionary.doc2bow(text) for text in texts]
ldamodel = gensim.models.ldamodel.LdaModel(corpus,
                                           num_topics=2  # 토픽 수
                                           , id2word=word_dictionary  # 단어 주머니
                                           , passes=100)  # epoch
print(ldamodel)
topic = ldamodel.print_topics(num_topics=2, num_words=5)
# print(topic)
for i in topic:
    print(i)
test1 = ldamodel[word_dictionary.doc2bow(texts[0])]
test2 = ldamodel[word_dictionary.doc2bow(texts[2])]
print('0문서:', test1, '2문서:', test2)
