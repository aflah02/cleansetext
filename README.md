# TextHelp

This is a simple library to help you clean your textual data.

## Why do I need this?

Honestly there are several packages out there which do similar things, but they've never really worked well for my use cases or don't have all the features I need. So I decided to make my own.

The API design is made to be readable, and I don't hesitate to create functions even for trivial tasks as they make reaching the goal easier.

## Sample usage

```
from pipeline import Pipeline
from steps import *

# Create a pipeline with a list of preprocessing steps
pipeline = Pipeline([
    RemoveAllPunctuations(),
    RemoveAllNonAlphabeticCharacters(),
    RemoveAllNonAlphabeticCharacters(),
    RemoveTokensWithMajorityNonAlphabeticCharacters(),
])

# Process text
text = ['.', 'this', 'is', 'a', '.', 'test', '.', '....', '99a']
print(pipeline.process(text))
print(pipeline.explain())
```