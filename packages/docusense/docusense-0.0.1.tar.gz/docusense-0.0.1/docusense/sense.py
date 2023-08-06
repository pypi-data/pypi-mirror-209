from typing import Dict

from docusense.keywords import KeywordsExtractor
from docusense.process_doc import TextReader
from docusense.qa import QAExtractor
from docusense.summary import Summarizer


class SenseExtractor:
    """
    A Document Sense class combining summary, question and answers and top_keywords
    """

    def __init__(self):
        """
        Initiation of classes to load the transformer models.
        """
        self.reader = TextReader()
        self.summarizer = Summarizer()
        self.qa_extractor = QAExtractor()
        self.keywords_extractor = KeywordsExtractor()

    def run(
        self,
        text: str,
        lang: str = "english",
        question: str = "What are the questions?",
        min_length: int = 50,
        max_length: int = 150,
        max_answer_len: int = 50,
        n_keywords: int = 5,
    ):
        output = dict()
        output["summary"] = self.summarizer(text, min_length, max_length)
        output["answer"] = self.qa_extractor(text, question, max_answer_len)
        output["keywords"] = self.keywords_extractor(text, lang, n_keywords)
        return output

    def __call__(
        self,
        path: str,
        text: str,
        lang: str = "english",
        question: str = "What are the questions?",
        min_length: int = 50,
        max_length: int = 150,
        max_answer_len: int = 50,
        n_keywords: int = 5,
    ) -> Dict:
        """
        :param path: document text for summarization.
        :param text: document text for summarization.
        :param lang: a language used for stopwords. Removes unnecessary stopwords for selected language.
        :param question: Question to look for the answer in text.
        :param min_length: Min length of generated summary.
        :param max_length: Max length of generated summary.
        :param max_answer_len: Max length of answer.
        :param n_keywords: Number of keywords to return.
        """
        if path:
            text = self.reader(path)

        if not text:
            raise Exception("Path or text must be provided.")

        return self.run(
            text, lang, question, min_length, max_length, max_answer_len, n_keywords
        )
