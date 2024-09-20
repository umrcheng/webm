import uvicorn

from fastapi import FastAPI, Request
from fastapi.exceptions import HTTPException
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles
from starlette.exceptions import HTTPException as StarletteHTTPException

from path.api import router as api_router
from path.video import router as player_router
from path.image import router as image_router
from path.vue import router as vue_router

app = FastAPI()

# 添加中间件
app.add_middleware(
    CORSMiddleware,  # 显式指定类型
    allow_origins=["*"],  # 允许的源列表
    allow_credentials=True,  # 是否允许携带凭证
    allow_methods=["*"],  # 允许的方法，"*"表示所有HTTP方法
    allow_headers=["*"],  # 允许的头部，"*"表示所有头部
)

app.include_router(api_router)
app.include_router(player_router)
app.include_router(image_router)
app.include_router(vue_router)

# 配置静态文件目录
app.mount("/assets", StaticFiles(directory="templates/assets"))


@app.get("/")
async def root():
    return FileResponse("templates/index.html")


# 自定义全局异常处理程序
@app.exception_handler(HTTPException)
async def http_exception_handler():
    # 定义全局的 HTTP 异常处理器
    return FileResponse("templates/error.html")


# 自定义404异常处理程序
@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request: Request, exc: StarletteHTTPException):
    if exc.status_code == 404:
        return FileResponse("templates/error.html")
    return request


# 启动 FastAPI 服务器
def run_uvicorn():
    uvicorn.run("main:app", host="0.0.0.0", port=80)
