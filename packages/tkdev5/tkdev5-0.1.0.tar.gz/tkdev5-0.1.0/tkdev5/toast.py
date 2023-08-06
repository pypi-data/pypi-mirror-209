from enum import IntEnum


class _ToastTemplateType(IntEnum):
    TOAST_IMAGE_AND_TEXT01 = 0
    TOAST_IMAGE_AND_TEXT02 = 1
    TOAST_IMAGE_AND_TEXT03 = 2
    TOAST_IMAGE_AND_TEXT04 = 3
    TOAST_TEXT01 = 4
    TOAST_TEXT02 = 5
    TOAST_TEXT03 = 6
    TOAST_TEXT04 = 7


class _NotificationSetting(IntEnum):
    ENABLED = 0
    DISABLED_FOR_APPLICATION = 1
    DISABLED_FOR_USER = 2
    DISABLED_BY_GROUP_POLICY = 3
    DISABLED_BY_MANIFEST = 4


class _Notifications(object):

    """
    在Windows10-11平台上发送通知消息框，winsdk.window.ui.notifications

    Attributes:
        template (_ToastTemplateType): 通知模板。默认模板适用于大部分系统版本，不要轻易修改
        xml (str): 通知xml布局。可以通过这个参数修改默认通知布局
    """

    def __init__(self, template=_ToastTemplateType.TOAST_TEXT01, xml: str = ""):
        from winsdk.windows.ui.notifications import Notification
        from winsdk.windows.ui.notifications import ToastNotificationManager
        self.notifications = Notification()
        self.notification_manager = ToastNotificationManager

        if template is not None:
            self.template = template
            self.toastxml = self.notification_manager.get_template_content(self.template)
        else:
            from winsdk.windows.data.xml.dom import XmlDocument
            self.toastxml = XmlDocument()
            self.toastxml.load_xml(xml)

    def load_xml(self, xml: str) -> None:
        self.toastxml.load_xml(xml)

    def get_xml(self):
        return self.toastxml.get_xml()

    from winsdk.windows.ui.notifications import ToastNotification

    def create_notification(self) -> ToastNotification:
        from winsdk.windows.ui.notifications import ToastNotification
        self._toast = ToastNotification(self.toastxml)
        return self._toast

    from winsdk.windows.ui.notifications import ToastNotifier

    def create_notifier(self, id: str = "Python") -> ToastNotifier:
        self._notifier = self.notification_manager.create_toast_notifier(id)
        return self._notifier

    def scheduled(self):
        from System import DateTime

    def show(self, notifier: ToastNotifier, notification: ToastNotification) -> None:
        notifier.show(notification)

    def hide(self, notifier: ToastNotifier, notification: ToastNotification) -> None:
        notifier.hide(notification)

    def update(self, notifier: ToastNotifier, notification: ToastNotification, id: str) -> None:
        notifier.update(notification, id)


class _SimpleNotifications(_Notifications):
    def message1(self, message: str = ""):
        self.load_xml(f"""
<toast>
    <visual>
        <binding template="ToastImageAndText01">
            <text id="01">{message}</text>
        </binding>
    </visual>
</toast>
        """)

    def message2(self, message: str = "", message2: str = ""):
        self.load_xml(f"""
<toast>
    <visual>
        <binding template="ToastImageAndText01">
            <text id="01">{message}</text>
            <text id="01">{message2}</text>
        </binding>
    </visual>
</toast>
        """)

    def message3(self, message: str = "", message2: str = "", message3: str = ""):
        self.load_xml(f"""
    <toast>
        <visual>
            <binding template="ToastImageAndText01">
                <text id="01">{message}</text>
                <text id="01">{message2}</text>
                <text id="01">{message3}</text>
            </binding>
        </visual>
    </toast>
            """)

    def show_message(self, id="Python", xml: str = ""):
        self.load_xml(xml)
        toast_notification = self.create_notification()
        toast_notifier = self.create_notifier(id)
        self.show(toast_notifier, toast_notification)

    def show_message1(self, id="Python", message: str = ""):
        self.message1(message)
        toast_notification = self.create_notification()
        toast_notifier = self.create_notifier(id)
        self.show(toast_notifier, toast_notification)

    def show_message2(self, id="Python", message: str = "", message2: str = ""):
        self.message2(message, message2)
        toast_notification = self.create_notification()
        toast_notifier = self.create_notifier(id)
        self.show(toast_notifier, toast_notification)

    def show_message3(self, id="Python", message: str = "", message2: str = "", message3: str = ""):
        self.message3(message, message2, message3)
        toast_notification = self.create_notification()
        toast_notifier = self.create_notifier(id)
        self.show(toast_notifier, toast_notification)


class DevNotifications(_Notifications):
    pass


class DevSimpleNotifications(_SimpleNotifications):
    pass


DevTemplateType = _ToastTemplateType


DevNotificationSetting = _NotificationSetting

if __name__ == '__main__':
    toast = DevSimpleNotifications()
    toast_notifier = toast.create_notifier(id="Python")
    print(toast_notifier.setting)
    toast_notification = toast.create_notification()
    toast.message2()
    toast.show(toast_notifier, toast_notification)
    print(toast.get_xml())
