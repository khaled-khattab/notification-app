from notifications.NotificationMethod import NotificationMethod


class XYZ(NotificationMethod):

    def send(self, message):
        print('Sending notification via XYZ')
        print('XYZ: ' + message)
        print('---------------------------------')
