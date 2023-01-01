import nltk
import emoji
import re
import string

class StopWordsRemover:
    """
    A class to remove stopwords from a list of words.

    Args:
        ignore_case (bool): If set to True, ignore the case of the words when comparing them to the stopwords list. Default is True.
        ignored_stopwords (list): A list of stopwords that should not be removed from the input text, even if they are in the stopwords list. Default is an empty list.
        include_stopwords (list): A list of additional stopwords to include in the stopwords list. Default is an empty list.
        language (str): The language of the stopwords list to use. Default is 'english'.

    Example:
        remover = StopWordsRemover()
        remover.process(['this', 'is', 'a', 'test'])
        >> ['test']
    """
    def __init__(self, ignore_case=True, ignored_stopwords=None, include_stopwords=None, language='english'):
        """Initialize the StopWordsRemover instance with the given parameters."""
        nltk.download('stopwords')
        self.stopwords = set(nltk.corpus.stopwords.words(language))
        self.ignore_case = ignore_case
        self.ignored_stopwords = set(ignored_stopwords) if ignored_stopwords else set()
        self.include_stopwords = set(include_stopwords) if include_stopwords else set()
        self.all_stopwords = self.stopwords.union(set(self.include_stopwords)) if self.include_stopwords else self.stopwords
        self.language = language

    def process(self, text):
        """
        Remove stopwords from a list of words.

        Args:
            text (list): A list of words to process.

        Returns:
            list: A list of words with stopwords removed.
        """
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
        """
        Return a string explanation of the current stopwords removal configuration.

        Returns:
            str: A string explanation of the current stopwords removal configuration.
        """
        return f"Remove stopwords from text | Ignore case: {self.ignore_case} | Ignored stopwords: {self.ignored_stopwords} | Language: {self.language}"


class EmojiToText:
    """
    A class to replace emojis in a list of words with text equivalents.

    Args:
        language (str): The language of the text. Default is 'en'.

    Example:
        emoji_to_text = EmojiToText()
        emoji_to_text.process(['this', 'is', 'a', 'test', '🤔'])
        >> ['this', 'is', 'a', 'test', ':thinking_face:']
    """
    def __init__(self, language='en'):
        """Initialize the EmojiToText instance with the given language."""
        self.language = language

    def process(self, text):
        """
        Replace emojis in a list of words with text equivalents.

        Args:
            text (list): A list of words to process.

        Returns:
            list: A list of words with emojis replaced with text equivalents.
        """
        return [emoji.demojize(word, language=self.language) if emoji.demojize(word, language=self.language) != word else word for word in text]

    def explain(self):
        """
        Return a string explanation of the current emoji replacement configuration.

        Returns:
            str: A string explanation of the current emoji replacement configuration.
        """
        return f"Replace emojis with text | Language: {self.language}"


class TextToEmoji:
    """
    A class to replace text with emojis in a list of words.

    Args:
        language (str): The language of the text. Default is 'en'.

    Example:
        text_to_emoji = TextToEmoji()
        text_to_emoji.process(['this', 'is', 'a', 'test', ':thinking_face:'])
        >> ['this', 'is', 'a', 'test', '🤔']
    """
    def __init__(self, language='en'):
        """Initialize the TextToEmoji instance with the given language."""
        self.language = language

    def process(self, text):
        """
        Replace text with emojis in a list of words.

        Args:
            text (list): A list of words to process.

        Returns:
            list: A list of words with text replaced with emojis.
        """
        return [emoji.emojize(word, language=self.language) if emoji.emojize(word, language=self.language) != word else word for word in text]

    def explain(self):
        """
        Return a string explanation of the current text replacement configuration.

        Returns:
            str: A string explanation of the current text replacement configuration.
        """
        return f"Replace text with emojis | Language: {self.language}"


class RemoveEmojis:
    """
    A class to remove emojis from a list of words.

    Args:
        ignored_emojis (list): A list of emojis that should not be removed from the input text. Default is an empty list.

    Example:
        remover = RemoveEmojis()
        remover.process(['this', 'is', 'a', 'test', '🤔'])
        >> ['this', 'is', 'a', 'test']
    """
    def __init__(self, ignored_emojis=None):
        """Initialize the RemoveEmojis instance with the given ignored emojis."""
        self.ignored_emojis = ignored_emojis

    def process(self, text):
        """
        Remove emojis from a list of words.

        Args:
            text (list): A list of words to process.

        Returns:
            list: A list of words with emojis removed.
        """
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
        """
        Return a string explanation of the current emoji removal configuration.

        Returns:
            str: A string explanation of the current emoji removal configuration.
        """
        return f"Remove emojis from text"


