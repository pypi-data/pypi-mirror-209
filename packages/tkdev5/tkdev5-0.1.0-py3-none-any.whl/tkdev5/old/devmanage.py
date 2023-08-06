import ctypes
from win32gui import *
from win32con import *
import tkinter as tk

from ctypes import POINTER, Structure, windll
from ctypes.wintypes import DWORD, ULONG, BOOL, HRGN
from enum import Enum


class AccentState(Enum):
    ACCENT_DISABLED = 0,
    ACCENT_ENABLE_GRADIENT = 1,
    ACCENT_ENABLE_TRANSPARENTGRADIENT = 2,
    ACCENT_ENABLE_BLURBEHIND = 3,
    ACCENT_ENABLE_ACRYLICBLURBEHIND = 4,
    ACCENT_INVALID_STATE = 5,


class WindowComPositionAttribute(Enum):
    WCA_UNDEFINED = 0,
    WCA_NCRENDERING_ENABLED = 1,
    WCA_NCRENDERING_POLICY = 2,
    WCA_TRANSITIONS_FORCEDISABLED = 3,
    WCA_ALLOW_NCPAINT = 4,
    WCA_CAPTION_BUTTON_BOUNDS = 5,
    WCA_NONCLIENT_RTL_LAYOUT = 6,
    WCA_FORCE_ICONIC_REPRESENTATION = 7,
    WCA_EXTENDED_FRAME_BOUNDS = 8,
    WCA_HAS_ICONIC_BITMAP = 9,
    WCA_THEME_ATTRIBUTES = 10,
    WCA_NCRENDERING_EXILED = 11,
    WCA_NCADORNMENTINFO = 12,
    WCA_EXCLUDED_FROM_LIVEPREVIEW = 13,
    WCA_VIDEO_OVERLAY_ACTIVE = 14,
    WCA_FORCE_ACTIVEWINDOW_APPEARANCE = 15,
    WCA_DISALLOW_PEEK = 16,
    WCA_CLOAK = 17,
    WCA_CLOAKED = 18,
    WCA_ACCENT_POLICY = 19,
    WCA_FREEZE_REPRESENTATION = 20,
    WCA_EVER_UNCLOAKED = 21,
    WCA_VISUAL_OWNER = 22,
    WCA_LAST = 23


class DWM_BLURBEHIND(ctypes.Structure):
    _fields_ = [
        ('dwFlags', DWORD),
        ('fEnable', BOOL),
        ('hRgnBlur', HRGN),
        ('fTransitionOnMaximized', BOOL)
    ]


class DwmWindowAttribute(Enum):
    DWMWA_NCRENDERING_ENABLED = 1
    DWMWA_NCRENDERING_POLICY = 2
    DWMWA_TRANSITIONS_FORCEDISABLED = 3
    DWMWA_ALLOW_NCPAINT = 4
    DWMWA_CAPTION_BUTTON_BOUNDS = 5
    DWMWA_NONCLIENT_RTL_LAYOUT = 6
    DWMWA_FORCE_ICONIC_REPRESENTATION = 7
    DWMWA_FLIP3D_POLICY = 8
    DWMWA_EXTENDED_FRAME_BOUNDS = 9
    DWMWA_HAS_ICONIC_BITMAP = 10
    DWMWA_DISALLOW_PEEK = 11
    DWMWA_EXCLUDED_FROM_PEEK = 12
    DWMWA_CLOAK = 13
    DWMWA_CLOAKED = 14
    DWMWA_FREEZE_REPRESENTATION = 15
    DWMWA_PASSIVE_UPDATE_MODE = 16
    DWMWA_USE_HOSTBACKDROPBRUSH = 17
    DWMWA_USE_IMMERSIVE_DARK_MODE = 18
    DWMWA_WINDOW_CORNER_PREFERENCE = 19
    DWMWA_BORDER_COLOR = 20
    DWMWA_CAPTION_COLOR = 21
    DWMWA_TEXT_COLOR = 22
    DWMWA_VISIBLE_FRAME_BORDER_THICKNESS = 23
    DWMWA_LAST = 24


