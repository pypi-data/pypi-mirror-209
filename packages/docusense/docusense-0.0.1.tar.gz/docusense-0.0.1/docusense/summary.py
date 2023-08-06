from transformers import MBartForConditionalGeneration, MBart50TokenizerFast


class Summarizer:
    """
    Extracting summary of selected text.
    """

    model = MBartForConditionalGeneration.from_pretrained("facebook/mbart-large-50")
    tokenizer = MBart50TokenizerFast.from_pretrained("facebook/mbart-large-50")

    def get_summary(self, text, min_length: int = 50, max_length: int = 150):
        """
        :return: Summary of text
        """
        input_tokens = self.tokenizer.batch_encode_plus(
            [text], return_tensors="pt", max_length=1024, truncation=True
        )["input_ids"]
        encoded_ids = self.model.generate(
            input_tokens,
            num_beams=2,
            min_length=min_length,
            max_length=max_length,
            do_sample=False,
        )
        summary = self.tokenizer.decode(encoded_ids.squeeze(), skip_special_tokens=True)
        return summary

    def __call__(self, text: str, min_length: int = 50, max_length: int = 150) -> str:
        """
        :param text: document text for summarization.
        :param min_length: Min length of generated summary.
        :param max_length: Max length of generated summary.
        """
        if not text:
            raise Exception("No text provided")
        return self.get_summary(text, min_length, max_length)
