import random
from pushbullet import Pushbullet
from dotenv import load_dotenv
import os

load_dotenv()

def generate_password(length=8):
    return ''.join(random.choice("0123456789") for _ in range(length))

def save_password(password, file_path="password.txt"):
    with open(file_path, "w") as file:
        file.write(password)

def send_push_notification(password):
    access_token = os.getenv('PUSHBULLET_TOKEN')
    pb = Pushbullet(access_token)
    title = "Random 8-Digit Password"
    message = f"Your new password is: {password}"
    pb.push_note(title, message)

if __name__ == "__main__":
    password = generate_password()
    save_password(password)
    send_push_notification(password)