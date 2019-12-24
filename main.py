from factories.NotificationMethodFactory import NotificationMethodFactory

notificationMethodFactory = NotificationMethodFactory()

telegram = notificationMethodFactory.make_notification_method('telegram')
if telegram is not None:
    telegram.send("Hello world")

whatsapp = notificationMethodFactory.make_notification_method('whatsapp')
if whatsapp is not None:
    whatsapp.send("Hello world")

xyz = notificationMethodFactory.make_notification_method('xyz')
if xyz is not None:
    xyz.send("Hello world")

# missing/wrong method name
missing = notificationMethodFactory.make_notification_method('missing')
if missing is not None:
    missing.send("Hello world")
