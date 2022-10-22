import pandas as pd
from datetime import date
from datetime import datetime as dt
data_extracao = date.today()
url = pd.read_json("https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json").head()
df_selic = pd.DataFrame(url)
df_selic['data_extracao'] = data_extracao
df_selic['responsavel'] = "Autora"
print(df_selic.info())
#print(df_selic.head())
