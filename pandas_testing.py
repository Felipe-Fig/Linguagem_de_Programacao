import pandas as pd
from datetime import date
from datetime import datetime as dt

url = pd.read_json("https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json").head()
df_selic = pd.DataFrame(url)

data_extracao = date.today()

df_selic['data_extracao'] = data_extracao
df_selic['responsavel'] = "Teste"

print(df_selic.sort_values(by='data', ascending=False, inplace=True))

print(df_selic.head())