# CleanseText

![](https://github.com/aflah02/cleansetext/actions/workflows/python-publish.yml/badge.svg)
![](https://github.com/aflah02/cleansetext/actions/workflows/python-package.yml/badge.svg)

This is a simple library to help you clean your textual data.

## Why do I need this?

Honestly there are several packages out there which do similar things, but they've never really worked well for my use cases or don't have all the features I need. So I decided to make my own.

The API design is made to be readable, and I don't hesitate to create functions even for trivial tasks as they make reaching the goal easier.

## How to Install?

`pip install cleansetext`

## Sample usage

```
from cleansetext.pipeline import Pipeline
from cleansetext.steps import *
from nltk.tokenize import TweetTokenizer
tk = TweetTokenizer()

# Create a pipeline with a list of preprocessing steps
pipeline = Pipeline([
    RemoveEmojis(),
    RemoveAllPunctuations(),
    RemoveTokensWithOnlyPunctuations(),
    ReplaceURLsandHTMLTags(),
    ReplaceUsernames(),
    RemoveWhiteSpaceOrChunksOfWhiteSpace()
], track_diffs=True)

# Process text
text = "@Mary I hate you    and everything about you ...... 🎉🎉 google.com"
text = tk.tokenize(text)

print(text)
# Output: ['@Mary', 'I', 'hate', 'you', 'and', 'everything', 'about', 'you', '...', '🎉', '🎉', 'google.com']

print(pipeline.process(text))

# Output:
# ['<USER>', 'I', 'hate', 'you', 'and', 'everything', 'about', 'you', '<URL>']

pipeline.explain(show_diffs=True)

# Output:
# Step 1: Remove emojis from text | Language: en
# Diff: ['@Mary', 'I', 'hate', 'you', 'and', 'everything', 'about', 'you', '...', '🎉', '🎉', 'google.com'] -> ['@Mary', 'I', 'hate', 'you', 'and', 'everything', 'about', 'you', '...', 'google.com']
# Step 2: Remove all punctuations from a list of words | Punctuations: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
# Diff: ['@Mary', 'I', 'hate', 'you', 'and', 'everything', 'about', 'you', '...', 'google.com'] -> ['@Mary', 'I', 'hate', 'you', 'and', 'everything', 'about', 'you', '...', 'google.com']
# Step 3: Remove tokens with only punctuations from a list of words | Punctuations: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
# Diff: ['@Mary', 'I', 'hate', 'you', 'and', 'everything', 'about', 'you', '...', 'google.com'] -> ['@Mary', 'I', 'hate', 'you', 'and', 'everything', 'about', 'you', 'google.com']
# Step 4: Remove URLs and HTML tags from a sentence | Replace with: <URL>
# Diff: ['@Mary', 'I', 'hate', 'you', 'and', 'everything', 'about', 'you', 'google.com'] -> ['@Mary', 'I', 'hate', 'you', 'and', 'everything', 'about', 'you', '<URL>']
# Step 5: Remove usernames from a sentence | Replace with: <USER>
# Diff: ['@Mary', 'I', 'hate', 'you', 'and', 'everything', 'about', 'you', '<URL>'] -> ['<USER>', 'I', 'hate', 'you', 'and', 'everything', 'about', 'you', '<URL>']
# Step 6: Remove whitespace from a sentence or chunks of whitespace
# Diff: ['<USER>', 'I', 'hate', 'you', 'and', 'everything', 'about', 'you', '<URL>'] -> ['<USER>', 'I', 'hate', 'you', 'and', 'everything', 'about', 'you', '<URL>']

```
