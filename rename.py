import os

folder_path = 'BTC_USDT'  # 你的資料夾名稱

for filename in os.listdir(folder_path):
    if filename.endswith('_C.csv'):
        new_name = filename.replace('_C.csv', '.csv')
        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_name)
        os.rename(old_path, new_path)
        print(f"✅ 已重新命名：{filename} ➜ {new_name}")
