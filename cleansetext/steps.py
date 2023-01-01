import nltk
import emoji
import re
import string

class StopWordsRemover:
    """
    A class to remove stopwords from a text.

    Expected input: list of words
    Expected output: list of words

    Example:
    >>> remover = StopWordsRemover()
    >>> remover.process(['this', 'is', 'a', 'test'])
    ['test']
    """
    def __init__(self, ignore_case=True, ignored_stopwords=None, include_stopwords=None, language='english'):
        nltk.download('stopwords')
        self.stopwords = set(nltk.corpus.stopwords.words(language))
        self.ignore_case = ignore_case
        self.ignored_stopwords = set(ignored_stopwords) if ignored_stopwords else set()
        self.include_stopwords = set(include_stopwords) if include_stopwords else set()
        self.all_stopwords = self.stopwords.union(set(self.include_stopwords)) if self.include_stopwords else self.stopwords
        self.language = language

    def process(self, text):
        if self.ignore_case:
            text_copy = [word.lower() for word in text]
        new_words = []
        for word in text_copy:
            if word in self.all_stopwords:
                if word not in self.ignored_stopwords:
                    continue
            new_words.append(word)
        return new_words

    def explain(self):
        return f"Remove stopwords from text | Ignore case: {self.ignore_case} | Ignored stopwords: {self.ignored_stopwords} | Language: {self.language}"

class EmojiToText:
    """
    A class to remove emojis from a text.

    Expected input: list of words
    Expected output: list of words

    Example:
    >>> emoji_to_text = EmojiToText()
    >>> emoji_to_text.process(['this', 'is', 'a', 'test', '🤔'])
    ['this', 'is', 'a', 'test', ':thinking_face:']
    """
    def __init__(self, language='en'):
        self.language = language

    def process(self, text):
        return [emoji.demojize(word, language=self.language) if emoji.demojize(word, language=self.language) != word else word for word in text]

    def explain(self):
        return f"Replace emojis with text | Language: {self.language}"

class TextToEmoji:
    """
    A class to replace text with emojis.

    Expected input: list of words
    Expected output: list of words

    Example:
    >>> text_to_emoji = TextToEmoji()
    >>> text_to_emoji.process(['this', 'is', 'a', 'test', ':thinking_face:'])
    ['this', 'is', 'a', 'test', '🤔']
    """
    def __init__(self, language='en'):
        self.language = language

    def process(self, text):
        return [emoji.emojize(word, language=self.language) if emoji.emojize(word, language=self.language) != word else word for word in text]

    def explain(self):
        return f"Replace text with emojis | Language: {self.language}"

class RemoveEmojis:
    """
    A class to remove emojis from a text.

    Expected input: list of words
    Expected output: list of words

    Example:
    >>> remover = RemoveEmojis()
    >>> remover.process(['this', 'is', 'a', 'test', '🤔'])
    ['this', 'is', 'a', 'test']
    """
    def __init__(self, ignored_emojis=None):
        self.ignored_emojis = ignored_emojis

    def process(self, text):
        if self.ignored_emojis is not None:
            self.ignored_emojis = set(self.ignored_emojis)
        else:
            self.ignored_emojis = set()
        
        new_text = []
        for word in text:
            if emoji.demojize(word) != word and word not in self.ignored_emojis:
                continue
            new_text.append(word)
        return new_text

    def explain(self):
        return f"Remove emojis from text"

class RemovePrecedingAndTrailingPunctuations:
    """
    A class to remove punctuations from the beginning and end of a list of words.

    Expected input: list of words
    Expected output: list of words

    Example:
    >>> remover = RemovePrecedingAndTrailingPunctuations()
    >>> remover.process(['.', 'this', 'is', 'a', 'test', '.', '.'])
    ['this', 'is', 'a', 'test']
    """
    def __init__(self, punctuations='!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~', ignore_starting_punctuations=False, ignore_ending_punctuations=False):
        self.punctuations = punctuations
        self.ignore_starting_punctuations = ignore_starting_punctuations
        self.ignore_ending_punctuations = ignore_ending_punctuations

    def process(self, text):
        startPointer = 0
        endPointer = len(text) - 1
        if not self.ignore_starting_punctuations:
            while text[startPointer] in self.punctuations:
                startPointer += 1
        if not self.ignore_ending_punctuations:
            while text[endPointer] in self.punctuations:
                endPointer -= 1
        if startPointer > endPointer:
            return []
        return text[startPointer:endPointer+1] 

    def explain(self):
        return f"Remove punctuations from the beginning and end of a word | Punctuations: {self.punctuations} | Ignore starting punctuations: {self.ignore_starting_punctuations} | Ignore ending punctuations: {self.ignore_ending_punctuations}"

