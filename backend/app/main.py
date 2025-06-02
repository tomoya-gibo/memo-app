from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


app = FastAPI()

app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"]
)

# リクエストボディのデータモデルを定義
class Data(BaseModel):
  title: str
  body: str
  references: str


# メモデータの初期値(サンプルデータ)
initial_data = {
  "title": "テスト1",
  "body": "テスト1の本文",
  "references": "テスト1の参考文献"
}

# 編集されるメモデータ
# /frontend/src/routes/editで編集されたtitle, body, referencesが格納される。
memo_data = {
  # TODO: 各項目がeditで入力された値を受け取るようにする。
  "title": "",
  "body": "",
  "references": ""
}

@app.get("/")
def get_memo_data():
  if not memo_data["title"]:
    memo_data.update(initial_data)
    print(memo_data)
  return memo_data