import io, requests
import pandas as pd

def load_df_from_url(url:str, sep:str=','):
  """
  Carrega dataframe disponível em URL (link externo)
  """
  with io.StringIO(load_txt_from_url(url)) as data:
    df = pd.read_csv(data, sep=sep)
  return df

def load_txt_from_url(url:str):
  """
  Carrega texto disponível em URL
  """
  return requests.get(url).text