class RemoveAllPunctuations:
    """
    A class to remove all punctuations from a list of words.

    Expected input: list of words
    Expected output: list of words

    Example:
    >>> remover = RemoveAllPunctuations()
    >>> remover.process(['.', 'this', 'is', 'a', '.', 'test', '.', '.'])
    ['this', 'is', 'a', 'test']
    """
    def __init__(self, punctuations='!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'):
        self.punctuations = punctuations

    def process(self, text):
        return [word for word in text if word not in self.punctuations]

    def explain(self):
        return f"Remove all punctuations from a list of words | Punctuations: {self.punctuations}"

class RemoveAllNonAlphabetOnlyWords:
    """
    A class to remove all non alphabet only words from a list of words.

    Expected input: list of words
    Expected output: list of words

    Example:
    >>> remover = RemoveAllNonAlphabetOnlyWords()
    >>> remover.process(['.', 'this', 'is', 'a', 'test', '9', '🤔'])
    ['this', 'is', 'a', 'test', '9]
    """
    def __init__(self):
        pass

    def process(self, text):
        new_text = []
        for word in text:
            if word.isalpha():
                new_text.append(word)
        return new_text

    def explain(self):
        return "Remove all non alphabet only words from a list of words"

class RemoveAllNonAlphanumericOnlyWords:
    """
    A class to remove all non alphanumeric only words from a list of words.

    Expected input: list of words
    Expected output: list of words

    Example:
    >>> remover = RemoveAllNonAlphanumericOnlyWords()
    >>> remover.process(['.', 'this', 'is', 'a', 'test', '9', '🤔'])
    ['this', 'is', 'a', 'test', '9']
    """
    def __init__(self):
        pass

    def process(self, text):
        new_text = []
        for word in text:
            if word.isalnum():
                new_text.append(word)
        return new_text

    def explain(self):
        return "Remove all non alphanumeric characters from a list of words"

class RemoveAllNonNumericCharacters:
    """
    A class to remove all non numeric characters from a list of words.

    Expected input: list of words
    Expected output: list of words

    Example:
    >>> remover = RemoveAllNonNumericCharacters()
    >>> remover.process(['.', 'this', 'is', 'a', 'test', '9', '🤔'])
    ['9']
    """
    def __init__(self):
        pass

    def process(self, text):
        return [word for word in text if word.isnumeric()]

    def explain(self):
        return "Remove all non numeric characters from a list of words"

class RemoveTokensWithOnlyPunctuations:
    """
    A class to remove tokens with only punctuations from a list of words.
    This class is useful in cases where the post tokenization you have some words
    which are just punctuations clubbed together.

    Expected input: list of words
    Expected output: list of words

    Example:
    >>> remover = RemoveTokensWithOnlyPunctuations()
    >>> remover.process(['.(', 'this', 'is', 'a', 'test', '?.', '....'])
    ['this', 'is', 'a', 'test']
    """
    def __init__(self, punctuations='!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'):
        self.punctuations = punctuations

    def process(self, text):
        return [word for word in text if not all(char in self.punctuations for char in word)]

    def explain(self):
        return f"Remove tokens with only punctuations from a list of words | Punctuations: {self.punctuations}"

class RemoveTokensWithMajorityNonAlphabeticCharacters:
    """
    A class to remove tokens with majority non alphabetic characters from a list of words.
    This class is useful in cases where the post tokenization you have some words
    which are dominated by Non Alphabetic Characters.

    Expected input: list of words
    Expected output: list of words

    Example:
    >>> remover = RemoveTokensWithMajorityNonAlphabeticCharacters()
    >>> remover.process(['.(', 'this', 'is', 'a', 'test', '?.', '....'])
    ['this', 'is', 'a', 'test']
    """
    def __init__(self, threshold=0.1):
        self.threshold = threshold

    def process(self, text):
        return [word for word in text if not (len(word) - sum(char.isalpha() for char in word))/len(word) > self.threshold]

    def explain(self):
        return f"Remove tokens with majority non alphabetic characters from a list of words | Threshold: {self.threshold}"

