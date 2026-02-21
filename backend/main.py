from fastapi import FastAPI

app = FastAPI(title="Cerebro Game Engine")

@app.get("/")
def root():
    return {"message": "Cerebro Engine Running"}