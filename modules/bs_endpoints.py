from .app import app
from flask import render_template, jsonify
from brawlstats import Client
from requests import get
from math import ceil
from os import environ

key = environ['BS_TOKEN']

cli = Client(key)
api_url = "https://api.brawlapi.com/v1/brawlers/"

@app.route('/bs/<tag>', methods=['GET', ['POST']])
def get_brawlers(tag):
    profile = cli.get_profile(tag)
    # guardo solo los que necesitan + de una victoria para dar puntos estelares
    brawlers = [brawl for brawl in profile.brawlers if brawl.trophies>493]
    brawlers = sorted(brawlers, key=lambda x: x.trophies)
    # listado de brawlers con +493 trofeos ordenados de mayor a menor
    brawlers.reverse()
    response = []

    for brawl in brawlers:
        diff = brawl.trophies%25
        at_end = brawl.trophies-diff-1 if brawl.trophies>525 else brawl.trophies-diff
        response.append({
            'img': get(api_url+str(brawl.id)).json()['imageUrl2'],
            'name': brawl.name,
            'trophies': brawl.trophies,
            'next_goal': brawl.trophies+25-diff,
            'remaining_wins': ceil((25-diff)/8),
            'trophies_at_end': at_end,
            'trophies_losted': brawl.trophies-at_end
            })
    return jsonify(sorted(response, key=lambda x: x['remaining_wins']))






@app.route('/bs')
def index_bs():
    return render_template('bs/index.html')


if __name__=="__main__":
    brawlers = get_brawlers("cr2ulju8")

    total = 0
    posible = 0
    for b in brawlers:
        total += b['trophies_losted']
        posible += 1
        print(b)

    print(f'Copas perdidas {total} (contra {posible})')
