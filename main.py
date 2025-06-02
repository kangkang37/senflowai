from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

app = FastAPI(title="SenFlow Technologies")

# Mount static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set template directory
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "title": "SenFlow Technologies - Intelligent Software Solutions"}
    )

@app.get("/products", response_class=HTMLResponse)
async def products(request: Request):
    return templates.TemplateResponse(
        "products.html",
        {"request": request, "title": "Products & Services"}
    )

@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse(
        "about.html",
        {"request": request, "title": "About Us"}
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 