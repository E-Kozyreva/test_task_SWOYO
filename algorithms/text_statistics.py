import re


class TextStatistics:
    def __init__(self):
        self.text = ""
        self.words = []
        self.letters = ()
        self.frequency = {}
        self.bilingual_words = []
        
    # текст из файла
    def get_text(self, file_path: str) -> str:
        with open(file_path, 'r', encoding='UTF-8') as file:
            self.text = file.read()
        
    # слова из текста
    def get_words(self) -> list:
        self.words = re.findall(r'\w+', self.text)
        return self.words
    
    # количество слов
    def words_amount(self) -> int:
        return len(self.words)
    
    # буквы из слов
    def get_letters(self) -> tuple:
        self.letters =  tuple("".join(self.words))
        return self.letters
    
    # количество букв и их частоту
    def letters_frequency(self) -> dict:
        split_text = "".join(self.words)

        for letter in self.letters:
            f_letter = split_text.count(letter)
            p_letter = 0
            for w in self.words:
                if letter in w:
                    p_letter += 1
            self.frequency[letter] = (f_letter, p_letter)
            
        return self.frequency
        
    # количество параграфов
    def paragraph_amount(self) -> int:
        return self.text.count("\n\n")
    
    # слова с включающие буквы из разных алфавитов
    def bilingual_word_amount(self) -> int:
        for w in self.words:
            if re.search(r'[a-zA-Z]', w) and re.search(r'[а-яА-Я]', w):
                self.bilingual_words.append(w)   
                  
        return self.bilingual_words



def text_statistics(file_path: str) -> tuple:
    ts = TextStatistics()
    ts.get_text(file_path)
    ts.get_words()
    ts.get_letters()

    w_amount = ts.words_amount()
    l_frequency = ts.letters_frequency()
    p_amount = ts.paragraph_amount()
    b_words = ts.bilingual_word_amount()

    text_statistics = {}

    for key, value in l_frequency.items():
        text_statistics[key] = value

    text_statistics["word_amount"] = w_amount
    text_statistics["paragraph_amount"] = p_amount
    text_statistics["bilingual_word_amount"] = len(b_words)

    return text_statistics
