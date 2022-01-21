from os import walk
import re, string
import numpy as np
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktParameters, PunktTrainer
import nltk.data
from nltk.tokenize import sent_tokenize
from w2v_embedding import google_model
from sklearn.metrics import pairwise_distances
import tensorflow_datasets as tfds
from itertools import combinations



trainer = PunktTrainer()

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')


def load_cnn_daily_mail_test():
    cnn = tfds.summarization.CnnDailymail()
    cnn.download_and_prepare()
    cnn_dataset = cnn.as_dataset()

    test = cnn_dataset['test']
    test_np = tfds.as_numpy(test)

    cnn_test = []
    for item in test_np:
        temp = {}
        temp['text'] = item['article'].decode('utf8')
        temp['summary'] = item['highlights'].decode('utf8')
        cnn_test.append(temp)
    return cnn_test


def load_cnn_daily_mail_validation():
    cnn = tfds.summarization.CnnDailymail()
    cnn.download_and_prepare()
    cnn_dataset = cnn.as_dataset()

    validation = cnn_dataset['validation']
    validation_np = tfds.as_numpy(validation)

    cnn_validation = []
    for item in validation_np:
        temp = {}
        temp['text'] = item['article'].decode('utf8')
        temp['summary'] = item['highlights'].decode('utf8')
        cnn_validation.append(temp)
    return cnn_validation


def get_file_names(dir):
    f = []
    for (dirpath, dirnames, filenames) in walk(dir):
        f.extend(filenames)
        break
    return f


def get_sentences_from_doc(filename):
    with open(filename) as f:
        data = f.read()
    return get_sentences(data)


def get_sentences_of_pars(list_text, module='nltk'):
    ls, lp = [], []
    for text in list_text:
        sents = get_sentences(text, module)
        processed, sentences = remove_empty_sents(sents)
        if len(sentences) == 0:
            continue
        sents, prep_sents = remove_repetition(sentences, processed)
        ls.append(sents)
        lp.append(prep_sents)
    return lp, ls


def get_sentences(text, module='nltk'):
    if module == 'nltk':
        return get_sentences_nltk(text)
    elif module == 'punkt':
        return get_sentences_punkt(text)


def get_sentences_nltk(text):
    sents = tokenizer.tokenize(text)
    return sents


def get_pairwise_distance(emb):
    return pairwise_distances(emb, metric='cosine')


def get_sentences_punkt(text):
    trainer.train(text, finalize=False)
    tokenizer = PunktSentenceTokenizer(trainer.get_params())
    sents = tokenizer.tokenize(text)
    return sents


def get_paragraphs_from_doc(filename):
    with open(filename, 'r') as f:
        data = f.read()
        paragraphs = data.split('\n\n')
        return paragraphs


def get_paragraphs(text):
    paragraphs = text.split('\n\n')
    return paragraphs


def preprocess_text(text):
    # text = text.lower()
    text = re.sub(r'\d+', '', text)
    text = text.translate(str.maketrans("","" , string.punctuation))
    words = word_tokenize(text)
    all_stopwords = stopwords.words('english')
    words = [word for word in words if not word in all_stopwords]
    words = [w for w in words if w in google_model.key_to_index.keys()]
    return words


def get_pars_to_sents_dic(filename):
    pars = get_paragraphs_from_doc(filename)
    prep_pars, pars = get_sentences_of_pars(pars)

    pars_to_sents = {}
    id = 0
    for i in range(len(pars)):
        l = []
        for j in range(len(pars[i])):
            l.append(id)
            id += 1
        pars_to_sents[i] = l
    return pars_to_sents, pars, prep_pars


def get_pars_to_sents_dic_text(paragraph_sents):
    pars_to_sents = {}
    id = 0
    for i in range(len(paragraph_sents)):
        l = []
        for j in range(len(paragraph_sents[i])):
            l.append(id)
            id += 1
        pars_to_sents[i] = l
    return pars_to_sents


def get_text_data(text, module='nltk'):
    pars = get_paragraphs(text)
    prep_pars, pars = get_sentences_of_pars(pars, module)
    pars_to_sents = get_pars_to_sents_dic_text(paragraph_sents=pars)
    sentences = []
    for small_list in pars:
        for item in small_list:
            sentences.append(item)
    preprocessed = []
    for small_list in prep_pars:
        for item in small_list:
            preprocessed.append(item)
    return pars_to_sents, sentences, preprocessed


def get_sents_to_pars_dic(sents_to_par_dict):
    result = {}
    for key in sents_to_par_dict.keys():
        for i in sents_to_par_dict[key]:
            result[i] = key

    return result


