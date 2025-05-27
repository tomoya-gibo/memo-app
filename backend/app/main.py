from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"]
)

# メモデータの初期値(サンプルデータ)
memo_data = {
  "title": "テスト1",
  "body": "テスト1の本文",
  "references": "テスト1の参考文献"
}

@app.get("/home")
def get_memo_data():
  return memo_data