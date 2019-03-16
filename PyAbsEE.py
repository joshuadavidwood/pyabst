import nltk
from collections import Counter
from nltk.corpus import stopwords
import spacy
import re
import en_core_web_sm
nlp = en_core_web_sm.load()



def PyAbst(text, target_words=[], word_weight=1):
    '''A function which returns the most important sentences from a list of sentences using common word weighting.'''

    doc = nlp(text) # Use SpaCy library to extract entities.
    target_entities = ([i.text for i in doc.ents if i.label_ != 'CARDINAL' and i.label_ != 'ORDINAL' and i.label_ != 'DATE']) # Remove CARDINAL and ORDINAL entities.
    target_entities = [i.split() for i in target_entities] # Split entities
    target_entities = list(set([item.lower() for sublist in target_entities for item in sublist]))
    entity_weighting = 4
    print(target_entities)

    # Define StopWords corpus.
    new_stopwords = ['said', 'so']  # Additional StopWords.
    stopwords = nltk.corpus.stopwords.words('english')
    stopwords = stopwords + new_stopwords


    # Evaluate upper, lower and capitalised combinations of target words.
    target_words_combinations = []
    for i in target_words:
        upper = i.upper() # Evaluate upper.
        target_words_combinations.append(upper)
        lower = i.lower() # Evaluate lower.
        target_words_combinations.append(lower)
        capitalise = i.capitalize() # Evaluate capitalised.
        target_words_combinations.append(capitalise)


    # Unprocessed text.
    input_text = text # Defined here to evaluate reduction percentage.
    text = text.replace('?', '.') # Replace ? character with .
    text = text.replace('!', '.') # Replace ! character with .
    text = [x.split('.') for x in text.split('.')]  # Use period to create list of lists with period separation.
    text = [[x.lstrip() for x in listx] for listx in text]  # Remove heading whitespace text for each list element.
    text = [[x + '.' for x in listx] for listx in text]  # Add a period at the end of each list.
    text = text[:-1]  # Remove list containing [.] at the end of list of lists.

    processed_text = [] #NOTE: This is a duplicate of unprocessed text with additional processing methods.
    for i in text:
        i = [re.sub(r'[^\w\s]', '', j).lower() for j in i]  # Remove punctuation and lower all words.
        i = [nltk.word_tokenize(j) for j in i]  # Tokenize words using NLTK.
        i = [item for sublist in i for item in sublist]  # Flatten the list of lists.
        i = [j for j in i if j not in stopwords]  # Remove StopWords using NLTK.
        processed_text.append(i)


    sentences_unpacked = [item for sublist in processed_text for item in sublist] # Unpacked list of lists.


    def replace_list_dict(list, dictionary):
        '''A function which replaces list elements with corresponding dictionary key-values.'''
        replaced = [(item, Counter(sentences_unpacked).get(item, item)) for item in list]
        return replaced


    sentences_list = []
    for i in processed_text: # Converts list (word) element to (word, frequency).
        sentences_list.append(replace_list_dict(i, Counter(sentences_unpacked)))


    weighted_sentences_list = []
    for i in sentences_list:  # Replaces list (word, frequency) element with (word, frequency * weight) if word is in target list.
        weighted_sentences_list.append([(t[0], t[1] * word_weight) if t[0] in target_words_combinations else (t[0], t[1] * entity_weighting) if t[0] in target_entities else (t[0], t[1]) for t in i])
    print(weighted_sentences_list)


    sentences_list_scores = []
    for i in weighted_sentences_list:
        sum_score = sum(x[1] for x in i) # Evalute the sum of frequency for each sentence (list within list of lists).
        sentences_list_scores.append(sum_score) # Evaluate the sum of frequencies for each sentence.


    sentences_length = []
    for i in processed_text:
        sentence_length = len(i) # Evaluate how many words are in each sentence.
        sentences_length.append(sentence_length)


    weighted_scores = [(x, x//y) for x, y in zip(sentences_list_scores, sentences_length)] # Evaluate (score, weighted score).
    index = int(len(processed_text) * 0.4) # Evaluate fraction of sentences to return.
    reduced_indexes = sorted((sorted(range(len(sentences_list_scores)), key=lambda i: sentences_list_scores[i])[-index:]))


    reduced_text = list(text[i] for i in reduced_indexes) # Only return the sentences with index in reduced_indexes.
    reduced_text = [item for sublist in reduced_text for item in sublist] # Unpacked list of lists.
    reduced_text = ' '.join(reduced_text)


    # Evaluate text reduction percentage.
    original_length = len(input_text)
    reduced_length = len(reduced_text)
    percentage_diff = str(int(((original_length - reduced_length) / original_length) * 100)) + '%'


    return reduced_text, percentage_diff



#TESTING CODE
#print(PyAbs(input_text, ['Japan'], -200)[0]) #NOTE: Suppressed Japan.
#print(PyAbs(input_text, ['Japan'], -200)[1]) #NOTE: Suppressed Japan.

#print(PyAbs(input_text, ['number'], 200)[0]) #NOTE: Boosted number.
#print(PyAbs(input_text, ['number'], 200)[1]) #NOTE: Boosted number.

#print(PyAbs(input_text, [], 1)[0]) #Set these as default values
print(PyAbs(input_text, [], 1)[1]) #Set these as default values
