from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json
import sqlite3


app = FastAPI()

# SQLiteを実装してmemo_dataテーブルを作成
con = sqlite3.connect("memoapp.db")
cur = con.cursor()
cur.execute("""
    CREATE TABLE IF NOT EXISTS memo_data (
            id INTEGER,
            title TEXT,
            body TEXT,
            references_list TEXT)
""")
con.commit()
con.close()


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

data_path = "../data.json"

# memo_dataのすべての要素を取得する
@app.get("/")
def get_memo_data():
  
  memo_data = cur.execute("SELECT * FROM memo_data")
  con.commit()
  for data in memo_data:
    title = data.get("title")
    if not title:
      data.update(initial_data)
  return memo_data

# /detailで対象のデータを取得する
@app.get("/detail/{data_id}")
def get_detail_data(data_id: int):
  print("data_id:", data_id)
  with open(data_path) as f:
    memo_data = json.load(f)

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
  with open(data_path) as f:
    memo_data = json.load(f)
  
  for data in memo_data:
    id = data.get("id")
    if id == data_id:
      data.update(edit_data)
      print("POST後のデータ", data)
      with open(data_path, "w") as f:
        json.dump(memo_data, f, ensure_ascii=False, indent=2)
        print(memo_data)    
    
# /newでメモを新規に作成して保存する
@app.post("/new")
def post_new_data(new_data: NewData):
  print("new_dataの型:", type(new_data))
  print("new_dataはdictか？:", type(new_data) is dict)
  
  with open(data_path) as f:
    memo_data = json.load(f)

  # new_dataをdict型に変換し、memo_dataの末尾に追加する
  data = {}
  data.update(new_data)
  print("data:", data)
  memo_data.append(data)
  print("memo_data: ", memo_data)
  
  with open(data_path, "w") as f:
    json.dump(memo_data, f, ensure_ascii=False, indent=2)
    print(memo_data)