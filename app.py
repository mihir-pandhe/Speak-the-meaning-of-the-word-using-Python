from PyMultiDictionary import (
    MultiDictionary,
    DICT_SYNONYMCOM,
    DICT_THESAURUS,
    DICT_WORDNET,
)
import pyttsx3


class Speaking:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty("voices")
        self.engine.setProperty("voice", self.voices[0].id)

    def speak(self, audio):
        self.engine.say(audio)
        self.engine.runAndWait()


def get_word_info():
    dictionary = MultiDictionary()
    speak = Speaking()

    word = input("Enter a word: ").strip()
    if not word:
        print("No word provided. Please try again.")
        speak.speak("No word provided. Please try again.")
        return

    choice = (
        input("Enter 'm' for meaning, 's' for synonyms, 'a' for antonyms: ")
        .strip()
        .lower()
    )

    if choice == "m":
        try:
            meanings = dictionary.meaning("en", word, dictionary=DICT_WORDNET)
            if meanings:
                for part_of_speech, definitions in meanings.items():
                    for definition in definitions:
                        print(f"{part_of_speech}: {definition}")
                        speak.speak(f"The {part_of_speech} meaning is: {definition}")
            else:
                print("No meaning found.")
                speak.speak("No meaning found.")
        except Exception as e:
            print(f"Error: {e}")
            speak.speak("An error occurred while fetching the meaning.")

    elif choice == "s":
        try:
            synonyms = dictionary.synonym("en", word)
            if synonyms:
                print(f"Synonyms for {word}:")
                for synonym in synonyms:
                    print(synonym)
                    speak.speak(f"Synonym: {synonym}")
            else:
                print(f"{word} has no synonyms in the API")
                speak.speak("No synonyms found.")
        except Exception as e:
            print(f"Error: {e}")
            speak.speak("An error occurred while fetching synonyms.")

    elif choice == "a":
        try:
            antonyms = dictionary.antonym("en", word)
            if antonyms:
                print(f"Antonyms for {word}:")
                for antonym in antonyms:
                    print(antonym)
                    speak.speak(f"Antonym: {antonym}")
            else:
                print(f"{word} has no antonyms in the API")
                speak.speak("No antonyms found.")
        except Exception as e:
            print(f"Error: {e}")
            speak.speak("An error occurred while fetching antonyms.")

    else:
        print("Invalid choice. Please enter 'm', 's', or 'a'.")
        speak.speak("Invalid choice. Please try again.")


if __name__ == "__main__":
    get_word_info()
