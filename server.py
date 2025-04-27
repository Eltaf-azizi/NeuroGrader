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