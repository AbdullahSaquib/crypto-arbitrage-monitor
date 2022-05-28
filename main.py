from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.responses import FileResponse
import httpx
import asyncio


app = FastAPI()


@app.get("/")
async def home():
    return FileResponse("static/app.html")


@app.get("/kucoin")
async def get_kucoin():
    async with httpx.AsyncClient() as client:
        r = await asyncio.gather(
            client.post("https://api.kucoin.com/api/v1/bullet-public")
        )
        data = r[0].json()["data"]
        return {
            "token": data["token"],
            "ws_url": data["instanceServers"][0]["endpoint"]
        }
