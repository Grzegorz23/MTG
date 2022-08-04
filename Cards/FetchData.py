import re


class FetchData:

    def __init__(self, files_path="C:\\Users\\Grzesiek\\PycharmProjects\\MTG\\"):
        self.files_path = files_path

    def card_file_parse(self):
        with open("{}cards.txt".format(self.files_path), encoding='utf-8') as f:
            return [re.findall('^\d* (.*)', card)[0]
                    for card in f.readlines()]

    def treatments(self):
        with open("{}treatments.txt".format(self.files_path), encoding='utf-8') as f:
            return {treat.split(" ")[0]: [j.replace("\n", "").replace(",", "")
                                          for j in treat.split(" ")[1:]] for treat in f.readlines()}


