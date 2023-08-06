import pandas as pd

def get_data(sheet_id: str = '1V4fwE7kxV0h_YqXCbHbOcUrtKBV4oYNL4D-mZuwp09I', sheet_name: str = 'campaign') -> pd.DataFrame:
    url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}'
    return pd.read_csv(url)