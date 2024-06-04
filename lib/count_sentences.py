#!/usr/bin/env python3

class MyString:
    pass
    def __init__(self, value = ""):
        self.value = value
    
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if type(value) == str:
            self._value = value
        else:
            print("The value must be a string.")
                      
    def is_sentence(self):
        return self._value.endswith(".")

    def is_question(self):
        return self._value.endswith("?")

    def is_exclamation(self):
        return self.value.endswith("!")

    def count_sentences(self):
        value = self.value
        for punctuation in ["!", "?"]:
            value = value.replace(punctuation, ".")

        sentences = [sentence for sentence in value.split(".") if sentence]

        return len(sentences)


string = MyString()

string.value = "This is a string!"
print(string.is_sentence())
print(string.is_question())
print(string.is_exclamation())
print(string.count_sentences())

setattr(string, "value", "It has three sentences.")
print(string.is_sentence())
print(string.is_question())
print(string.is_exclamation())
print(string.count_sentences())

setattr(string, "value", "Right?")
print(string.is_sentence())
print(string.is_question())
print(string.is_exclamation())
print(string.count_sentences())

setattr(string, "value", "This is a string! It has three sentences. Right?")
print(string.is_sentence())
print(string.is_question())
print(string.is_exclamation())
print(string.count_sentences())

new_string = MyString("Hello.")
print(new_string.value)

new_string.value = 234
print(new_string.value)


    






