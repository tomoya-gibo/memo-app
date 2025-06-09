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
  "title": "サンプルデータ",
  "body": "サンプルデータの本文",
  "references": "サンプルデータの参考文献"
}

# 編集されるメモデータ
# /frontend/src/routes/editで編集されたtitle, body, referencesが格納される。
memo_data = [
  {
    "title": "テスト1",
    "body": "テスト1の本文",
    "references": "テスト1の参考文献",
    "id": 1
  },
  {
    "title": "",
    "body": "テスト2の本文",
    "references": "テスト2の参考文献",
    "id": 0
  },
  {
    "title": "テスト3",
    "body": "テスト3の本文",
    "references": "テスト3の参考文献",
    "id": 2
  }
]

@app.get("/")
def get_memo_data():
  for data in memo_data:
    title = data.get("title")
    if not title:
      data.update(initial_data)
  return memo_data

@app.get("/detail/{data_id}")
def get_detail_data(data_id: int):
  return memo_data[data_id]

@app.post("/edit")
def post_memo_data(data: Data):
  memo_data.update(data)
  print("POST後のデータ", memo_data)