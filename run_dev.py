import os
import sys
import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class RestartHandler(FileSystemEventHandler):
    def __init__(self, command):
        super().__init__()
        self.command = command
        self.process = None
        self.start_process()

    def start_process(self):
        if self.process:
            self.process.terminate()
        self.process = subprocess.Popen([sys.executable] + self.command)

    def on_any_event(self, event):
        if event.is_directory:
            return
        if event.src_path.endswith(".py"):
            print("🔁 File change detected — restarting app...")
            self.start_process()

if __name__ == "__main__":
    path = "."
    command = ["main.py"]

    handler = RestartHandler(command)
    observer = Observer()
    observer.schedule(handler, path, recursive=True)
    observer.start()

    print("👀 Watching for changes... (Press Ctrl+C to stop)")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        if handler.process:
            handler.process.terminate()

    observer.join()
