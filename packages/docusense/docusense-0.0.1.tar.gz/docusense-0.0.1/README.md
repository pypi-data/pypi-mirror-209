docusense
======
A python library for extracting main logic from document using NLP transformers and stop words.
With multilingual transformers the extraction process should work well enough on many types of documents.

The purpose of this library is to extract main logical sense from documents without needing to open them.


Features
---
- summary extraction
- questions & answers from the document
- strongest keywords from document

Setup
---
Install using pip
```bash
pip install docusense
```

Terminal usages
---
### Possible parameters
- path: document text for summarization.
- text: document text for summarization.
- lang: a language used for stopwords. Removes unnecessary stopwords for selected language.
- question: Question to look for the answer in text.
- min_length: Min length of generated summary.
- max_length: Max length of generated summary.
- max_answer_len: Max length of answer.
- n_keywords: Number of keywords to return.

### Simple case
Logging summary, answer to asked question and keywords.
```bash
python extract.py --path "path/to/file"
```

Examples as python code
---
### Simple case
```python
from docusense.sense import SenseExtractor

text = """
Good evening,
Carriers constantly violate the passenger and baggage transport rules.
In the evenings from 21:00 to 24:00 drivers are specially late to leave
around the ring for 3-4 minutes (all this time the buses are standing still in the ring with the engines running,
at the same time creating additional air and noise pollution close to residential houses in the evenings
and during the night).
Also, some buses often arrive a few minutes earlier than indicated
in the schedule. Apparently, the transporters live and work in a parallel world, somewhere at night
traffic jams occur in the district.
The company "Communication Services" has been informing about violations for several months, but
does not take any action, although it is required to carry out the control of public transport carriers and
ensure compliance with passenger and baggage regulations.
The director of the municipal administration also does not carry out any control, rules 3
point - To instruct the Director of Administration to control how this is carried out
solution.
Please provide an answer: why are the same violations repeated every night and how
it is ensured that the carriers comply with the passenger and baggage transport rules.
"""

extractor = SenseExtractor()
output = extractor(text=text)

```

### Divided use
You can use each part of the extractor separate.

#### Summarizer
```python

text = """
Good evening,
Carriers constantly violate the passenger and baggage transport rules.
In the evenings from 21:00 to 24:00 drivers are specially late to leave
around the ring for 3-4 minutes (all this time the buses are standing still in the ring with the engines running,
at the same time creating additional air and noise pollution close to residential houses in the evenings
and during the night).
Also, some buses often arrive a few minutes earlier than indicated
in the schedule. Apparently, the transporters live and work in a parallel world, somewhere at night
traffic jams occur in the district.
The company "Communication Services" has been informing about violations for several months, but
does not take any action, although it is required to carry out the control of public transport carriers and
ensure compliance with passenger and baggage regulations.
The director of the municipal administration also does not carry out any control, rules 3
point - To instruct the Director of Administration to control how this is carried out
solution.
Please provide an answer: why are the same violations repeated every night and how
it is ensured that the carriers comply with the passenger and baggage transport rules.
"""

#summarizer part
from docusense.summary import Summarizer
summarizer = Summarizer()
summary = summarizer(text, min_length=20)

#questions and answers
from docusense.qa import QAExtractor
qa_extractor = QAExtractor()
answer = qa_extractor(text, question="What is the question in the text?")

#keywords
from docusense.keywords import KeywordsExtractor
keywords_extractor = KeywordsExtractor()
keywords = keywords_extractor(text, lang='english', n_keywords=3)

```


Development
---
1. Install poetry https://python-poetry.org/docs/#installation depending on your machine
2. `poetry install`
