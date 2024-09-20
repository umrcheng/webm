import sys
import os
import pystray
import threading
from PIL import Image
from main import run_uvicorn

# 将标准输出和错误输出重定向到 os.devnull (类似 /dev/null)
sys.stdout = open(os.devnull, 'w')
sys.stderr = open(os.devnull, 'w')


# 创建一个简单的图标
def create_icon():
    image = Image.open("templates/vite.png")
    return image


# 定义菜单项
def on_quit(icon, item):
    icon.stop()


# 主函数
def main():
    # 创建图标
    icon = pystray.Icon('webm', create_icon(), title='webm服务')

    # 添加菜单项
    menu = pystray.Menu(
        pystray.MenuItem('webm', None),
        pystray.MenuItem('退出', on_quit),
    )

    # 设置菜单
    icon.menu = menu

    # 在新线程中启动 uvicorn
    server_thread = threading.Thread(target=run_uvicorn)
    server_thread.daemon = True
    server_thread.start()

    # 运行图标
    icon.run()


if __name__ == '__main__':
    main()
