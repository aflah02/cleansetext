from pipeline import Pipeline
from steps import *

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
