# module main

# system
import os

# web
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# mount the public directory to serve static files
app.mount("/static", StaticFiles(directory="public"), name="static")

@app.get("/")
async def read_root():
    """Serve the index.html file from the public folder"""
    return FileResponse("public/index.html")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv('PORT', 8081)))

    
