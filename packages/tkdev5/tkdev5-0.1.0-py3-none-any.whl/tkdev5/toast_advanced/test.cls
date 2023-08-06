using Microsoft.Toolkit.Uwp.Notifications;
using Windows.UI.Notifications;

var toastContent = new ToastContent()
{
    Visual = new ToastVisual()
    {
        BindingGeneric = new ToastBindingGeneric()
        {
            Children =
            {
                new AdaptiveText()
                {
                    Text = "Time to wake up!"
                },
                new AdaptiveText()
                {
                    Text = "To prove you're awake, select which of the following fruits is yellow..."
                }
            }
        }
    },
    Actions = new ToastActionsCustom()
    {
        Inputs =
        {
            new ToastSelectionBox("answer")
            {
                DefaultSelectionBoxItemId = "wrongDefault",
                Items =
                {
                    new ToastSelectionBoxItem("wrong", "Orange"),
                    new ToastSelectionBoxItem("wrongDefault", "Blueberry"),
                    new ToastSelectionBoxItem("right", "Banana"),
                    new ToastSelectionBoxItem("wrong", "Avacado"),
                    new ToastSelectionBoxItem("wrong", "Cherry")
                }
            }
        },
        Buttons =
        {
            new ToastButtonSnooze(),
            new ToastButton("Dismiss", "dismiss")
            {
                ActivationType = ToastActivationType.Background
            }
        }
    },
    Launch = "action=viewAlarm&alarmId=3",
    Scenario = ToastScenario.Alarm
};

// Create the toast notification
var toastNotif = new ToastNotification(toastContent.GetXml());

// And send the notification
ToastNotificationManager.CreateToastNotifier().Show(toastNotif);