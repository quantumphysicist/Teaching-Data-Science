# CountVectorizer & TF-IDFVectorizer

## Overview
This repository contains a Jupyter Notebook that demonstrates the use of **CountVectorizer** and **TF-IDFVectorizer** from scikit-learn to process textual data. These vectorization techniques are fundamental in Natural Language Processing (NLP) for converting raw text into numerical representations that can be used in machine learning models.

## Features
- **CountVectorizer**: Transforms a collection of text documents into a matrix of token counts.
- **TF-IDFVectorizer**: Computes the Term Frequency-Inverse Document Frequency (TF-IDF) representation of a corpus, giving higher weights to less frequent but more meaningful words.
- **Examples and Explanations**:
  - A detailed breakdown of how word counts and TF-IDF values are computed.
  - Step-by-step examples using small corpora for better understanding.
  - Mathematical derivations of TF-IDF values based on the scikit-learn documentation.

## Prerequisites
Ensure you have the following Python packages installed:

```bash
pip install numpy pandas scikit-learn matplotlib
```

## Usage
### CountVectorizer Example

```python
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

corpus = [
    'The woods are lovely, dark and deep',  
    'But I have promises to keep',   
    'And miles to go before I sleep',   
    'And miles to go before I sleep'
]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)

# Convert to DataFrame for better visualization
df = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())
print(df)
```

### TF-IDF Example

```python
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(norm=None)  # norm=None disables normalization
X = vectorizer.fit_transform(corpus)

df = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())
print(df)
```

## Understanding TF-IDF Calculation
TF-IDF values are computed using the formula:

$$\[ \text{idf}(t) = \log \left(\frac{1 + n}{1 + \text{df}(t)} \right) + 1 \]$$

Where:
- $\( n \)$ = total number of documents
- $\( \text{df}(t) \)$ = number of documents containing the term $\( t \)$

This repository includes step-by-step calculations to validate these values.

## References
- [Scikit-learn Documentation: CountVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html)
- [Scikit-learn Documentation: TfidfVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html)

## License
This project is licensed under the MIT License.

