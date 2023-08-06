import base64
from datetime import datetime

from motoo import wit_util as wu
import requests
import orjson

user_id = ''
password = ''

def set_credentials(id, pw):
    global user_id, password
    user_id = id
    password = pw

def get_wit(wit_id, from_date=None, to_date=datetime.today().strftime('%Y%m%d'), stock_codes=[]):
    global user_id, password
    if user_id is None or user_id == '' or password is None or password == '':
        return ''

    data = dict(
        user_id=user_id,
        password=password,
        wit_id=wit_id,
        from_date=from_date,
        to_date=to_date,
        stock_codes=stock_codes
    )
    
    response = requests.post('https://comp.quantbox.net/api.app.get_data', json=data).text
    return json_loads(json_loads(response))

def get_shared_wit(share_code='', from_date=None, to_date=datetime.today().strftime('%Y%m%d'), stock_codes=[]):
    if user_id is None or user_id == '' or password is None or password == '':
        return ''

    data = dict(
        user_id=user_id,
        password=password,
        share_code=share_code,
        from_date=from_date,
        to_date=to_date,
        stock_codes=stock_codes
    )
    
    response = requests.post('https://comp.quantbox.net/api.app.get_shared_data', json=data).text
    return json_loads(json_loads(response))

def json_loads(s):
    try:
        result_value = orjson.loads(s)
        json_load_parser(result_value)
    except:
        if isinstance(s, str) and s.startswith("wit_temp_data_tttt_"):
            result_value = s[len("wit_temp_data_tttt_"):]
            result_value = result_value.encode('utf-8')
            result_value = base64.b64decode(result_value)
            result_value = wu.bytes_to_wit_data(result_value).to_dataframe()
        elif isinstance(s, str) and s.startswith("bbbbytes_"):
            result_value = s[len("bbbbytes_"):]
            result_value = result_value.encode('utf-8')
            result_value = base64.b64decode(result_value)
        else:
            result_value = s

    return result_value

def json_load_parser(s):
    if isinstance(s, list):
        for i, v in enumerate(s):
            if isinstance(v, str) and v.startswith("wit_temp_data_tttt_"):
                try:
                    v = v[len("wit_temp_data_tttt_"):]
                    v = v.encode('utf-8')
                    v = base64.b64decode(v)
                    s[i] = wu.bytes_to_wit_data(v).to_dataframe()
                except: pass
            elif isinstance(v, str) and v.startswith("bbbbytes_"):
                try:
                    v = v[len("bbbbytes_"):]
                    v = v.encode('utf-8')
                    s[i] = base64.b64decode(v)
                except: pass
            else: json_load_parser(v)
    elif isinstance(s, dict):
        for k, v in s.items():
            if isinstance(v, str) and v.startswith("wit_temp_data_tttt_"):
                try:
                    v = v[len("wit_temp_data_tttt_"):]
                    v = v.encode('utf-8')
                    v = base64.b64decode(v)
                    s[k] = wu.bytes_to_wit_data(v).to_dataframe()
                except: pass
            elif isinstance(v, str) and v.startswith("bbbbytes_"):
                try:
                    v = v[len("bbbbytes_"):]
                    v = v.encode('utf-8')
                    s[k] = base64.b64decode(v)
                except: pass
            else: json_load_parser(v)