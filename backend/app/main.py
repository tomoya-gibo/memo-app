from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import time

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
memo_data = [
  {
    "title": "",
    "body": "テストの本文",
    "references": "テストの参考文献",
    "id": 1
  },
  {
    "title": "テスト2",
    "body": "テスト2の本文",
    "references": "テスト2の参考文献",
    "id": 0
  },
  {
    "title": "",
    "body": "テスト3の本文",
    "references": "テスト3の参考文献",
    "id": 2
  }
]

@app.get("/")
def get_memo_data():
  memo_data_length = len(memo_data)
  print("memo_dataの長さ:", memo_data_length)
  for i in range(memo_data_length):
    print("ループの回数:", i)
    for data in memo_data:
      title = data.get("title")
      #id = data.get("id")
      print("title:", title)
      if not title:
        print("titleが空文字")
        #print("id:", id)
        #memo_data[id].update(initial_data)
        #print(memo_data[id])
        title = initial_data["title"]
        body = initial_data["body"]
        refereces = initial_data["references"]
  return memo_data

@app.post("/edit")
def post_memo_data(data: Data):
  memo_data.update(data)
  print("POST後のデータ", memo_data)