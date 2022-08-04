import multiprocessing
import API.ApiCall as Call
import time
import Cards.FetchData as Data


def get_cards(card):
    return card.call().parse_call()

if __name__ == '__main__':
    data = Data.FetchData()
    all_cards = data.card_file_parse()
    treatments = data.treatments()

    cards_details = {card: {j: treatments[j] for j in treatments} for card in all_cards}

    call_list = [Call.ApiCall(card_name, key_word, treatment) for card_name in cards_details for key_word in cards_details[card_name] for treatment in cards_details[card_name][key_word]]

    start = time.time()
    with multiprocessing.Pool(multiprocessing.cpu_count()) as p:
        r = p.map(get_cards, call_list)
    print(time.time() - start)
    for i in r:
        print(i)
#

  #for i in json_list:
  #    print(i)
  ## print(json_list)
  #    # json_list.append()

  ## image = requests.get('https://api.scryfall.com/cards/named?exact=Kumena, Tyrant of Orazca&format=image')
  #Json = requests.get('https://api.scryfall.com/cards/search?q=Aboleth Spawn+frame%3Aextendedart')

  #key_word = json.loads(Json.content)

  ## print(key_word)
#  ##(Image.open(BytesIO(image.content))).show()