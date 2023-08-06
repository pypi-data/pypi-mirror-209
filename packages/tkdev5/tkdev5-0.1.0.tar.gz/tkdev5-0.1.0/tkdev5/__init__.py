from tkdev5.toast import DevSimpleNotifications, DevNotifications, DevTemplateType
from tkdev5.toast_advanced import DevToastBuilder
from tkdev5.winforms import DevUserWidget
from tkdev5.acrylic import DevAcrylicEffect, DevAcrylicEffect2
from tkdev5.method_sets import listbox_dnd_package, listbox_dnd_enable, window_dnd

from tkdev5.ttree import Tree
from tkdev5.old.devstack import DevStack

from tkdev5.tray import DevTray

from tkinter import Listbox, Tk


__all__ = [
    "DevTk",

    "DevNotification",
    "DevUserFormWidget",
    "DevAcrylicEffect",
    "DevAcrylicEffect2",

    "DevMinimalTreeView",

    "DevAdded",
    "DevTray",

]


class DevTk(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        from tkdev5.old.devicon import Icon_QuickFish

        self.wm_title("DevTk")
        self.wm_iconbitmap(Icon_QuickFish)


class DevMinimalTreeView(Tree):
    pass


class DevNotification(object):
    def __init__(self):
        self.toast = DevSimpleNotifications()

    def show_toast(self, title: str = "", content: str = "", added: str = "", id: str = "Python"):
        self.toast.show_message3(message=title, message2=content, message3=added, id=id)


class DevUserFormWidget(DevUserWidget):
    pass


class DevAdded(object):
    @staticmethod
    def listbox_dnd_enable(listbox: Listbox):
        """
        启用拖放列表框列表

        根据https://wiki.tcl-lang.org/page/Listbox+Drag-and-Drop文章修改而来

        Attributes:
            listbox (Listbox): 选择目标列表框
        """
        listbox_dnd_package()
        listbox.configure(selectmode="single")
        listbox_dnd_enable(listbox)

    @staticmethod
    def window_dnd():
        """
        无边框窗口拖放

        根据https://wiki.tcl-lang.org/page/Drag+and+Drop+a+Window文章修改而来
        """
        window_dnd()