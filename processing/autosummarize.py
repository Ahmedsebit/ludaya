# coding: utf8
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords


from collections import defaultdict
from string import punctuation
from heapq import nlargest


class FrequencySummarizer:

    def __init__(self, min_cut=0.1, max_cut=0.9):
        self._min_cut = min_cut
        self._max_cut = max_cut

        self._stopwords = set(stopwords.words('english') + list(punctuation))


    def _compute_frequency(self, word_sent):
        freq = defaultdict(int)
        for sentence in word_sent:
            for word in sentence:
                if word not in self._stopwords:
                    freq[word] +=1
        max_freq = float(max(freq.values())) 

        for word in freq.keys():
            freq[word] = freq[word]/max_freq

            if freq[word] >= self._max_cut or freq[word] <= self._min_cut:
                del freq[word]

        return freq

    def summarize(self, text, n):
        sents = sent_tokenize(text)
        assert n <= len(text)
        word_sent = [word_tokenize(sent.lower()) for sent in sents]

        self._freq = self._compute_frequency(word_sent)
        ranking = defaultdict(int)
        for i,sent in enumerate(word_sent):
            for word in sent:
                ranking[i] += self._freq[word]

        sents_idx = nlargest(n,ranking, key = ranking.get)
        return [sent[j] for j in sents_idx]
