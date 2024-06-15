import uuid
from http.client import HTTPException
from pathlib import Path
from fastapi import FastAPI, File, UploadFile
from Data.categories import categories_storage
from Data.meals import meal_by_category
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from dotenv import load_dotenv

app = FastAPI()
load_dotenv()
# images folder
IMAGE_DIR = Path("images")
app.mount("/static", StaticFiles(directory="images"), name="static")


@app.get("/categories")
async def get_categories():
    return {"categories": categories_storage}


@app.get("/categories/{name}")
async def get_meals_by_category(name: str):
    if name in meal_by_category:
        return {"meals": meal_by_category[name]}
    else:
        raise HTTPException(status_code=404, detail="wrong category")


@app.get("/get-image/{image_name}")
async def get_image(image_name: str):
    file_image = f"{image_name}.jpg"
    file_path = IMAGE_DIR / file_image
    if file_path.exists():
        return FileResponse(file_path)
    else:
        raise HTTPException(status_code=404, detail="Image not found")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
