import os
from tkdev5.acrylic.acrylic import WindowEffect


acrylic_dLL = os.path.dirname(__file__).replace("\\", "//") + "//acrylic.dll"


class _Acrylic(object):
    def enable_acrylic(self, hwnd):
        from ctypes import cdll
        from ctypes.wintypes import HWND, DWORD

        hWnd = HWND(hwnd)
        gradient_color = DWORD(0x50F2F2F2)
        cdll.LoadLibrary(acrylic_dLL).setBlur(hWnd, gradient_color)


class DevAcrylicEffect(_Acrylic):

    from tkinter import Widget

    def enable(self, widget: Widget):
        from ctypes import windll

        self.enable_acrylic(windll.user32.GetParent(widget.winfo_id()))


class DevAcrylicEffect2(WindowEffect):

    from tkinter import Widget

    def enable(self, widget: Widget):
        from win32gui import GetParent

        self.setAcrylicEffect(GetParent(widget.winfo_id()), )