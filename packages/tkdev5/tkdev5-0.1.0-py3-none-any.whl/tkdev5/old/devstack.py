import tkinter as tk


class DevStack(tk.Frame):
    def __init__(self):
        """
        用于切换不同的界面
        """
        super(DevStack, self).__init__()
        self._pages = {}

    def add_page(self, page: tk.Widget, id: int = 0):
        """
        添加页面

        :param page: 页面组件
        :param id: 组件ID
        """
        self._pages[id] = page

    def show_page(self, id: int):
        """
        显示页面，会将其他页面隐藏

        :param id: 被显示的页面ID
        """
        self._pages[id].pack(fill=tk.BOTH, expand=tk.YES)
        for item in self._pages.keys():
            if not item == id:
                self.hide_page(item)

    def hide_page(self, id: int):
        """
        内置函数，最好不要使用，因为几乎没有什么用
        """
        self._pages[id].pack_forget()

    def get_page(self, id: int):
        """
        获取页面

        :param id: 所要获取的页面ID
        """
        return self._pages[id]

    def get_pages(self):
        """
        获取所有页面
        """
        return self._pages