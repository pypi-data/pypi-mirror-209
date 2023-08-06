""" For Markdown text """

import re
import tkinter

from .__main__ import Canvas


class Markdown:
    """ MD文本格式 """

    font: list = ['微软雅黑', 20]
    size: list = [60, 48, 40, 32, 24, 12]

    def __init__(self, text: str = '') -> None:
        """

        """
        self.text = text
        self.text_lis = []  # type: list[tkinter._CanvasItemId]

    def parse(self) -> None:
        """ 解析内容 """

    def configure(self, **kw) -> None:
        """ 修改 """

    def write(self, text) -> None:
        """ 写入文本 """

    def display(canvas: Canvas, x: float, y: float) -> None:
        """ 显示 """

    def destroy(self) -> None:
        """ 删除 """


def configure_default(**kw) -> None:
    """ 修改默认值 """
    for key, value in kw:
        setattr(Markdown, key, value)
