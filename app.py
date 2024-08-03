from PyDictionary import PyDictionary


class DictionaryApp:
    def __init__(self):
        self.dictionary = PyDictionary()

    def get_word_meaning(self, word):
        meaning = self.dictionary.meaning(word)
        if meaning:
            for part_of_speech, definitions in meaning.items():
                for definition in definitions:
                    print(f"{part_of_speech}: {definition}")
        else:
            print("No meaning found.")

    def run(self):
        word = input("Enter a word: ").strip()
        self.get_word_meaning(word)


if __name__ == "__main__":
    app = DictionaryApp()
    app.run()
