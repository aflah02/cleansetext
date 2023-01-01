from cleansetext.steps import *

def test_stopwords_removed():
    remover = StopWordsRemover()
    text = ['this', 'is', 'a', 'test']
    assert remover.process(text) == ['test']

def test_ignore_case_stopwords():
    remover = StopWordsRemover(ignore_case=True)
    text = ['This', 'is', 'a', 'test']
    assert remover.process(text) == ['test']

def test_ignored_stopwords():
    remover = StopWordsRemover(ignored_stopwords=['is'])
    text = ['this', 'is', 'a', 'test']
    assert remover.process(text) == ['is', 'test']

def test_include_stopwords():
    remover = StopWordsRemover(include_stopwords=['not'])
    text = ['this', 'is', 'not', 'a', 'test']
    assert remover.process(text) == ['test']

def test_language_stopwords():
    remover = StopWordsRemover(language='spanish')
    text = ['Este', 'es', 'un', 'test']
    assert remover.process(text) == ['test']

def test_explain_stopwords():
    remover = StopWordsRemover(ignore_case=True, ignored_stopwords=['is'], include_stopwords=['not'], language='spanish')
    expected_output = "Remove stopwords from text | Ignore case: True | Ignored stopwords: {'is'} | Language: spanish"
    assert remover.explain() == expected_output

## EmojiToText

def test_emojis_replaced_EmojiToText():
    emoji_to_text = EmojiToText()
    text = ['this', 'is', 'a', 'test', '🤔']
    assert emoji_to_text.process(text) == ['this', 'is', 'a', 'test', ':thinking_face:']

def test_language_emoji_replaced_EmojiToText():
    emoji_to_text = EmojiToText(language='es')
    text = ['this', 'is', 'a', 'test', '🤔']
    assert emoji_to_text.process(text) == ['this', 'is', 'a', 'test', ':cara_pensativa:']

def test_explain_emoji_replaced_EmojiToText():
    emoji_to_text = EmojiToText(language='es')
    expected_output = "Replace emojis with text | Language: es"
    assert emoji_to_text.explain() == expected_output

## TextToEmoji

def test_text_replaced_TextToEmoji():
    text_to_emoji = TextToEmoji()
    text = ['this', 'is', 'a', 'test', ':thinking_face:']
    assert text_to_emoji.process(text) == ['this', 'is', 'a', 'test', '🤔']

def test_language_text_replaced_TextToEmoji():
    text_to_emoji = TextToEmoji(language='es')
    text = ['this', 'is', 'a', 'test', ':cara_pensativa:']
    assert text_to_emoji.process(text) == ['this', 'is', 'a', 'test', '🤔']

def test_explain_text_replaced_TextToEmoji():
    text_to_emoji = TextToEmoji(language='es')
    expected_output = "Replace text with emojis | Language: es"
    assert text_to_emoji.explain() == expected_output

## RemoveEmojis

def test_emojis_removed_RemoveEmojis():
    remover = RemoveEmojis()
    text = ['this', 'is', 'a', 'test', '🤔']
    assert remover.process(text) == ['this', 'is', 'a', 'test']

def test_ignored_emojis_RemoveEmojis():
    remover = RemoveEmojis(ignored_emojis=['🤔'])
    text = ['this', 'is', 'a', 'test', '🤔']
    assert remover.process(text) == ['this', 'is', 'a', 'test', '🤔']

def test_explain_RemoveEmojis():
    remover = RemoveEmojis()
    expected_output = "Remove emojis from text"
    assert remover.explain() == expected_output

## RemoveAllNonAlphabetOnlyWords

def test_non_alphabet_only_words_removed_RemoveAllNonAlphabetOnlyWords():
    remover = RemoveAllNonAlphabetOnlyWords()
    text = ['.', 'this', 'is', 'a', 'test', '9', '🤔']
    assert remover.process(text) == ['this', 'is', 'a', 'test']

def test_explain_RemoveAllNonAlphabetOnlyWords():
    remover = RemoveAllNonAlphabetOnlyWords()
    expected_output = "Remove all non alphabet only words from a list of words"
    assert remover.explain() == expected_output

## RemoveAllNonAlphanumericOnlyWords

def test_non_alphanumeric_only_words_removed_RemoveAllNonAlphanumericOnlyWords():
    remover = RemoveAllNonAlphanumericOnlyWords()
    text = ['.', 'this', 'is', 'a', 'test', '9', '🤔']
    assert remover.process(text) == ['this', 'is', 'a', 'test', '9']

def test_explain_RemoveAllNonAlphanumericOnlyWords():
    remover = RemoveAllNonAlphanumericOnlyWords()
    expected_output = "Remove all non alphanumeric characters from a list of words"
    assert remover.explain() == expected_output

## RemoveEmojis

def test_emojis_removed_RemoveEmojis():
    remover = RemoveEmojis()
    text = ['this', 'is', 'a', 'test', '🤔']
    assert remover.process(text) == ['this', 'is', 'a', 'test']

