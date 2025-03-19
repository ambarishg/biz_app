from config_openai import *
from biz import *

from fastapi import FastAPI, HTTPException
import logging
from fastapi import FastAPI, HTTPException, Depends, UploadFile, File, Request, Form
from fastapi.middleware.cors import CORSMiddleware


origins = [
    "*",
]
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


    
@app.get("/hello/")
async def hello():
    try:
        response = {"message": "Hello"}
        return response
    except Exception as e:
        logging.error(e)
        raise HTTPException(status_code=500, detail="Error in Hello")
    
@app.post("/get_answer/")
async def get_answer():
    try:
        reply = get_reply()
        response = {"message": reply}
        return response
    except Exception as e:
        logging.error(e)
        raise HTTPException(status_code=500, detail="Error in Hello")
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
