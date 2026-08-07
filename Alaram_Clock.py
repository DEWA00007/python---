# Python Alarm Clock:
import time
import datetime
import pygame  # For sound effect 


def set_alarm(alarm_time):
    print(f"Alarm set for : {alarm_time}")
    sound_file = "song.mp3"
    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        if current_time == alarm_time:
            print("WAKE UP !🧑‍🎤")

            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)
                ask_user=input("DO you want to off it (y/n)").capitalize()
                if ask_user == 'Y':
                    break
                

            is_running = False

        time.sleep(1) # this shows the time running in like stop watch
       

if __name__ == "__main__":
    alarm_time = input("Enter the alarm time(HH:MM:SS): ")
    set_alarm(alarm_time)