def get_text(filename):
    with open(filename, 'r') as f:
        data = f.read()
    return data


def cnn_story_parser(text):
    all = re.split("\n\n@highlight\n\n", text)
    return {'article': all[0],
            'highlights': all[1:]}


def par_lengths(par_to_sents_dict):
    l = []
    for key in par_to_sents_dict.keys():
        l.append(len(par_to_sents_dict[key]))
    return l


def remove_empty_sents(sents):
    processed = []
    new_sentes = []
    for i, s in enumerate(sents):
        ps = preprocess_text(s)
        if len(ps) > 2:
            processed.append(ps)
            new_sentes.append(s)
    return processed, new_sentes


def get_cnn_text_summary(cnn_dir, cnn_filename):
    try:
        story = get_text(cnn_dir + cnn_filename)
    except:
        print('could not read file {}'.format(id))
        return '', ''
    story = cnn_story_parser(story)
    text = story['article']
    gold_summary = ". ".join(story['highlights'])
    return text, gold_summary


def timer(start, end):
    hours, rem = divmod(end - start, 3600)
    minutes, seconds = divmod(rem, 60)
    return "{:0>2}:{:0>2}:{:05.2f}".format(int(hours), int(minutes), seconds)


def remove_repetition(sentences, preprocessed_sentences):
    filtered_sentence = []
    filtered_preprocessed = []
    for i, s in enumerate(preprocessed_sentences):
        if s not in filtered_preprocessed:
            filtered_preprocessed.append(preprocessed_sentences[i])
            filtered_sentence.append(sentences[i])
    return filtered_sentence, filtered_preprocessed


def create_frequency_table(preprocessed_sents):
    freq_table = {}
    total = 0
    for sent in preprocessed_sents:
        for word in sent:
            if word in freq_table:
                freq_table[word] += 1
            else:
                freq_table[word] = 1
            total += 1
    for word in freq_table.keys():
        freq_table[word] /= total
    return freq_table

# @profile
def k_centers(distance_matrix, k):
    n = distance_matrix.shape[0]
    indicies = range(n)
    comb = combinations(indicies, k)
    comb = list(comb)
    max_distances = []
    for c in comb:
        d = distance_matrix[c, :]
        d_closest = np.min(d, axis=0)
        max_distances.append(np.max(d_closest))
    c = np.argmin(max_distances)
    return comb[c]


def remove_short_sentences_std(preprocessed_sents, sentences, n_std):
    l = [len(x) for x in preprocessed_sents]
    mean = np.mean(l)
    std = np.std(l)
    # print('mean:', mean, ', std:', std)
    if mean - n_std * std > 0:
        p = np.ceil(mean - n_std * std)
    else:
        return preprocessed_sents, sentences
        # p = mean - (n_std - 1) * std
    # print('shorter than', p, 'is removed')
    new_prep, new_sents = [] , []
    for i, s in enumerate(preprocessed_sents):
        if len(s) > p:
            new_prep.append(s)
            new_sents.append(sentences[i])
        # else:
            # print('remove', i, s)
    return new_prep, new_sents


def remove_short_sentences_percentile(preprocessed_sents, sentences, percent):
    l = [len(x) for x in preprocessed_sents]
    p = np.percentile(l, percent)
    print('shorter than', p)
    new_prep, new_sents = [] , []
    for i, s in enumerate(preprocessed_sents):
        if len(s) > p:
            new_prep.append(s)
            new_sents.append(sentences[i])
        # else:
            # print('remove', i, s)
    return new_prep, new_sents


def merge_close_sentences(embs, prep_sents, sents, threshold):
    D = pairwise_distances(embs, metric='cosine')
    merged_prep_sents = prep_sents.copy()
    merged_sents = sents.copy()
    merge = []
    for i in range(D.shape[0]):
        for j in range(i+1, D.shape[0]):
            if D[i, j] < threshold:
                merge.append((i, j))

    for i, j in merge:
        if prep_sents[j] in merged_prep_sents:
            merged_prep_sents.remove(prep_sents[j])
        if sents[j] in merged_sents:
            merged_sents.remove(sents[j])
    return merged_prep_sents, merged_sents, merge


def cleanup_sentences(embs, preprocessed_sents, sentences, threshold, n_std):
    prep_sents, sents, merged = merge_close_sentences(embs, preprocessed_sents, sentences, threshold)
    prep_sents, sents = remove_short_sentences_std(prep_sents, sents, n_std)
    # prep_sents, sents = remove_short_sentences_percentile(prep_sents, sents, percent=5)
    return prep_sents, sents, merged
