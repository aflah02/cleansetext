from steps import *
remover = RemoveUnicode(unicode_below=10, unicode_above=200)
print(remover.process(['this', 'is', 'a', 'test', '🤔']))