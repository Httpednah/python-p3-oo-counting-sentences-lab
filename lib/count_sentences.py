class MyString:
    def __init__(self, value=''):
        # Initialize with default empty string
        if isinstance(value, str):
            self._value = value
        else:
            print("The value must be a string.")
            self._value = ''

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        return self._value.endswith('.')

    def is_question(self):
        return self._value.endswith('?')

    def is_exclamation(self):
        return self._value.endswith('!')

    def count_sentences(self):
        import re
        # Split on '.', '?', '!' and remove empty strings
        sentences = re.split(r'[.!?]+', self._value)
        # Filter out empty strings or whitespace-only strings
        sentences = [s for s in sentences if s.strip()]
        return len(sentences)
