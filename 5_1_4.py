class WordString:
    def __init__(self, string=''):
        self.string = string
        self.lst_words = string.split()
        for i in self.lst_words:
            i.split()
if __name__ == '__main__':
    words = WordString('  Python  OOP')
    n = len(words.lst_words)
    first = '' if n == 0 else words.lst_words[0]
    print(words.string)
    print(f"Число слов: {n}; первое слово: {first}")
