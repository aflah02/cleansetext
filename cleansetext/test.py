from pipeline import Pipeline
from steps import *
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
