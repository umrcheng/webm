from fastapi import APIRouter, Request
from fastapi.responses import FileResponse
from fastapi.exceptions import HTTPException

from utli import path_processing

router = APIRouter(
    prefix="/api/image",
    tags=["image"]
)


@router.get('/')
async def get_image(request: Request):
    image_path = request.query_params.get("path")
    path = path_processing.path_cl(image_path)

    if type(path) == str:
        return FileResponse(path)
    else:
        raise HTTPException(status_code=404, detail=path)
