import gensim
import numpy as np


google_model = gensim.models.KeyedVectors.load_word2vec_format('../bert/resources/GoogleNews-vectors-negative300.bin', binary=True)

def get_w2v(words):
    vecs = np.empty([0, 300])
    available = []
    for w in words:
        if w in google_model.key_to_index.keys():
            vecs = np.vstack((vecs, google_model.get_vector(w)))
            available.append(w)
    return vecs, available


def get_sentence_embedding(preprocessed_sent):
    vecs, av = get_w2v(preprocessed_sent)
    return np.average(vecs, axis=0)


def get_normalized_sentence_embedding(preprocessed_sent, frequency_dict):
    vecs, available = get_w2v(preprocessed_sent)
    result = np.zeros((1, vecs.shape[1]))
    for i, word in enumerate(preprocessed_sent):
        result += frequency_dict[word] * vecs[i]
    return result


def get_doc_embedding(processed_units):
    data = np.empty((0,300))
    for u in processed_units:
        data = np.vstack((data, get_sentence_embedding(u)))
    return data


def get_normalized_doc_embedding(processed_units, frequency_dict):
    data = np.empty((0, 300))
    for u in processed_units:
        data = np.vstack((data, get_normalized_sentence_embedding(u, frequency_dict)))
    return data