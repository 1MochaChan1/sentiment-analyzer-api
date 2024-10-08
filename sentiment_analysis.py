import bs4, requests # Libraries for scraping
import pandas as pd # For handling CSV (not used here)
from transformers import AutoTokenizer, AutoModelForSequenceClassification # BERT model for sentiment analysis
import torch # For model-related operations
import re # For regex

class BertSentimentAnalyzer():
    def __init__(self) -> None:
        self.model = None
        self.tokenizer = None


    def load_model(
        self, 
        tokenizer:str='nlptown/bert-base-multilingual-uncased-sentiment', 
        model:str='nlptown/bert-base-multilingual-uncased-sentiment'):
        
        # Load pre-trained tokenizer and model
        self.tokenizer = AutoTokenizer.from_pretrained(tokenizer)
        self.model = AutoModelForSequenceClassification.from_pretrained(model)
        
    def get_blog_content(self, link: str) -> str:
        try:
            res = requests.get(link).text # Fetches page content as text
            soup = bs4.BeautifulSoup(res) # Parses the HTML content
            paras = ' '.join([x.text for x in soup.findAll(re.compile("^h[1-6]$"))])
            # Cleans text by removing tabs, newlines, and commas
            paras = paras.replace('\t','').replace('\n','').replace(',','')
            return str(paras).strip() # Returns the cleaned text
        except Exception as e:
            print(e) # Prints error if any issues occur

    def get_sentiment(self, link: str=None, content: str=None) -> str:
        blog_data = None
        
        # Get content either from link or passed text
        if link:
            blog_data = self.get_blog_content(link)
        elif content:
            blog_data = content
        
        tokens = self.tokenizer.encode(blog_data, return_tensors='pt') # Tokenize the content for analysis
        res = self.model(tokens) # Get sentiment prediction
        
        # Determine sentiment: less than 3 is 'NEGATIVE', otherwise 'POSITIVE'
        verdict = 'NEGATIVE' if int(torch.argmax(res.logits)) + 1 < 3 else 'POSITIVE'
        
        return verdict
    
