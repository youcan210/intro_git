import eel
import numpy as np

# 3. JSからアクセス
@eel.expose
def js_function(values):
    
    result()

# 1.eel.init('web') # ファイル構成で作ったwebディレクトリを呼び出す
eel.init("web")
eel.start("index.html", size=(650,500))