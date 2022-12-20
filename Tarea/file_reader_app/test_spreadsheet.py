import pandas as pd

def coon_pool_to_google_spreadsheet(sheet_id):
    return f'https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&id={sheet_id}&gid=135007174'

def test_coon_pool_to_google_spreadsheet_is_ok():
    
    sheet_id = '1-Wx3MunuVlDT96K_fz18P1HgBUYaxSBjUu16_KyNjDU'
    url = coon_pool_to_google_spreadsheet(sheet_id=sheet_id)
    df = pd.read_csv(url)

    assert len(df)!=0