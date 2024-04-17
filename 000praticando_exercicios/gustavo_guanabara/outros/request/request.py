import request

from datetime import datetime

requisisao = request.get('') 

requisisao_dic = requisisao.json()
cotacao_dolar = requisisao_dic['USDBRL'] ['bid']
cotacao_euro = requisisao_dic['EURBRL'] ['bid']
cotacao_btc = requisisao_dic['BTCBRL'] ['bid']

print(f'cotação atualizad. {datetime.now()}')