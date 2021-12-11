from nonebot import on_command
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Bot, MessageEvent, GroupMessageEvent, MessageSegment
from utils.utils import get_message_text
from services.log import logger
import requests
from nonebot.permission import SUPERUSER
from .pandalearning import main_handler
from .path import plugin_path
import os
from utils.message_builder import image
from utils.image_utils import CreateImg
import time
from pathlib import Path
import asyncio
from async_timeout import timeout

__zx_plugin_name__ = "xxqg_helper"
__plugin_usage__ = """
usage：
    学习强国
    指令：
        学习强国: 自动学习强国
        示例：学习强国
""".strip()
__plugin_des__ = "学习强国的事情就交给真寻吧！"
__plugin_cmd__ = ["学习强国"]
__plugin_version__ = 0.1
__plugin_author__ = "Gaze"
__plugin_settings__ = {
    "level": 5,
    "default_status": True,
    "limit_superuser": False,
    "cmd": ["学习强国"],
}


xxqg = on_command("学习强国", priority=1, permission=SUPERUSER, block=True)


@xxqg.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    path = f'{plugin_path}qrcode/qrcode.png'
    cookie_path = "user/cookies.json"
    if os.path.exists(cookie_path):
        os.remove(cookie_path)
    if os.path.exists(path):
        os.remove(path)
    async with timeout(120) as cm:
        main_handler()
    await asyncio.sleep(5)
    if os.path.exists(path):
        await xxqg.send(image(abspath=path))
    msg = "开始学习强国"
    await xxqg.finish(msg, at_sender=True)
    logger.info(
        f"(USER {event.user_id}, "
        f"GROUP {event.group_id if isinstance(event, GroupMessageEvent) else 'private'}) 学习强国：{msg}"
    )