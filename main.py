import os, logging
from dotenv import load_dotenv
## 설정 파일
load_dotenv()
import uvicorn
from logging_config import setup_logging
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
## 로깅 설정 적용 및 로거 생성
setup_logging()
logger = logging.getLogger("app")

logger.info("start k-lingo api")
app = FastAPI(title="K Lingo API", vision="1.0.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)
@app.get("/")
def home():
    return RedirectResponse(url="/index.html")
logger.info('load routers')
# app.include_router(...)
logger.info('static folder')
os.makedirs("static", exist_ok=True)
app.mount("/", StaticFiles(directory="static"), name="static")
logger.info('ready to service[port 8104]')
if __name__ == "__main__":
    # Render는 PORT 환경변수를 제공
    port = int(os.environ.get("PORT", 8104))
    uvicorn.run(app, host="0.0.0.0", port=port)