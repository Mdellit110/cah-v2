import json
from models import *

json_file = open('cah.json')
data = json.load(json_file)

white_cards = data['white']
black_cards = data['black']

for card in white_cards:
    db_session.add(
        WhiteCardModel(
            deck = card['deck'],
            icon = card['icon'],
            text = card['text'],
        )
    )

for card in black_cards:
    db_session.add(
        BlackCardModel(
            pick = card['pick'],
            deck = card['deck'],
            text = card['text'],
            icon = card['icon'],
        )
    )

db_session.commit()
