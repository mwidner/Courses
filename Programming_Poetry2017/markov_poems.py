import nltk
import pymarkovchain
import string

words = nltk.corpus.gutenberg.words('whitman-leaves.txt')
words += nltk.corpus.gutenberg.words('milton-paradise.txt')
words += nltk.corpus.gutenberg.words('blake-poems.txt')
words += nltk.corpus.brown.words(categories=['fiction', 'science_fiction'])


seed = ' '.join([word for word in words if not word.isdigit()])
mc = pymarkovchain.MarkovChain('./markov')
mc.generateDatabase(seed)
verse = list()
for _ in range(10):
  line = mc.generateString()
  verse.append(line)
print('\n'.join(verse))

