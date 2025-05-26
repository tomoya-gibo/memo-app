from fastapi import FastAPI

app = FastAPI()

# メモデータの初期値(サンプルデータ)
memoData = {
  "title": "テスト1",
  "body": "テスト1の本文",
  "references": "テスト1の参考文献"
}

@app.get("/")
async def root():
  return {"message": "Hello World"}