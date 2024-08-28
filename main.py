from fastapi import FastAPI
from mangum import Mangum
from sentiment_analysis import BertSentimentAnalyzer, get_sentiment

app = FastAPI()
handler = Mangum(app)

analyzer = BertSentimentAnalyzer()
analyzer.load_model()


@app.get("/l")
async def get_analysis(link:str):
    res = analyzer.get_sentiment(link=link)
    return {"sentiment":res}
    

@app.get("/c")
async def get_analysis(content:str):
    res = analyzer.get_sentiment(content=content)
    return {"sentiment":res}
