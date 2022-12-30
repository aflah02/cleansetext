# CleanseText

NOTE: THE LIBRARY IS CURRENTLY PRERELEASE AND SEVERAL FEATURES MIGHT STILL BE BROKEN

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

# Create a pipeline with a list of preprocessing steps
pipeline = Pipeline([
    RemoveAllPunctuations(),
    RemoveAllNonAlphabeticCharacters(),
    RemoveTokensWithMajorityNonAlphabeticCharacters(),
], track_diffs=True)

# Process text
text = ['.', 'this', 'is', 'a', '.', 'test', '.', '....', '99a']
print(pipeline.process(text))

# Output:
# ['this', 'is', 'a', 'test']

pipeline.explain(show_diffs=True)

# Output:
# Step 1: Remove all punctuations from a list of words | Punctuations: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
# Diff: ['.', 'this', 'is', 'a', '.', 'test', '.', '....', '99a'] -> ['this', 'is', 'a', 'test', '....', '99a']
# Step 2: Remove all non alphabetic characters from a list of words
# Diff: ['this', 'is', 'a', 'test', '....', '99a'] -> ['this', 'is', 'a', 'test']
# Step 3: Remove tokens with majority non alphabetic characters from a list of words | Threshold: 0.5
# Diff: ['this', 'is', 'a', 'test'] -> ['this', 'is', 'a', 'test']
```
