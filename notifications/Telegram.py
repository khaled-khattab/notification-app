from notifications.NotificationMethod import NotificationMethod


class Telegram(NotificationMethod):

    def send(self, message):
        print('Sending notification via Telegram')
        print('Telegram: ' + message)
        print('---------------------------------')
