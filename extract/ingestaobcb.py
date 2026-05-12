import pandas as pd
import requests

url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados"
#CHAMANDO O ENDPOINT(URL), O ENDEREÇO DO BCB

params = {
    "formato": "json",
    "dataInicial": "01/01/2020" # PARÂMETRO ADICIONAL OBRIGATÓRIO pelo BCB
}

headers = {
    "Accept": "application/json"
}

response = requests.get(
    url,
    params=params,
    headers=headers
)

print(response.url)

dados = response.json()

df = pd.DataFrame(dados)

print(df.tail())

df.to_csv("selic.csv", index=False)

df.to_parquet("selic.parquet", index=False)