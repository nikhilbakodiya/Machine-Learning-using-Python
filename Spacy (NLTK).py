import spacy
from spacy.lang.en.examples import sentences

nlp = spacy.load('en_core_web_sm')
doc = nlp("India is exporting $10 million software to U.S.")

#Tokenization
for token in doc:
    print(token.text)

doc1 = nlp("India is exporting $10 million software to U.S. It is one of the most growing sector.")

#Splitting Sentances
for s in doc1.sents:
    print(s)

doc[0]
doc[1:3]

#Part of speech (POS)
for token in doc:
    print(token.text,token.pos_)

#NER(Named Entity Recognition)
for entity in  doc1.ents:
    print(entity.text,entity.label_)


for entity in  doc1.ents:
    print(entity.text,entity.label_,str(spacy.explain(entity.label_)))

#Lemmatization
doc5 = nlp("I am a ruuner running in the race as i love to run since I ran past years")

for token in doc5:
    print(token.text,'\t',token.lemma_)

# Noun chunking
doc2 = nlp("India is exporting artificial intelligence software ")
for chunk in  doc2.noun_chunks:
    print(chunk)

#Stop words
spacy_stopwords = spacy.lang.en.stop_words.STOP_WORDS
len(spacy_stopwords)
list(spacy_stopwords)[:20]