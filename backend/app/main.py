from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def get_profile():
    return "Hello"
