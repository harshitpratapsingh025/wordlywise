from fastapi import FastAPI

app = FastAPI(title="AI Blog — Backend")


@app.get("/")
async def root():
    return {"message": "AI Blog backend running"}
