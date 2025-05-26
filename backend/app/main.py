from fastapi import FastAPI

app = FastAPI()

# TODO CORS設定をする。

# メモデータの初期値(サンプルデータ)
memo_data = {
  "title": "テスト1",
  "body": "テスト1の本文",
  "references": "テスト1の参考文献"
}

@app.get("/home")
def get_memo_data():
  return memo_data