class RemovePrecedingAndTrailingPunctuations:
    """
    A class to remove punctuations from the beginning and end of a list of words.

    Args:
        punctuations (str): A string of punctuation characters to remove. Default is all ASCII punctuation characters.
        ignore_starting_punctuations (bool): If set to True, do not remove punctuations from the beginning of words. Default is False.
        ignore_ending_punctuations (bool): If set to True, do not remove punctuations from the end of words. Default is False.

    Example:
        remover = RemovePrecedingAndTrailingPunctuations()
        remover.process(['.', 'this', 'is', 'a', 'test', '.', '.'])
        >> ['this', 'is', 'a', 'test']
    """
    def __init__(self, punctuations='!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~', ignore_starting_punctuations=False, ignore_ending_punctuations=False):
        """
        Initialize the RemovePrecedingAndTrailingPunctuations instance with the given punctuations and ignore flags.
        
        Args:
            punctuations (str): A string of punctuation characters to remove.
            ignore_starting_punctuations (bool): If set to True, do not remove punctuations from the beginning of words.
            ignore_ending_punctuations (bool): If set to True, do not remove punctuations from the end of words.
        """
        self.punctuations = punctuations
        self.ignore_starting_punctuations = ignore_starting_punctuations
        self.ignore_ending_punctuations = ignore_ending_punctuations

    def process(self, text):
        """
        Remove punctuations from the beginning and end of a list of words.

        Args:
            text (list): A list of words to process.

        Returns:
            list: A list of words with punctuations removed from the beginning and end.
        """
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
        """
        Return a string explanation of the current punctuation removal configuration.

        Returns:
            str: A string explanation of the current punctuation removal configuration.
        """
        return f"Remove punctuations from the beginning and end of a word | Punctuations: {self.punctuations} | Ignore starting punctuations: {self.ignore_starting_punctuations} | Ignore ending punctuations: {self.ignore_ending_punctuations}"


class RemoveAllPunctuations:
    """
    A class to remove all punctuations from a list of words.

    Args:
        punctuations (str): A string of punctuation characters to remove. Default is all ASCII punctuation characters.

    Example:
        remover = RemoveAllPunctuations()
        remover.process(['.', 'this', 'is', 'a', '.', 'test', '.', '.'])
        >> ['this', 'is', 'a', 'test']
    """
    def __init__(self, punctuations='!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'):
        """
        Initialize the RemoveAllPunctuations instance with the given punctuation characters.

        Args:
            punctuations (str): A string of punctuation characters to remove.
        """
        self.punctuations = punctuations

    def process(self, text):
        """
        Remove all punctuations from a list of words.

        Args:
            text (list): A list of words to process.

        Returns:
            list: A list of words with all punctuations removed.
        """
        return [word for word in text if word not in self.punctuations]

    def explain(self):
        """
        Return a string explanation of the current punctuation removal configuration.

        Returns:
            str: A string explanation of the current punctuation removal configuration.
        """
        return f"Remove all punctuations from a list of words | Punctuations: {self.punctuations}"


class RemoveAllNonAlphabetOnlyWords:
    """
    A class to remove all non alphabet only words from a list of words.

    Example:
        remover = RemoveAllNonAlphabetOnlyWords()
        remover.process(['.', 'this', 'is', 'a', 'test', '9', '🤔'])
        >> ['this', 'is', 'a', 'test', '9]
    """
    def __init__(self):
        """Initialize the RemoveAllNonAlphabetOnlyWords instance."""
        pass

    def process(self, text):
        """
        Remove all non alphabet only words from a list of words.

        Args:
            text (list): A list of words to process.

        Returns:
            list: A list of words with all non alphabet only words removed.
        """
        new_text = []
        for word in text:
            if word.isalpha():
                new_text.append(word)
        return new_text

    def explain(self):
        """
        Return a string explanation of the current non alphabet only word removal configuration.

        Returns:
            str: A string explanation of the current non alphabet only word removal configuration.
        """
        return "Remove all non alphabet only words from a list of words"


