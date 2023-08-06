class DevTray(object):

    """
    通过tkwinico快速制作系统托盘。（tkwinico也是我做的，但是考虑到打包时会很麻烦，就没直接加入库里了，而是加入依赖项）
    """

    def default_event(self, Message, X, Y):
        if Message == "WM_RBUTTONDOWN":
            from tkinter import Menu, _default_root
            Menu = Menu(tearoff=False)
            Menu.add_command(label="Quit", command=_default_root.quit)
            Menu.tk_popup(X, Y)

    def create(self, icon=None, event=None):
        from tkwinico import taskbar, createfrom
        from tkinter import _default_root
        if icon is None:
            from tkwinico import load
            icon = load("application")
        else:
            icon = createfrom(icon)

        if event is None:
            event = self.default_event
        taskbar("add", icon, (_default_root.register(event), "%m", "%x", "%y"))

