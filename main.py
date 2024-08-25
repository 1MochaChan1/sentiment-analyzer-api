from fastapi import FastAPI
from mangum import Mangum
from sentiment_analysis import get_sentiment

app = FastAPI()
handler = Mangum(app)


@app.get("/l")
async def get_analysis(link:str):
    res = get_sentiment(link=link)
    return {"sentiment":res}
    

@app.get("/c")
async def get_analysis(content:str):
    res = get_sentiment(content=content)
    return {"sentiment":res}