def test_ignored_emojis_RemoveEmojis():
    remover = RemoveEmojis(ignored_emojis=['🤔'])
    text = ['this', 'is', 'a', 'test', '🤔']
    assert remover.process(text) == ['this', 'is', 'a', 'test', '🤔']

def test_explain_RemoveEmojis():
    remover = RemoveEmojis()
    expected_output = "Remove emojis from text"
    assert remover.explain() == expected_output

## RemovePrecedingAndTrailingPunctuations

def test_punctuations_removed_RemovePrecedingAndTrailingPunctuations():
    remover = RemovePrecedingAndTrailingPunctuations()
    text = ['.', 'this', 'is', 'a', 'test', '.', '.']
    assert remover.process(text) == ['this', 'is', 'a', 'test']

def test_ignore_starting_punctuations_RemovePrecedingAndTrailingPunctuations():
    remover = RemovePrecedingAndTrailingPunctuations(ignore_starting_punctuations=True)
    text = ['.', 'this', 'is', 'a', 'test', '.', '.']
    assert remover.process(text) == ['.', 'this', 'is', 'a', 'test']

def test_ignore_ending_punctuations_RemovePrecedingAndTrailingPunctuations():
    remover = RemovePrecedingAndTrailingPunctuations(ignore_ending_punctuations=True)
    text = ['.', 'this', 'is', 'a', 'test', '.', '.']
    assert remover.process(text) == ['this', 'is', 'a', 'test', '.', '.']

def test_custom_punctuations_RemovePrecedingAndTrailingPunctuations():
    remover = RemovePrecedingAndTrailingPunctuations(punctuations='#')
    text = ['#', 'this', 'is', 'a', 'test', '#', '#']
    assert remover.process(text) == ['this', 'is', 'a', 'test']

def test_explain_RemovePrecedingAndTrailingPunctuations():
    remover = RemovePrecedingAndTrailingPunctuations(ignore_starting_punctuations=True)
    expected_output = """Remove punctuations from the beginning and end of a word | Punctuations: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ | Ignore starting punctuations: True | Ignore ending punctuations: False"""
    assert remover.explain() == expected_output

## RemoveAllPunctuations

def test_punctuations_removed_RemoveAllPunctuations():
    remover = RemoveAllPunctuations()
    text = ['.', 'this', 'is', 'a', '.', 'test', '.', '.']
    assert remover.process(text) == ['this', 'is', 'a', 'test']

def test_custom_punctuations_RemoveAllPunctuations():
    remover = RemoveAllPunctuations(punctuations='#')
    text = ['#', 'this', 'is', 'a', '#', 'test', '#', '#']
    assert remover.process(text) == ['this', 'is', 'a', 'test']

def test_explain_RemoveAllPunctuations():
    remover = RemoveAllPunctuations()
    expected_output = """Remove all punctuations from a list of words | Punctuations: !"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"""
    assert remover.explain() == expected_output

## RemoveAllNonNumericOnlyWords

def test_non_numeric_characters_removed_RemoveAllNonNumericOnlyWords():
    remover = RemoveAllNonNumericOnlyWords()
    text = ['.', 'this', 'is', 'a', 'test', '9', '🤔']
    assert remover.process(text) == ['9']

def test_no_numeric_characters_RemoveAllNonNumericOnlyWords():
    remover = RemoveAllNonNumericOnlyWords()
    text = ['.', 'this', 'is', 'a', 'test', '🤔']
    assert remover.process(text) == []

def test_explain_RemoveAllNonNumericOnlyWords():
    remover = RemoveAllNonNumericOnlyWords()
    expected_output = "Remove all non numeric only words from a list of words"
    assert remover.explain() == expected_output

## RemoveTokensWithOnlyPunctuations

def test_tokens_with_only_punctuations_removed_RemoveTokensWithOnlyPunctuations():
    remover = RemoveTokensWithOnlyPunctuations()
    text = ['.(', 'this', 'is', 'a', 'test', '?.', '....']
    assert remover.process(text) == ['this', 'is', 'a', 'test']

def test_only_punctuations_RemoveTokensWithOnlyPunctuations():
    remover = RemoveTokensWithOnlyPunctuations()
    text = ['....', '?!', '...']
    assert remover.process(text) == []

