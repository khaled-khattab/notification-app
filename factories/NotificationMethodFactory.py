from notifications.Telegram import Telegram
from notifications.Whatsapp import Whatsapp
from notifications.XYZ import XYZ


class NotificationMethodFactory:

    def make_notification_method(self, notification_method):
        notification_methods = self.get_notification_methods()
        if notification_method in notification_methods:
            return notification_methods[notification_method]
        else:
            # Here we may log that the sent notification method not exist
            print('Error: notification method "'+notification_method+'" not exists')
            print('---------------------------------')
            return None

    def get_notification_methods(self):
        return {"telegram": Telegram(), "whatsapp": Whatsapp(), "xyz": XYZ()}
