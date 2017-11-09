import tkinter as tk
import RPi.GPIO as GPIO
import time
import socket
import sys


def getButton():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    while True:
        input_state = GPIO.input(18)
        if input_state == False:
            on_start_alarm()
            break


def on_start_alarm():
    start.configure(state="disabled")
    global alarm_id
    alarm_id = root.after(10000, start_alarm)
    alarm.configure(text="Alarm start binnen 10 seconden,\n druk op 'Reset alarm' om te annuleren.")


def on_stop_alarm():
    global alarm_id
    alarm.configure(text="", foreground="black")
    root.after_cancel(alarm_id)
    start.configure(state="normal")


def start_alarm():
    alarm.configure(text='Alarm! Alarm!', foreground="red")
    HOST, PORT = "192.168.43.136", 9999
    data = " ".join(sys.argv[1:])
    # Create a socket (SOCK_STREAM means a TCP socket)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("pressed")
    try:
        # Connect to server and send data
        sock.connect((HOST, PORT))
        # sock.sendall(data + "\n")

    finally:
        sock.close()


root = tk.Tk()
root.title("Alarm systeem - Client")
root.geometry("800x300")

alarm = tk.Label(root, text="", width=20)
start = tk.Button(root, text="Zet alarm aan", command=getButton)
stop = tk.Button(root, text="Reset alarm", command=on_stop_alarm)

alarm.pack(side="top", fill="both", expand=True)
start.pack()
stop.pack()

root.mainloop()