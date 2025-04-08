# TextCleaner

A simple Python package to clean text input by:
- Removing punctuation
- Lowercasing all words
- Deduplicating
- Returning a sorted list of words

## Usage

```python
from textcleaner import clean_sentence

sentence = "Hello, hello world! Clean clean."
print(clean_sentence(sentence))
# Output: ['clean', 'hello', 'world']
```

## Running Tests

```bash
python -m unittest discover tests
```
