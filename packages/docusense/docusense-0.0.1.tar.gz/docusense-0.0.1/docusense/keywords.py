from typing import List

import nltk
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from docusense.utils import stopwords_lt


class KeywordsExtractor:
    """
    Extracting keywords by TF-IDF methodology
    """

    def __init__(self):
        nltk.download("punkt")
        nltk.download("stopwords")

    def get_keywords(self, text: str, language: str = "english", n_keywords: int = 5):
        """
        :return: Extracted n-number of keywords from text for provided question.
        """
        # Tokenize the text into individual words
        tokens = word_tokenize(text.lower())

        # Remove stopwords (common words with little semantic meaning)
        try:
            if "lithuanian" in language:
                stop_words = stopwords_lt
            else:
                stop_words = set(stopwords.words(language))
        except Exception as e:
            stop_words = set()

        filtered_tokens = [token for token in tokens if token not in stop_words]

        # Create TF-IDF vectorizer
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform([" ".join(filtered_tokens)])

        # Get the feature names (keywords)
        feature_names = vectorizer.get_feature_names_out()

        # Get the top keywords based on TF-IDF scores
        top_keywords = []
        if tfidf_matrix.shape[1] > 0:
            top_indices = tfidf_matrix.toarray()[0].argsort()[-n_keywords:][
                ::-1
            ]  # Extract top 5 keywords
            top_keywords = [feature_names[idx] for idx in top_indices]

        return top_keywords

    def __call__(self, text: str, lang: str = "english", n_keywords: int = 5) -> List:
        """
        :param text: document text for summarization.
        :param lang: a language used for stopwords. Removes unnecessary stopwords for selected language.
        :param n_keywords: Number of keywords to return.
        """
        if not text:
            raise Exception("No text provided")
        return self.get_keywords(text, lang, n_keywords)
