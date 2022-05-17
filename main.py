#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fastapi import FastAPI, UploadFile
from PIL import Image
import pytesseract

app = FastAPI()


@app.get('/')
async def index():
    return 'A ocr service compatable to JCSS service'


@app.post('/')
async def ocr(image: UploadFile):
    im = Image.open(image.file)
    text = pytesseract.image_to_string(im)
    return {
        'data': {
            'predict': text.strip()
        }
    }
