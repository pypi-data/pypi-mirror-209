import PyPDF2
import docx2txt


class TextReader:
    """
    Document reader class
    """

    text = ""

    def _read_pdf(self, file_path):
        with open(file_path, "rb") as file:
            reader = PyPDF2.PdfFileReader(file)
            for page in range(reader.numPages):
                self.text += reader.getPage(page).extract_text()
        return self.text

    def _read_docx(self, file_path):
        self.text = docx2txt.process(file_path)
        return self.text

    def _read_text(self, file_path):
        with open(file_path, "r") as file:
            self.text = file.read()
        return self.text

    def convert_to_text(self, file_path):
        if file_path.endswith(".pdf"):
            return self._read_pdf(file_path)
        elif file_path.endswith(".docx"):
            return self._read_docx(file_path)
        elif file_path.endswith(".txt"):
            return self._read_text(file_path)
        else:
            raise ValueError("Unsupported file format.")

    def __call__(self, file_path) -> str:
        if not file_path:
            raise Exception("No path to file provided.")
        return self.convert_to_text(file_path)
