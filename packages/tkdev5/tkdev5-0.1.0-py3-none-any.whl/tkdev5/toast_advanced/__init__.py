from clr import AddReference
from os.path import abspath, dirname

path = dirname(abspath(__file__))


Microsoft_Toolkit_Uwp_Notifications = path.replace("\\", "//") + "//Microsoft.Toolkit.Uwp.Notifications.dll"


def _add_uwp_notifications():
    AddReference(Microsoft_Toolkit_Uwp_Notifications)


class _ToastBuilder(object):
    def __init__(self):
        _add_uwp_notifications()

        from Microsoft.Toolkit.Uwp.Notifications import ToastContent, ToastVisual, ToastBindingGeneric, AdaptiveText, ToastActionsCustom, ToastButton, ToastContentBuilder

        self.notifications_visual = ToastVisual()
        self.notifications_binding_generic = ToastBindingGeneric()
        self.notifications_visual.BindingGeneric = self.notifications_binding_generic

        self.notifications_actions = ToastActionsCustom()

        self.notifications_content = ToastContent()

        self.notifications_content.Visual = self.notifications_visual
        self.notifications_content.Content = self.notifications_content

        self.notifications_toast_builder = ToastContentBuilder()

    def create_button_action(self):
        from Microsoft.Toolkit.Uwp.Notifications import ToastButton
        _button = ToastButton()
        return _button

    def add_action(self, action):
        self.notifications_actions.Buttons.Add(action)

    from winsdk.windows.data.xml.dom import XmlDocument

    def add_builder_text(self, content: str = "", id="01"):
        self.notifications_toast_builder.AddText(content, Id=id)

    def get_xml_dom(self) -> XmlDocument:
        from winsdk.windows.data.xml.dom import XmlDocument
        dom = XmlDocument()
        dom.load_xml(self.notifications_content.GetXml().GetXml())
        return dom

    def get_xml(self) -> str:
        return self.get_xml_dom().get_xml()

    def get_builder_xml_dom(self) -> XmlDocument:
        from winsdk.windows.data.xml.dom import XmlDocument
        dom = XmlDocument()
        dom.load_xml(self.notifications_toast_builder.GetXml().GetXml())
        return dom

    def get_builder_xml(self) -> str:
        return self.get_builder_xml_dom().get_xml()


class DevToastBuilder(_ToastBuilder):
    pass


if __name__ == '__main__':
    notifications = DevToastBuilder()
    notifications.notifications_toast_builder.AddText("Featured image of the day.")
    print(notifications.notifications_toast_builder.GetXml().GetXml())