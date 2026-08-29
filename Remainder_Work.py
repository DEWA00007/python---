import time
from datetime import datetime
from win10toast import ToastNotifier

notifier = ToastNotifier()

STUDY_TIME = "9:18"

MESSAGE = "⏰ Time for study!"

print("Study Reminder is running...")
print(f"Study time: {STUDY_TIME}")

already_notified = False

while True:
    current_time = datetime.now().strftime("%H:%M")

    if current_time == STUDY_TIME and not already_notified:
        notifier.show_toast(
            "Study Reminder",
            MESSAGE,
            duration=10
        )

        already_notified = True

    if current_time != STUDY_TIME:
        already_notified = False

    time.sleep(1)
