from random import choice, randint
from string import ascii_uppercase, hexdigits
from datetime import datetime
from json import dump, load, JSONDecodeError

# N grupos de m:M caracteres
key_max_len = 9 # N
group_max_size = 6 # M
group_min_size = 4 # m

# Key config
KEY_COUNT = 100
KEY_LEVEL = 70000000
KEYFILE_PATH = 'valid_keys.json'


# Elimino los simbolos no válidos

def gen_group():
    size = randint(group_min_size, group_max_size)
    group = ''
    for n in range(size):
        group += choice(hexdigits)
    return (group, int(group, 16))

def gen_key():
    size = randint(4, key_max_len)
    key = ''
    score = 0
    for n in range(size):
        group, fit = gen_group()
        key += f'{group}-'
        score += fit
    key = key[:-1]

    return {
        'key':key,
        'is_valid':(score>=KEY_LEVEL), # 70M ~= 4/1000 (0.004%)
        'fit_level':score,
        'created_at':datetime.now()#.strftime('%d/%m/%y-%H:%M:%S')
    }


def security_level(obj, min, inc):
    score = obj['fit_level']
    if score>(min+inc):
        obj['security_level'] = 'S'
    elif score>(min+inc*2):
        obj['security_level'] = 'A'
    elif score>(min+inc*3):
        obj['security_level'] = 'B'
    elif score>(min+inc*5):
        obj['security_level'] = 'C'
    else:
        obj['security_level'] = 'test'
    return obj


def get_keys(file):
    try:
        with open(file, 'r') as f:
            list = load(f)
            print(f'file {file} loaded.')
        return list
    except JSONDecodeError as err:
        print(err)
        return False
    except FileNotFoundError as err:
        print(err)
        print('generating keyfile...')
        with open(file, 'w') as f:
            print('keyfile created')
        return []


def get_range(keys):
    keys.sort(key=lambda x: x['fit_level'], reverse=True)
    max = keys[-1]['fit_level']
    min = keys[0]['fit_level']
    return (min, max)



def gen_one_key():
    key = gen_key()
    while not key['is_valid']:
        key = gen_key()
        key['hash'] = hash(key.key+key.created_at)
    return key



if __name__=='__main__':
    keys = get_keys(KEYFILE_PATH)
    if not keys or len(keys)==0:
        print('keyfile without keys, generating...')
        keys = []
        while len(keys)<KEY_COUNT:
            key = gen_key()
            if key['is_valid'] == True:
                keys.append(key)
        print('valid keys generated successfully')

    min, max = get_range(keys)
    inc = (max-min)/5

    for key in keys:
        key = security_level(key, min, inc)
        key['hash'] = hash(str(key))


    with open(KEYFILE_PATH, 'w') as f:
        dump(keys, f, indent=2, sort_keys=True)
        print('keyfile updated')
