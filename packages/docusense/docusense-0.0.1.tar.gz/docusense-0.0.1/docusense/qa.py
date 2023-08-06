from transformers import pipeline


class QAExtractor:
    """
    Class for QA related logic
    """

    model = "timpal0l/mdeberta-v3-base-squad2"
    pipe = pipeline("question-answering", model=model, framework='pt')

    def get_qa(
        self,
        text: str,
        question: str = "What are the questions?",
        max_answer_len: int = 50,
    ):
        """
        :return: Extracted answer from text for provided question.
        """
        output = self.pipe(
            question=question, context=text, top_k=3, max_answer_len=max_answer_len
        )
        return output[0]['answer']

    def __call__(
        self,
        text: str,
        question: str = "What are the questions?",
        max_answer_len: int = 50,
    ) -> str:
        """
        :param text: document text for summarization.
        :param question: Question to look for the answer in text.
        :param max_answer_len: Max length of answer.
        """
        if not text:
            raise Exception("No text provided")
        return self.get_qa(text, question, max_answer_len)
