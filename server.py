from fastapi import FastAPI, Request, HTTPException, Depends
import uvicorn
import openai
import os
import sys
from pydantic import BaseModel
from typing import Dict, Any, Optional, Union, List
import requests
from functools import lru_cache
import logging



# Initialize logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


# ===== 🔒 Config =====
class Settings:
    def __init__(self):
        self.openai_api_key = os.environ.get("OPENAI_API_KEY", "")
        self.google_api_key = os.environ.get("GOOGLE_API_KEY", "")
        self.search_engine_id = os.environ.get("SEARCH_ENGINE_ID", "")


        # Log configuration status (but don't expose actual keys)
        logger.info(f"OPENAI_API_KEY  set: {'Yes' if self.openai_api_key else 'No'}")
        logger.info(f"GOOGLE_API_KEY set: {'Yes' if self.google_api_key else 'No'}")
        logger.info(f"SEARCH_ENGINE_ID set: {'Yes' if self.search_engine_id else 'No'}")
        logger.info(f"Python version: {sys.version}")



@lru_cache()
def get_settings():
    return Settings()


# ==== Models ====
class BaseRequest(BaseModel):
    openai_api_key: Optional[str] = None
    google_api_key: Optional[str] = None
    search_engine_id: Optional[str] = None


class ParseFileRequest(BaseRequest):
    file_path: str


class PlagiarismRequest(BaseRequest):
    text: str
    similarity_threshold: Optional[int] = 40


class GradeRequest(BaseRequest):
    text: str
    rubric: str
    model: Optional[str] = "gpt-3.5-turbo"