class RemoveAllNonAlphanumericOnlyWords:
    """
    A class to remove all non alphanumeric only words from a list of words.

    Example:
        remover = RemoveAllNonAlphanumericOnlyWords()
        remover.process(['.', 'this', 'is', 'a', 'test', '9', '🤔'])
        >> ['this', 'is', 'a', 'test', '9']
    """
    def __init__(self):
        """Initialize the RemoveAllNonAlphanumericOnlyWords instance."""
        pass

    def process(self, text):
        """
        Remove all non alphanumeric only words from a list of words.

        Args:
            text (list): A list of words to process.

        Returns:
            list: A list of words with all non alphanumeric only words removed.
        """
        new_text = []
        for word in text:
            if word.isalnum():
                new_text.append(word)
        return new_text

    def explain(self):
        """
        Return a string explanation of the current non alphanumeric only word removal configuration.

        Returns:
            str: A string explanation of the current non alphanumeric only word removal configuration.
        """
        return "Remove all non alphanumeric characters from a list of words"


class RemoveAllNonNumericOnlyWords:
    """
    A class to remove all non numeric characters from a list of words.

    Example:
        remover = RemoveAllNonNumericCharacters()
        remover.process(['.', 'this', 'is', 'a', 'test', '9', '🤔'])
        >> ['9']
    """
    def __init__(self):
        """Initialize the RemoveAllNonNumericOnlyWords instance."""
        pass

    def process(self, text):
        """
        Remove all non numeric characters from a list of words.

        Args:
            text (list): A list of words to process.

        Returns:
            list: A list of words with all non numeric characters removed.
        """
        return [word for word in text if word.isnumeric()]

    def explain(self):
        """
        Return a string explanation of the current non numeric only word removal configuration.

        Returns:
            str: A string explanation of the current non numeric only word removal configuration.
        """
        return "Remove all non numeric only words from a list of words"


class RemoveTokensWithOnlyPunctuations:
    """
    A class to remove tokens with only punctuations from a list of words.
    This class is useful in cases where the post tokenization you have some words
    which are just punctuations clubbed together.

    Example:
        remover = RemoveTokensWithOnlyPunctuations()
        remover.process(['.(', 'this', 'is', 'a', 'test', '?.', '....'])
        >> ['this', 'is', 'a', 'test']
    """
    def __init__(self, punctuations='!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'):
        """
        Initialize the RemoveTokensWithOnlyPunctuations instance.

        Args:
            punctuations (str): A string of punctuation characters to remove.
        """
        self.punctuations = punctuations

    def process(self, text):
        """
        Remove tokens with only punctuations from a list of words.

        Args:
            text (list): A list of words to process.

        Returns:
            list: A list of words with tokens containing only punctuations removed.
        """
        return [word for word in text if not all(char in self.punctuations for char in word)]

    def explain(self):
        """
        Return a string explanation of the current token removal configuration.

        Returns:
            str: A string explanation of the current token removal configuration.
        """
        return f"Remove tokens with only punctuations from a list of words | Punctuations: {self.punctuations}"


class RemoveTokensWithMajorityNonAlphabeticCharacters:
    """
    A class to remove tokens with majority non alphabetic characters from a list of words.
    This class is useful in cases where the post tokenization you have some words
    which are dominated by non alphabetic characters.

    Example:
        remover = RemoveTokensWithMajorityNonAlphabeticCharacters()
        remover.process(['.(', 'this', 'is', 'a', 'test', '?.', '....'])
        >> ['this', 'is', 'a', 'test']
    """
    def __init__(self, threshold=0.1):
        """
        Initialize the RemoveTokensWithMajorityNonAlphabeticCharacters instance.

        Args:
            threshold (float): A threshold ratio of non alphabetic characters to remove a token.
        """
        self.threshold = threshold

    def process(self, text):
        """
        Remove tokens with majority non alphabetic characters from a list of words.

        Args:
            text (list): A list of words to process.

        Returns:
            list: A list of words with tokens containing majority non alphabetic characters removed.
        """
        return [word for word in text if not (len(word) - sum(char.isalpha() for char in word))/len(word) > self.threshold]

    def explain(self):
        """
        Return a string explanation of the current token removal configuration.

        Returns:
            str: A string explanation of the current token removal configuration.
        """
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