from fastapi import FastAPI, UploadFile, File

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    return {
        "result": "AI 서버 정상 연결 (YOLO 미연결 상태)"
    }
