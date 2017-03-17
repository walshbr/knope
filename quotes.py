# python 3


import nltk
from nltk import word_tokenize
import string

def read_text(file):
    """Takes a file and reads it in."""
    with open(file, 'r') as fin:
        return fin.read()


def split_text_into_sentences(text):
    """Takes a text and splits it into sentences, preserving punctuation."""
    tokenizer = nltk.load('tokenizers/punkt/{0}.pickle'.format('english'))
    return tokenizer.tokenize(text)


def split_sentences_into_tokens(sentence):
    """Takes a sentence and splits it into tokens."""
    return word_tokenize(sentence)


def ann_test(tokens):
    """Takes a tokenized sentence and tests if it is an Ann adjective"""
    if tokens[0] == "Ann" and tokens[1] == ',' and tokens[2] == 'you':
        return True


def untokenize(sent_tokens):
    return "".join([" " + i if not i.startswith("'") and
                    i not in string.punctuation else i for
                    i in sent_tokens]).strip()


def main():
    transcript = "transcript.txt"
    text = read_text(transcript)
    sentences = split_text_into_sentences(text)

    tokenized_sentences = [split_sentences_into_tokens(sentence)
                           for sentence in sentences]
    ann_sentences = [sent_tokens for sent_tokens in
                     tokenized_sentences if ann_test(sent_tokens)]
    results = [untokenize(sent) for sent in ann_sentences]
    print(results)


if __name__ == '__main__':
    main()
