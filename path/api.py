from fastapi import APIRouter, Request
from fastapi.exceptions import HTTPException

from utli import path_processing
from utli import file_processing
from utli.load import CONFIG

router = APIRouter(
    prefix="/api",
    tags=["api"],
)


@router.get("/dirs/show")
async def show_dir():
    data = []
    for item in CONFIG.get("path"):
        data.append({
            "name": path_processing.get_path_name(item),
            "type": "dir",
            "time": file_processing.get_file_time(item),
        })

    return data


@router.get("/dirs/show/path")
async def show_dir_path(request: Request):
    path = request.query_params.get("path")
    if path is None or "/" not in path:
        return []
    dir_name = path_processing.get_path_dir_and_file_name(path)["dir_name"]
    abs_path = path_processing.in_path(dir_name)
    if not abs_path:
        raise HTTPException(404)
    abs_path.replace(f"{dir_name}", "")

    data = path_processing.get_path_list(abs_path, path)
    for item in data:
        item.pop("path")

    return data
