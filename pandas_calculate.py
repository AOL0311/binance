import os
import pandas as pd
import ta.momentum as TM
import ta.trend as TT

def add_indicators_to_file(file_path):
    df = pd.read_csv(file_path)

    if 'Close' not in df.columns:
        print(f"❌ 檔案缺少 Close 欄位：{file_path}")
        return

    close = pd.to_numeric(df['Close'], errors='coerce')

    df['5EMA'] = TT.EMAIndicator(close=close, window=5).ema_indicator()
    df['10EMA'] = TT.EMAIndicator(close=close, window=10).ema_indicator()
    df['20EMA'] = TT.EMAIndicator(close=close, window=20).ema_indicator()

    df['RSI'] = TM.RSIIndicator(close=close, window=14).rsi()

    macd = TT.MACD(close=close)
    df['MACD'] = macd.macd()
    df['Signal'] = macd.macd_signal()

    df.to_csv(file_path, index=False)
    print(f"✅ 已加入技術指標：{os.path.basename(file_path)}")

def add_indicators_to_folder(folder_path='.'):
    for filename in os.listdir(folder_path):
        if filename.startswith('BTCUSDT_') and filename.endswith('.csv'):
            file_path = os.path.join(folder_path, filename)
            try:
                add_indicators_to_file(file_path)
            except Exception as e:
                print(f"❌ 錯誤處理 {filename}: {e}")

add_indicators_to_folder('BTC_USDT')