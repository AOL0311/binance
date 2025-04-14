import os
import pandas as pd

def clean_binance_csv_to_formatted_datetime(file_path):
    with open(file_path, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]

    final_columns = ['Date', 'Open', 'High', 'Low', 'Close',
                     '5EMA', '10EMA', '20EMA', 'RSI', 'MACD', 'Signal']

    max_cols = max(len(line.split(',')) for line in lines[1:])
    all_data = [
        line.split(',') + [''] * (max_cols - len(line.split(',')))
        for line in lines[1:]
    ]

    df = pd.DataFrame(all_data)
    df = df.iloc[:, :len(final_columns)]
    df.columns = final_columns

    df['Date'] = pd.to_datetime(df['Date'], format='%Y%m%d %H%M%S', errors='coerce')
    df = df.dropna(subset=['Date']).sort_values(by='Date')
    df['Date'] = df['Date'].dt.strftime('%Y%m%d %H%M%S')

    return df

def clean_folder(folder_path='.'):
    for filename in os.listdir(folder_path):
        if filename.startswith('BTCUSDT') and filename.endswith('.csv'):
            file_path = os.path.join(folder_path, filename)
            try:
                df = clean_binance_csv_to_formatted_datetime(file_path)
                output_file = os.path.join(folder_path, filename)
                df.to_csv(output_file, index=False)
                print(f"✅ 已處理：{filename} → {os.path.basename(output_file)}")
            except Exception as e:
                print(f"❌ 錯誤處理檔案 {filename}: {e}")

clean_folder('BTC_USDT')