class DevManage(object):

    def __init__(self, master: tk.Tk):
        """
        用于管理窗口高级功能。

        :param master: 管理的组件。
        """
        self._master = GetParent(master.winfo_id())
        self._master_tk = master
        self.DwmApi = ctypes.windll.dwmapi
        self.Win32 = ctypes.windll.user32
        self.UXTheme = ctypes.windll.uxtheme
        self.Shcore = ctypes.windll.shcore
        self.DwmSetWindowAttribute = self.DwmApi.DwmSetWindowAttribute
        self.DwmGetWindowAttribute = self.DwmApi.DwmGetWindowAttribute
        self.DwmGetColorizationColor = self.DwmApi.DwmGetColorizationColor
        self.DwmEnableBlurBehindWindow = self.DwmApi.DwmEnableBlurBehindWindow
        self.DwmIsCompositionEnabled = self.DwmApi.DwmIsCompositionEnabled
        self.DwmExtendFrameIntoClientArea = self.DwmApi.DwmExtendFrameIntoClientArea
        self.DwmRegisterThumbnail = self.DwmApi.DwmRegisterThumbnail

        self.SetWindowCompositionAttribute = self.Win32.SetWindowCompositionAttribute

        self.DWMSBT_AUTO = 0
        self.DWMSBT_NONE = 1
        self.DWMSBT_MAINWINDOW = 2
        self.DWMSBT_TRANSIENTWINDOW = 3
        self.DWMSBT_TABBEDWINDOW = 4

        self.DWMNCRP_USEWINDOWSTYLE = 0
        self.DWMNCRP_DISABLED = 1
        self.DWMNCRP_ENABLED = 2
        self.DWMNCRP_LAS = 3

        self.DWMWCP_DEFAULT = 0
        self.DWMWCP_DONOTROUND = 1
        self.DWMWCP_ROUND = 2
        self.DWMWCP_ROUNDSMALL = 3

        self.ACCENT_DISABLED = 0,
        self.ACCENT_ENABLE_GRADIENT = 1,
        self.ACCENT_ENABLE_TRANSPARENTGRADIENT = 2,
        self.ACCENT_ENABLE_BLURBEHIND = 3,  # Aero效果
        self.ACCENT_ENABLE_ACRYLICBLURBEHIND = 4,  # 亚克力效果
        self.ACCENT_INVALID_STATE = 5

        self.DWM_BB_ENABLE = 0x00000001
        self.DWM_BB_BLURREGION = 0x00000002
        self.DWM_BB_TRANSITIONONMAXIMIZED = 0x00000004

        self.DWMWA_NCRENDERING_ENABLED = 1
        self.DWMWA_NCRENDERING_POLICY = 2
        self.DWMWA_TRANSITIONS_FORCEDISABLED = 3
        self.DWMWA_ALLOW_NCPAINT = 4
        self.DWMWA_CAPTION_BUTTON_BOUNDS = 5
        self.DWMWA_NONCLIENT_RTL_LAYOUT = 6
        self.DWMWA_FORCE_ICONIC_REPRESENTATION = 7
        self.DWMWA_FLIP3D_POLICY = 8
        self.DWMWA_EXTENDED_FRAME_BOUNDS = 9
        self.DWMWA_HAS_ICONIC_BITMAP = 10
        self.DWMWA_DISALLOW_PEEK = 11
        self.DWMWA_EXCLUDED_FROM_PEEK = 12
        self.DWMWA_CLOAK = 13
        self.DWMWA_CLOAKED = 14
        self.DWMWA_FREEZE_REPRESENTATION = 15
        self.DWMWA_PASSIVE_UPDATE_MODE = 16
        self.DWMWA_USE_HOSTBACKDROPBRUSH = 17
        self.DWMWA_CAPTION_COLOR = 19
        self.DWMWA_USE_IMMERSIVE_DARK_MODE = 20
        self.DWMWA_LAST = 24
        self.DWMWA_WINDOW_CORNER_PREFERENCE = 33
        self.DWMWA_BORDER_COLOR = 34
        self.DWMWA_TEXT_COLOR = 36
        self.DWMWA_VISIBLE_FRAME_BORDER_THICKNESS = 37
        self.DWMWA_SYSTEMBACKDROP_TYPE = 38

        self.DWMSC_DOWN = 0
        self.DWMSC_UP = 1
        self.DWMSC_DRAG = 2
        self.DWMSC_HOLD = 3
        self.DWMSC_PENBARREL = 4
        self.DWMSC_NONE = 5
        self.DWMSC_ALL = 6

        self.rgbRed = 0x000000FF
        self.rgbGreen = 0x0000FF00
        self.rgbBlue = 0x00FF0000
        self.rgbBlack = 0x00000000
        self.rgbWhite = 0x00FFFFFF

    def high_dpi(self):
        try:
            self.Shcore.SetProcessDpiAwareness(2)
        except:
            self.Win32.SetProcessDPIAware()
        ScaleFactor = self.Shcore.GetScaleFactorForDevice(0)
        self._master_tk.tk.call('tk', 'scaling', ScaleFactor / 75)

    def window_screenshot(self):
        from tkcap import CAP
        return CAP(self._master).capture(image_name)

    def dwm_set_window_attribute(self, type, attribute, size):
        """
        用于对非客户区进行设置。
        """
        self.DwmSetWindowAttribute(
            self._master,
            type,
            attribute,
            size
        )

    def dwm_get_window_attribute(self, type, size):
        """
        用于对非客户区进行设置。
        """
        return self.DwmGetWindowAttribute(
            self._master,
            type,
            size
        )

    def dwm_set_window_attribute_use_dark_mode(self):
        """
        设置窗口主题为黑暗模式，标题栏会有所改变。
        """
        Value = ctypes.c_int(2)
        self.dwm_set_window_attribute(
            self.DWMWA_USE_IMMERSIVE_DARK_MODE,
            ctypes.byref(Value),
            ctypes.sizeof(Value)
        )

    def dwm_get_window_attribute_use_dark_mode(self):
        """
        设置窗口主题为黑暗模式，标题栏会有所改变。
        """
        Value = ctypes.c_int(self.DWMWA_USE_IMMERSIVE_DARK_MODE)
        self.dwm_get_window_attribute(
            self.DWMWA_USE_IMMERSIVE_DARK_MODE,
            ctypes.sizeof(Value)
        )

    def dwm_set_window_attribute_use_light_mode(self):
        """
        设置窗口主题为明亮模式，标题栏会有所改变。
        """
        Value = ctypes.c_int(0)
        self.dwm_set_window_attribute(
            self.DWMWA_USE_IMMERSIVE_DARK_MODE,
            ctypes.byref(Value),
            ctypes.sizeof(Value)
        )

    def dwm_set_window_attribute_systembackdrop_type(self, type=1):
        Value = ctypes.c_int(type)
        self.dwm_set_window_attribute(self.DWMWA_SYSTEMBACKDROP_TYPE, ctypes.byref(Value), ctypes.sizeof(Value))

    def dwm_set_window_attribute_systembackdrop_type_auto(self):
        self.dwm_set_window_attribute_systembackdrop_type(self.DWMSBT_AUTO)

    def dwm_set_window_attribute_systembackdrop_type_none(self):
        self.dwm_set_window_attribute_systembackdrop_type(self.DWMSBT_NONE)

    def dwm_set_window_attribute_systembackdrop_type_mainwindow(self):
        self.dwm_set_window_attribute_systembackdrop_type(self.DWMSBT_MAINWINDOW)

    def dwm_set_window_attribute_systembackdrop_type_transient_window(self):
        self.dwm_set_window_attribute_systembackdrop_type(self.DWMSBT_TRANSIENTWINDOW)

    def dwm_set_window_attribute_systembackdrop_type_tabbed_window(self):
        self.dwm_set_window_attribute_systembackdrop_type(self.DWMSBT_TABBEDWINDOW)

    def dwm_set_window_attribute_visible_frame_border_thickness(self, value):
        self.Value = ctypes.c_int(value)
        self.dwm_set_window_attribute(self.DWMWA_VISIBLE_FRAME_BORDER_THICKNESS, ctypes.byref(self.Value),
                                      ctypes.sizeof(self.Value))

    def dwm_set_window_attribute_ncrendering_policy(self, value=2):
        Value = ctypes.c_int(value)
        self.dwm_set_window_attribute(self.DWMWA_NCRENDERING_POLICY,
                                      ctypes.byref(Value), ctypes.sizeof(Value))

    def dwm_set_window_attribute_border_color(self, color=0x00FF0000):
        Value = ctypes.c_int(color)
        self.dwm_set_window_attribute(self.DWMWA_BORDER_COLOR, ctypes.byref(Value), ctypes.sizeof(Value))

    def dwm_set_window_attribute_text_color(self, color=0x00FF0000):
        Value = ctypes.c_int(color)
        self.dwm_set_window_attribute(self.DWMWA_TEXT_COLOR, ctypes.byref(Value), ctypes.sizeof(Value))

    def dwm_set_window_attribute_caption_color(self, color=0x00FF0000):
        Value = ctypes.c_int(color)
        self.dwm_set_window_attribute(self.DWMWA_CAPTION_COLOR, ctypes.byref(Value), ctypes.sizeof(Value))

    def dwm_set_window_round(self, value):
        Value = ctypes.c_int(value)
        self.dwm_set_window_attribute(
            self.DWMWA_WINDOW_CORNER_PREFERENCE,
            ctypes.byref(Value),
            ctypes.sizeof(Value)
        )

    def dwm_set_window_round_default(self):
        self.dwm_set_window_round(self.DWMWCP_DEFAULT)

    def dwm_set_window_round_donot_round(self):
        self.dwm_set_window_round(self.DWMWCP_DONOTROUND)

    def dwm_set_window_round_round(self):
        self.dwm_set_window_round(self.DWMWCP_ROUND)

    def dwm_set_window_round_round_small(self):
        self.dwm_set_window_round(self.DWMWCP_ROUNDSMALL)

    def dwm_get_window_attribute(self, type, put):
        """
        获取非客户区的属性。
        """
        return self.DwmGetWindowAttribute(
            self._master,
            type,
            put
        )

    def dwm_get_colorization_color(self):
        return self.DwmGetColorizationColor()

    def dwm_enable_blurbehind_window(self, flags=0x00000001, enable: bool = True, rgn_blur=1,
                                     transition_on_maximized: bool = True):
        BlurBehid = DWM_BLURBEHIND()
        BlurBehid.dwFlags = flags
        BlurBehid.fEnable = enable
        BlurBehid.hRgnBlur = rgn_blur
        BlurBehid.TransitionOnMaximized = transition_on_maximized
        return self.DwmEnableBlurBehindWindow(self._master, ctypes.byref(BlurBehid))

    def dwm_is_composition_enabled(self):
        return self.DwmIsCompositionEnabled()

    def dwm_extend_frame_into_client_area(self, margins=[-1, -1, -1, -1]):
        Margins = MARGINS(margins[0], margins[1], margins[2], margins[3])
        return self.DwmExtendFrameIntoClientArea(self._master, ctypes.byref(Margins))

    def dwm_register_thumbnail(self, id):
        return self.DwmRegisterThumbnail(self._master, self.find_window("Program", NULL), id)

    def use_mica(self, is_dark=False):
        """
        使用Windows11的云母特效。

        :param is_dark: 用来设置是否是黑暗模式
        """
        from win32mica import ApplyMica
        return ApplyMica(self._master, is_dark)

    def use_mica_mode_light(self):
        """
        使用Windows11的云母特效。设置为明亮模式
        """
        return self.use_mica(False)

    def use_mica_mode_dark(self):
        """
        使用Windows11的云母特效。设置为暗黑模式
        """
        return self.use_mica(True)

    def use_mica_mode_auto(self):
        """
        使用Windows11的云母特效。主题会变成和系统一样颜色的。
        """
        import darkdetect
        if darkdetect.isLight():
            self.use_mica_mode_light()
        elif darkdetect.isDark():
            self.use_mica_mode_dark()

    def use_acrylic(self, is_dark=False, hex_color: bool = False, acrylic: bool = False):
        """
        使用Windows10的亚克力特效。

        :param is_dark: 用来设置是否是黑暗模式
        """
        from BlurWindow import blurWindow
        return blurWindow.GlobalBlur(self._master, Dark=is_dark, hexColor=hex_color, Acrylic=acrylic)

    def use_acrylic_mode_light(self, hex_color: bool = False, acrylic: bool = False):
        """
        使用Windows10的亚克力特效。设置为明亮模式
        """
        return self.use_acrylic(False, hex_color, acrylic)

    def use_acrylic_mode_dark(self, hex_color: bool = False, acrylic: bool = False):
        """
        使用Windows10的亚克力特效。设置为黑暗模式
        """
        return self.use_acrylic(True, hex_color, acrylic)

    def use_acrylic_mode_auto(self, hex_color: bool = False, acrylic: bool = False):
        """
        使用Windows10的亚克力特效。主题会变成和系统一样颜色的。
        """
        import darkdetect
        if darkdetect.isLight():
            self.use_acrylic_mode_light(hex_color, acrylic)
        elif darkdetect.isDark():
            self.use_acrylic_mode_dark(hex_color, acrylic)

    def update_window(self):
        """
        刷新窗口
        """
        return UpdateWindow(self._master)

    def enable_theming(self, bool: bool):
        return self.UXTheme.EnableTheming(bool)

    def find_window(self, Class, Name):
        return FindWindow(Class, Name)

    def set_master(self, master: tk.Tk):
        """
        设置组件的父组件。
        """
        SetParent(self._master, GetParent(master.winfo_id()))

    def set_window_text(self, text):
        return SetWindowText(self._master, text)

    def set_window_long(self, setting):
        """
        设置窗口样式
        """
        return SetWindowLong(self._master, GWL_STYLE, setting)

    def set_window_ex_long(self, setting):
        """
        设置窗口扩展样式
        """
        return SetWindowLong(self._master, GWL_EXSTYLE, setting)

    def set_window_pos(self, after, x, y, width, height, flags):
        SetWindowPos(self._master, after, x, y, width, height, flags)

    def set_window_pos_center(self):
        """
        将窗口放在屏幕中心。
        """
        x = self._master_tk.winfo_screenwidth() / 2 - self._master_tk.winfo_width() / 2
        y = self._master_tk.winfo_screenheight() / 2 - self._master_tk.winfo_height() / 2
        self._master_tk.geometry(
            f"{self._master_tk.winfo_width()}x{self._master_tk.winfo_height()}+{round(x)}+{round(y)}"
        )

    def set_window_pos_bottom_right(self, padx: int = 15, pady: int = 15):
        """
        将窗口放在右下位置，

        :param padx: 表示X间距
        :param pady: 表示Y间距
        """
        self._master_tk.after(1, lambda: self._master_tk.geometry(
            f"+{self._master_tk.winfo_screenwidth() - self._master_tk.winfo_width() - padx - 10}+"
            f"{self._master_tk.winfo_screenheight() - taskbar_height - self._master_tk.winfo_height() - pady - 35}"))

    def set_window_pos_bottom_left(self, padx: int = 15, pady: int = 15):
        """
        将窗口放在左下位置。

        :param padx: 表示X间距
        :param pady: 表示Y间距
        """
        self._master_tk.after(1, lambda: self._master_tk.geometry(
            f"+{padx}+{self._master_tk.winfo_screenheight() - taskbar_height - self._master_tk.winfo_height() - pady - 35}"))

    def set_window_pos_top_right(self, padx: int = 15, pady: int = 15):
        """
        将窗口放在右上位置。

        :param padx: 表示X间距
        :param pady: 表示Y间距
        """
        self._master_tk.after(1, lambda: self._master_tk.geometry(
            f"+{self._master_tk.winfo_screenwidth() - self._master_tk.winfo_width() - padx - 10}+{pady}"))

    def set_window_pos_top_left(self, padx: int = 15, pady: int = 15):
        """
        将窗口放在左上位置

        :param padx: 表示X间距
        :param pady: 表示Y间距
        """
        self._master_tk.after(1, lambda: self._master_tk.geometry(
            f"+{padx}+{pady}"))

    def get_window_long(self):
        return GetWindowLong(self._master, GWL_STYLE)

    def get_window_ex_long(self):
        return GetWindowLong(self._master, GWL_EXSTYLE)

    def add_window_popup(self):
        return self.add_window_long(WS_POPUP)

    def add_window_long(self, setting):
        return SetWindowLong(self._master, GWL_STYLE, self.get_window_long() & ~setting)

    def add_window_ex_long(self, setting):
        return SetWindowLong(self._master, GWL_EXSTYLE, self.get_window_ex_long() & ~setting)

    def add_window_popup_window(self):
        return self.add_window_long(WS_POPUPWINDOW)

    def add_window_init_minimize(self):
        return self.add_window_long(WS_MINIMIZE)

    def add_window_init_maximize(self):
        return self.add_window_long(WS_MAXIMIZE)

    def add_window_init_disable(self):
        return self.add_window_long(WS_DISABLED)

    def add_window_init_visible(self):
        return self.add_window_long(WS_VISIBLE)

    def add_window_sysmenu(self):
        return self.add_window_long(WS_SYSMENU)

    def add_window_toolwindow(self):
        return self.add_window_ex_long(WS_EX_TOOLWINDOW)

    def add_window_maximizebox(self):
        return self.add_window_long(WS_MAXIMIZEBOX)

    def add_window_minimizebox(self):
        return self.add_window_long(WS_MINIMIZEBOX)

    def add_window_caption(self):
        return self.add_window_long(WS_CAPTION)

    def add_window_titlebar(self):
        def titlebar():
            self.add_window_long(WS_CAPTION)
            self.set_window_pos(NULL, 0, 0, 0, 0, SWP_NOSIZE | SWP_NOMOVE | SWP_NOZORDER | SWP_DRAWFRAME)
            self.update_window()

        self._master_tk.after(100, lambda: titlebar())

    def add_window_border(self):
        return self.add_window_long(WS_BORDER)

    def add_window_dlg_frame(self):
        return self.add_window_long(WS_DLGFRAME)

    def add_window_think_frame(self):
        return self.add_window_long(WS_THICKFRAME)

    def add_window_resize_border_frame(self):
        return self.add_window_long(WS_THICKFRAME)

    def add_window_child(self):
        return self.add_window_long(WS_CHILD)

    def release_capture(self):
        """
        使用ReleaseCapture释放并捕捉数据
        """
        return ReleaseCapture()

    def send_message(self, window, message, wParam, lParam):
        """
        使用SendMessage发送消息给Window，

        :param window: 接收消息的窗口
        :param message: 为要发送的消息
        :param wParam: 附加项
        :param lParam: 附加项
        """
        return SendMessage(GetParent(window.winfo_id()), message, wParam, lParam)

    def send_message_move_window(self, window):
        """
        拖动当前控件移动参数window。

        :param window: 被拖动的窗口
        """

        def move():
            self.release_capture()
            self.send_message(window, WM_SYSCOMMAND, SC_MOVE + HTCAPTION, 0)

        self._master_tk.bind("<B1-Motion>", lambda event: move())

    def show_window(self, state):
        return ShowWindow(self._master, state)

    def show_window_hide(self):
        return self.show_window(SW_HIDE)

    def show_window_maximize(self):
        return self.show_window(SW_MAXIMIZE)

    def show_window_minimize(self):
        return self.show_window(SW_MINIMIZE)

    def show_window_restore(self):
        return self.show_window(SW_RESTORE)

    def show_window_show(self):
        return self.show_window(SW_SHOW)

    def show_window_show_maximize(self):
        return self.show_window(SW_SHOWMAXIMIZED)

    def show_window_show_minimize(self):
        return self.show_window(SW_SHOWMINIMIZED)

    def show_window_show_minno_action(self):
        return self.show_window(SW_SHOWMINNOACTIVE)

    def show_window_show_na(self):
        return self.show_window(SW_SHOWNA)

    def show_window_show_normal(self):
        return self.show_window(SW_SHOWNORMAL)

    def close_window(self):
        return CloseWindow(self._master)

    def minimize_window(self):
        return CloseWindow(self._master)

    def enable_window(self, bool: bool):
        return EnableWindow(self._master, bool)

    def destroy_window(self):
        return DestroyWindow(self._master)

    def destroy_icon(self):
        return DestroyIcon(self._master)

    def drag_accept_files(self, bool: bool):
        return DragAcceptFiles(self._master, bool)

    def drag_finish(self):
        return DragFinish()

    def draw_menubar(self):
        return DrawMenuBar(self._master)

    def create_menu(self):
        return CreateMenu()

    def set_menu(self, menu):
        return SetMenu(self._master,
                       menu)
