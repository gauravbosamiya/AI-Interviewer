from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import os

app = FastAPI()


@app.get("/")
def home():
    return {'Message':'AI Interviewer Assistant'}

@app.get("/upload-resume")
def upload_resume(file:UploadFile=File(...)):
    pass
    # allowed_type=['.pdf','.docx']
    # file_extension = os.path.splitext(file.filename)[1].lower()
    
    # if file_extension not in allowed_type:
    #     raise HTTPException(status_code=400, detail=f"Unsupported file type Allowed file types are : {', '.join(allowed_type)}")

