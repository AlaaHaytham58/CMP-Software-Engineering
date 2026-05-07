# ContentCreator class (Subject in the Observer Pattern)
class ContentCreator:
    def __init__(self, name):
        self.name = name
        self.followers = []  # List of User objects that follow this creator

    def add_follower(self, user):
        """Add a user to the followers list."""
        self.followers.append(user)
        print(f"{user.name} is now following {self.name}")

    def remove_follower(self, user):
        """Remove a user from the followers list."""
        if user in self.followers:
            self.followers.remove(user)
            print(f"{user.name} is no longer following {self.name}")

    def upload_content(self, content):
        """Notify all followers about the new content."""
        print(f"{self.name} has uploaded new content: {content}")
        # Use NotificationManager to notify each follower
        notification_manager = NotificationManager.get_instance()
        for follower in self.followers:
            notification_manager.send_notification(follower, self, content)

# User class (Observer in the Observer Pattern)
class User:
    def __init__(self, name):
        self.name = name

    def update(self, content_creator, content):
        """Receive notification of new content from a content creator."""
        print(f"{self.name} received notification: {content_creator.name} uploaded '{content}'")

# NotificationManager class (Singleton)
class NotificationManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(NotificationManager, cls).__new__(cls)
        return cls._instance

    @staticmethod
    def get_instance():
        """Static access method."""
        if NotificationManager._instance is None:
            NotificationManager._instance = NotificationManager()
        return NotificationManager._instance

    def send_notification(self, user, content_creator, content):
        """Send a notification to the user."""
        user.update(content_creator, content)

# Decorator classes for different notification channels
class NotificationChannelDecorator(User):
    """Base class for notification channel decorators."""
    def __init__(self, user):
        self.user = user

    @property
    def name(self):
        """Access the name of the wrapped user."""
        return self.user.name

    def update(self, content_creator, content):
        """Call the update method of the wrapped User object."""
        self.user.update(content_creator, content)

class EmailNotificationDecorator(NotificationChannelDecorator):
    def update(self, content_creator, content):
        """Send email notification in addition to the regular update."""
        super().update(content_creator, content)
        print(f"Email sent to {self.name}: {content_creator.name} uploaded '{content}'")

class SMSNotificationDecorator(NotificationChannelDecorator):
    def update(self, content_creator, content):
        """Send SMS notification in addition to the regular update."""
        super().update(content_creator, content)
        print(f"SMS sent to {self.name}: {content_creator.name} uploaded '{content}'")

class PushNotificationDecorator(NotificationChannelDecorator):
    def update(self, content_creator, content):
        """Send push notification in addition to the regular update."""
        super().update(content_creator, content)
        print(f"Push notification sent to {self.name}: {content_creator.name} uploaded '{content}'")

# Example usage
def main():
    # Creating ContentCreators
    creator1 = ContentCreator("Music Channel")
    creator2 = ContentCreator("Vlog Channel")

    # Creating Users
    user1 = User("Alice")
    user2 = User("Bob")

    # Users follow creators with different notification channels
    # Alice & Bob follow creator1. Alice gets email notifications, Bob gets SMS and Push notifications
    creator1.add_follower(EmailNotificationDecorator(user1))
    creator1.add_follower(PushNotificationDecorator(SMSNotificationDecorator(user2)))
    
    # Alice follows creator2. She receives regular notifications (no decorators)
    creator2.add_follower(user1)

    # Simulating content upload
    creator1.upload_content("New Song Release!")
    creator2.upload_content("Day in My Life Vlog")


if __name__ == "__main__":
    main()

if __name__ == "__main__": 
    main()