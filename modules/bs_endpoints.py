from .app import app
from flask import render_template, jsonify
from requests import get
from bs4 import BeautifulSoup
from math import ceil


api_url = "https://brawlify.com/stats/profile/"

@app.route('/bs/<tag>', methods=['GET', ['POST']])
def get_brawlers(tag):
    req = get(api_url+tag)
    bs = BeautifulSoup(req.content, 'html.parser')

    try:
        brawlers = [{
            'name':brawl.find('img')['alt'],
            'trophies':int(brawl.find_all('div')[-1].text),
            'img_url':brawl.find('img')['src'],
        } for brawl in bs.find_all('a', class_='brawlerBlock') if int(brawl.find_all('div')[-1].text)>=493]

        for brawl in brawlers:
            diff = brawl['trophies']%25
            at_end = brawl['trophies']-diff-1 if brawl['trophies']>525 else brawl['trophies']-diff
            brawl['next_goal'] = brawl['trophies']+25-diff
            brawl['remaining_wins'] = ceil((25-diff)/8)
            brawl['trophies_at_end'] = at_end
            brawl['trophies_losted'] = brawl['trophies']-at_end

        return jsonify(brawlers)
    except:
        return jsonify('message':'invalid tag')


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
