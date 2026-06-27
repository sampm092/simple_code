import time
from plyer import notification

def start_notifier():
    print("🔔 Notification service started!")
    print("Press Ctrl + C at any time to DISABLE and exit the program.\n")
    
    # This variable acts as our toggle/disable switch
    is_enabled = True
    
    try:
        while is_enabled:
            # Send the desktop notification
            notification.notify(
                title="Reminder!",
                message="10 seconds have passed. Time to stretch!",
                app_name="Python Notifier",
                timeout=3  # How long the notification stays on screen (in seconds)
            )
            print("Notification sent. Waiting 10 seconds...")
            
            # Pause for 10 seconds
            time.sleep(10)
            
    except KeyboardInterrupt:
        # Catching Ctrl + C to gracefully disable the script
        is_enabled = False
        print("\n🛑 Service Disabled. Notifications stopped safely.")

if __name__ == "__main__":
    #Not really necessary for single python project
    start_notifier()