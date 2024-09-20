from fastapi import APIRouter, Request
from fastapi.exceptions import HTTPException
from fastapi.responses import StreamingResponse
from os.path import getsize

import mimetypes

from utli import path_processing

router = APIRouter(
    prefix="/api/video",
    tags=["video"],
)


@router.get("/")
async def get_video(request: Request):
    video_path = request.query_params.get("path")
    video_path = path_processing.path_cl(video_path)

    if type(video_path) == dict:
        raise HTTPException(status_code=404, detail=video_path)

    video_size = getsize(video_path)
    mimetype = mimetypes.guess_type(video_path)[0]

    headers = request.headers
    start = 0
    end = video_size - 1

    range_header = headers.get("Range")
    if range_header:
        ranges = range_header.replace("bytes=", "").split("-")
        start = int(ranges[0]) if ranges[0] else start
        end = int(ranges[1]) if ranges[1] else end

    length = end - start + 1

    headers = {
        "Content-Range": f"bytes {start}-{end}/{video_size}",
        "Accept-Ranges": "bytes",
        "Content-Length": str(length),
        "Content-Type": mimetype,
        # "Access-Control-Allow-Origin": "*",
        # "Access-Control-Allow-Methods": "GET",
        # "Access-Control-Allow-Headers": "Content-Type",
    }

    return StreamingResponse(generate_video(start, video_path), status_code=206, media_type=mimetype, headers=headers)


def generate_video(start, video_path):
    with open(video_path, "rb") as file:
        file.seek(start)
        while True:
            data = file.read(1024 * 1024 * 10)  # 一次读取 多少 字节数据
            if not data:
                break
            yield data
