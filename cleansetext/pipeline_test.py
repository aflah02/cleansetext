from cleansetext.pipeline import Pipeline
from cleansetext.steps import *

from nltk.tokenize import TweetTokenizer

def test_pipeline() -> None:
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

    assert pipeline.process(text) == ['<USER>', 'I', 'hate', 'you', 'and', 'everything', 'about', 'you', '<URL>']

    pipeline.explain(show_diffs=True)