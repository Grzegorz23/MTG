from Constants import MAIN_LINK, CARDS, SEARCH, SLASH
import requests


class ApiCall:
    call_content = 'null'

    def __init__(self, card_name, key_word, treatment):
        self.card_name = card_name
        self.key_word = key_word
        self.treatment = treatment

    def call(self):
        self.call_content = requests.get(
            MAIN_LINK
            + SLASH
            + CARDS
            + SLASH
            + SEARCH
            + "q="
            + self.card_name
            + "+"
            + self.key_word
            + "%3A"
            + self.treatment).status_code
        return self

    def parse_call(self):
        if (self.call_content == 400) or (self.call_content == 404):
            return "{}: {}: false".format(self.card_name, self.treatment)
        else:
            return "{}: {}: true".format(self.card_name, self.treatment)
