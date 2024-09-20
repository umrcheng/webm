from fastapi import APIRouter
from starlette.responses import FileResponse

router = APIRouter(
    prefix="",
    tags=["vue"],
)

"""
    这个页面的路由交给 vur-router 处理.
    交由Vue Router处理前端路由.
"""


@router.get("/image/")
async def res_image():
    return FileResponse("templates/index.html")


@router.get("/video/")
async def res_video():
    return FileResponse("templates/index.html")


@router.get("/player/")
async def res_player():
    return FileResponse("templates/index.html")


@router.get("/player/plyr")
async def res_player_plyr():
    return FileResponse("templates/index.html")


@router.get("/path")
async def res_path():
    return FileResponse("templates/index.html")


@router.get("/path/")
async def res_paths():
    return FileResponse("templates/index.html")
