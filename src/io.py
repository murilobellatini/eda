from google.colab import drive
import io, os, requests
import pandas as pd

from src.paths import GDRIVE_PATH

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


def mount_gdrive(path=GDRIVE_PATH):
    """
    Monta GDrive.
    
    `Nota`: Este método precisa de autorização de acesso ao Googles
    """
    drive.mount(path)


def export_df(df:pd.DataFrame, fname:str, outdir:str):
    """
    Exporta DataFrame para diretório
    """
    if not os.path.exists(outdir):
        os.makedirs(outdir)

    df.to_csv(f'{outdir}/{fname}')


def export_to_gdrive(df:pd.DataFrame, fname:str, gdrive_folder:str):
    """
    Persiste DataFrame em Google Drive
    """
    mount_gdrive()
    assert GDRIVE_PATH in gdrive_folder, f"`gdrive_folder` not within `GDRIVE_PATH` ({GDRIVE_PATH}). Export data within Google Drive."
    export_df(df, fname, gdrive_folder)
