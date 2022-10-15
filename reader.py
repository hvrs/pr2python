

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
class Handler(FileSystemEventHandler):
    def on_created(self, event):
        filename : str = event.src_path.replace("G:\\pythonProject\\", "").replace(".txt", "").lower()
        for char in filename:
            if char in "аиоуыэaeiouy":
                print(char)
            else:
                print(char.upper())
        print()





observer = Observer()
observer.schedule(Handler(), path="G:\\pythonProject\\")
observer.start()
try:
    while 1:
        pass
except KeyboardInterrupt:
    observer.stop()
    print("Handler stoped")