def test_explain_RemoveTokensWithOnlyPunctuations():
    remover = RemoveTokensWithOnlyPunctuations()
    expected_output = """Remove tokens with only punctuations from a list of words | Punctuations: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
    assert remover.explain() == expected_output

## RemoveTokensWithMajorityNonAlphabeticCharacters

def test_tokens_with_majority_non_alphabetic_characters_removed_RemoveTokensWithMajorityNonAlphabeticCharacters():
    remover = RemoveTokensWithMajorityNonAlphabeticCharacters()
    text = ['.(', 'this', 'is', 'a', 'test', '?.', '....']
    assert remover.process(text) == ['this', 'is', 'a', 'test']

def test_only_non_alphabetic_characters_RemoveTokensWithMajorityNonAlphabeticCharacters():
    remover = RemoveTokensWithMajorityNonAlphabeticCharacters()
    text = ['....', '?!', '...']
    assert remover.process(text) == []

def test_threshold_RemoveTokensWithMajorityNonAlphabeticCharacters():
    remover = RemoveTokensWithMajorityNonAlphabeticCharacters(threshold=0.9)
    text = ['....', '?!', '.aaaa']
    assert remover.process(text) == ['.aaaa']

def test_explain_RemoveTokensWithMajorityNonAlphabeticCharacters():
    remover = RemoveTokensWithMajorityNonAlphabeticCharacters()
    expected_output = "Remove tokens with majority non alphabetic characters from a list of words | Threshold: 0.1"
    assert remover.explain() == expected_output

## ReplaceURLsandHTMLTags

def test_process_ReplaceURLsandHTMLTags():
    remover = ReplaceURLsandHTMLTags()
    assert remover.process(['this', 'is', 'a', 'test', 'google.com']) == ['this', 'is', 'a', 'test', '<URL>']
    assert remover.process(['this', 'is', 'a', 'test', 'https://www.google.com']) == ['this', 'is', 'a', 'test', '<URL>']
    assert remover.process(['this', 'is', 'a', 'test', '&lt;']) == ['this', 'is', 'a', 'test', '<URL>']
    assert remover.process(['this', 'is', 'a', 'test', '&amp;']) == ['this', 'is', 'a', 'test', '<URL>']
    assert remover.process(['this', 'is', 'a', 'test', '&quot;']) == ['this', 'is', 'a', 'test', '<URL>']

def test_explain_ReplaceURLsandHTMLTags():
    remover = ReplaceURLsandHTMLTags()
    assert remover.explain() == "Remove URLs and HTML tags from a sentence | Replace with: <URL>"

## ReplaceUsernames

def test_process_ReplaceUsernames():
    remover = ReplaceUsernames()
    assert remover.process(['this', 'is', 'a', 'test', '@user']) == ['this', 'is', 'a', 'test', '<USER>']
    assert remover.process(['this', 'is', 'a', 'test', '@username123']) == ['this', 'is', 'a', 'test', '<USER>']
    assert remover.process(['this', 'is', 'a', 'test', '@USERNAME123']) == ['this', 'is', 'a', 'test', '<USER>']
    assert remover.process(['this', 'is', 'a', 'test', '@UsErNaMe123']) == ['this', 'is', 'a', 'test', '<USER>']
    assert remover.process(['this', 'is', 'a', 'test', 'user@domain.com']) == ['this', 'is', 'a', 'test', 'user@domain.com']

def test_explain_ReplaceUsernames():
    remover = ReplaceUsernames()
    assert remover.explain() == "Remove usernames from a sentence | Replace with: <USER>"

## RemoveUnicode

def test_process_RemoveUnicode():
    remover = RemoveUnicode(unicode_below=10, unicode_above=200)
    assert remover.process(['this', 'is', 'a', 'test', '🤔']) == ['this', 'is', 'a', 'test', '']

def test_explain_RemoveUnicode():
    remover = RemoveUnicode(unicode_below=10, unicode_above=200)
    assert remover.explain() == "Remove unicode characters from a sentence | Unicode below: 10 | Unicode above: 200 | Remove unicode: []"

def test_unicode_below_RemoveUnicode():
    remover = RemoveUnicode(unicode_below=10)
    assert remover.process(['this', 'is', 'a', 'test', '🤔']) == ['this', 'is', 'a', 'test', '🤔']

def test_unicode_above_RemoveUnicode():
    remover = RemoveUnicode(unicode_above=300)
    assert remover.process(['this', 'is', 'a', 'test', '🤔']) == ['this', 'is', 'a', 'test', '']

## RemoveWhiteSpaceOrChunksOfWhiteSpace

def test_process_RemoveWhiteSpaceOrChunksOfWhiteSpace():
    remover = RemoveWhiteSpaceOrChunksOfWhiteSpace()
    assert remover.process(['this', 'is', 'a', ' ', 'test', '     ']) == ['this', 'is', 'a', 'test']
    assert remover.process(['this', 'is', 'a', ' ', 'test', '     ', ' ', ' ', ' ', ' ']) == ['this', 'is', 'a', 'test']
    assert remover.process(['this', 'is', 'a', ' ', 'test', '     ', 'word']) == ['this', 'is', 'a', 'test', 'word']
    assert remover.process(['this', 'is', 'a', ' ', 'test', '     ', 'word', ' ', ' ', ' ', ' ']) == ['this', 'is', 'a', 'test', 'word']
    assert remover.process([' ', ' ', ' ', ' ', ' ', 'this', 'is', 'a', ' ', 'test', '     ', 'word', ' ', ' ', ' ', ' ']) == ['this', 'is', 'a', 'test', 'word']

def test_explain_RemoveWhiteSpaceOrChunksOfWhiteSpace():
    remover = RemoveWhiteSpaceOrChunksOfWhiteSpace()
    assert remover.explain() == "Remove whitespace from a sentence or chunks of whitespace"