from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json


app = FastAPI()

app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"]
)

# リクエストボディのデータモデルを定義
class EditData(BaseModel):
  title: str
  body: str
  references: str

class NewData(BaseModel):
  title: str
  body: str
  references: str
  id: int

# メモデータの初期値(サンプルデータ)
initial_data = {
  "title": "サンプルデータ",
  "body": "サンプルデータの本文",
  "references": "サンプルデータの参考文献"
}

# 編集されるメモデータ
# /frontend/src/routes/editで編集されたtitle, body, referencesが格納される。
#memo_data = []

# memo_dataのすべての要素を取得する
@app.get("/")
def get_memo_data():
  with open("../data.json") as f:
    memo_data = json.load(f)
    print("memo_data:", memo_data)
  for data in memo_data:
    title = data.get("title")
    if not title:
      data.update(initial_data)
  return memo_data

# /detailで対象のデータを取得する
@app.get("/detail/{data_id}")
def get_detail_data(data_id: int):
  print("data_id:", data_id)
  for data in memo_data:
    id = data.get("id")
    title = data.get("title")
    if id == data_id:
      if not title:
        data.update(initial_data)
      return data

# /editで変更内容を保存する
@app.post("/edit/{data_id}")
def post_memo_data(data_id: int, edit_data: EditData):
  print("edit_dataの型:", type(edit_data))
  for data in memo_data:
    id = data.get("id")
    if id == data_id:
      data.update(edit_data)

      print("POST後のデータ", data)
      return data
    
# /newでメモを新規に作成して保存する
@app.post("/new")
def post_new_data(new_data: NewData):
  print("new_dataの型:", type(new_data))
  print("new_dataはdictか？:", type(new_data) is dict)
  
  # new_dataをdict型に変換し、memo_dataの末尾に追加する
  data = {}
  data.update(new_data)
  print("data:", data)
  memo_data.append(data)
  print("memo_data: ", memo_data)