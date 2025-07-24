from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.templating import Jinja2Templates
from app.config import DASHBOARD_USER, DASHBOARD_PASS
import secrets

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")
security = HTTPBasic()

def check_auth(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, DASHBOARD_USER)
    correct_password = secrets.compare_digest(credentials.password, DASHBOARD_PASS)
    if not (correct_username and correct_password):
        from fastapi import HTTPException, status
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized", headers={"WWW-Authenticate": "Basic"})
    return True

@app.get("/", response_class=HTMLResponse)
def dashboard(request: Request, authenticated: bool = Depends(check_auth)):
    # fetch current signals, news, logs, etc.
    signals = []
    news = []
    return templates.TemplateResponse("dashboard.html", {"request": request, "signals": signals, "news": news})
