from notifications.NotificationMethod import NotificationMethod


class Whatsapp(NotificationMethod):

    def send(self, message):
        print('Sending notification via Whatsapp')
        print('Whatsapp: ' + message)
        print('---------------------------------')