def findURLsandHTML(sentence):
  falsePositiveIndicators = ['but', 'don', 'we', 'what', 'you', 'night', 'since', 'especially', 'keep', 'lol', 'and', 'last']
  falsePositiveIndicatorsRegex = re.compile(r'^(' + r'|'.join(falsePositiveIndicators) + r')$', re.IGNORECASE)
  urls = re.findall("(?:http://|https://)?[A-Za-z0-9_]+\.[a-z][A-Za-z0-9_]{1,}[\.A-Za-z0-9_]*[/?[A-Za-z0-9_~]*]*\.?[A-Za-z0-9_]*\\b", sentence)
  all_urls = []
  for url in urls:
    dummy = re.split("\.", url)
    shouldAdd = True
    for comps in dummy:
      if (re.search(falsePositiveIndicatorsRegex, comps) or re.search("^[0-9_]*$", comps)):
        shouldAdd = False
    if shouldAdd:
      all_urls.append(url)
  if re.search("&quot;", sentence):
    all_urls.append("&quot;")
  if re.search("&amp;", sentence):
    all_urls.append("&amp;")
  if re.search("&lt;", sentence):
    all_urls.append("&lt;")
  return all_urls

class ReplaceURLsandHTMLTags:
    """
    A class to remove URLs and HTML tags from a sentence.

    Expected input: list of words
    Expected output: list of words

    Example:
    >>> remover = RemoveURLsandHTMLTags()
    >>> remover.process(['this', 'is', 'a', 'test', 'google.com'])
    ['this', 'is', 'a', 'test', '<URL>']
    """
    def __init__(self, replace_with="<URL>"):
        self.replace_with = replace_with

    def process(self, text):
        new_text = []
        for word in text:
            all_urls = findURLsandHTML(word)
            if len(all_urls) == 0:
                new_text.append(word)
            else:
                for url in all_urls:
                    word = word.replace(url, self.replace_with)
                new_text.append(word)
        return new_text

    def explain(self):
        return "Remove URLs and HTML tags from a sentence | Replace with: {}".format(self.replace_with)

def findUsernames(sentence):
  return re.findall("(?<=^|(?<=[^a-zA-Z0-9-_\.]))@([A-Za-z]+[A-Za-z0-9_]+)", sentence)

class ReplaceUsernames:
    """
    A class to remove usernames from a sentence.

    Expected input: list of words
    Expected output: list of words

    Example:
    >>> remover = ReplaceUsernames()
    >>> remover.process(['this', 'is', 'a', 'test', '@user'])
    ['this', 'is', 'a', 'test', '<USER>']
    """
    def __init__(self, replace_with="<USER>"):
        self.replace_with = replace_with

    def process(self, text):
        new_text = []
        for word in text:
            all_usernames = findUsernames(word)
            if len(all_usernames) == 0:
                new_text.append(word)
            else:
                for username in all_usernames:
                    word = word.replace('@' + username, self.replace_with)
                new_text.append(word)
        return new_text

    def explain(self):
        return "Remove usernames from a sentence | Replace with: {}".format(self.replace_with)

class RemoveUnicode:
    """
    A class to remove unicode characters from a words in a sentence. 
    Removes values below and above a user defined threshold or removes specific unicode characters provided by the user.

    Expected input: list of words
    Expected output: list of words

    Example:
    >>> remover = RemoveUnicode(unicode_below=10, unicode_above=200)
    >>> remover.process(['this', 'is', 'a', 'test', '👍'])
    ['this', 'is', 'a', 'test']
    """
    def __init__(self, unicode_below=None, unicode_above=None, remove_unicode=[]):
        self.unicode_below = unicode_below
        self.unicode_above = unicode_above
        self.remove_unicode = remove_unicode
        if unicode_below is None and unicode_above is None and len(remove_unicode) == 0:
            raise ValueError("At least one of unicode_below or unicode_above or remove_unicode must be defined.")

    def process(self, text):
        new_text = []
        for word in text:
            if self.unicode_below is not None:
                word = ''.join([char for char in word if ord(char) >= self.unicode_below])
            if self.unicode_above is not None:
                word = ''.join([char for char in word if ord(char) <= self.unicode_above])
            if len(self.remove_unicode) > 0:
                word = ''.join([char for char in word if char not in self.remove_unicode])
            new_text.append(word)
        return new_text

    def explain(self):
        return f"Remove unicode characters from a sentence | Unicode below: {self.unicode_below} | Unicode above: {self.unicode_above} | Remove unicode: {self.remove_unicode}"

class RemoveWhiteSpaceOrChunksOfWhiteSpace:
    """
    A class to remove whitespace from a sentence or chunks of whitespace.

    Expected input: list of words
    Expected output: list of words

    Example:
    >>> remover = RemoveWhiteSpaceOrChunksOfWhiteSpace()
    >>> remover.process(['this', 'is', 'a', ' ', 'test', '     '])
    ['this', 'is', 'a', 'test']
    """
    def __init__(self):
        pass

    def process(self, text):
        new_text = []
        for word in text:
            if len(word) == word.count(" "):
                continue
            new_text.append(word)
        return new_text
    
    def explain(self):
        return "Remove whitespace from a sentence or chunks of whitespace"