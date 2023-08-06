from fastapi import FastAPI
import uvicorn

description = """
"""

version = "1.0.1"


app = FastAPI(title="pyappi", description=description, version=version)

@app.get("/pyappi/{version}/{mode}/{document}")
async def pyappi_get_document():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, log_level="info")