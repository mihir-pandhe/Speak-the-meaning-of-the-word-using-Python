import pyttsx3
from PyDictionary import PyDictionary


class Speaking:
    def __init__(self):
        self.engine = pyttsx3.init("sapi5")
        self.voices = self.engine.getProperty("voices")
        self.engine.setProperty("voice", self.voices[0].id)

    def speak(self, audio):
        self.engine.say(audio)
        self.engine.runAndWait()


class DictionaryApp:
    def __init__(self):
        self.dictionary = PyDictionary()
        self.speaker = Speaking()

    def get_word_meaning(self, word):
        meaning = self.dictionary.meaning(word)
        if meaning:
            for part_of_speech, definitions in meaning.items():
                for definition in definitions:
                    print(f"{part_of_speech}: {definition}")
                    self.speaker.speak(f"The {part_of_speech} meaning is: {definition}")
        else:
            print("No meaning found.")
            self.speaker.speak("No meaning found.")

    def run(self):
        word = input("Enter a word: ").strip()
        self.get_word_meaning(word)


if __name__ == "__main__":
    app = DictionaryApp()
    app.run()
