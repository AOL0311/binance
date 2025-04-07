# .recv() 回傳 dic

|代號|名稱|解釋|
|:----:|:----:|:-----|
|e|event type|事件類型，指示這個消息是交易事件|
|E|event time|事件時間，表示事件發生的時間戳|
|s|symbol|交易對，表示這是 `BTC/USDT` 交易對|
|t|trade ID|交易 ID，唯一標示一次交易的 ID|
|p|price|交易價格，表示此次交易的價格為多少 USDT|
|q|quantity|交易數量，表示此次交易的數量為多少 BTC|
|T|trade time|交易時間，表示此次交易的時間戳|
|m|maker|是否為做市商|
|M|best match|是否為最佳匹配|