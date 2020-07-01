#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import time
import sys
from load import import_json
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class WatchDir(object):
    def __init__(self, path):
        self.observer = Observer()
        self.watch_path = path

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.watch_path, recursive=True)
        self.observer.start()

        try:
            while True:
                time.sleep(5)
        except KeyboardInterrupt:
            self.observer.stop()
            print("Observer stopped")

        self.observer.join()

class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            print("Received event for directory: {}".format(event.src_path))
            return None

        if event.event_type == 'created':
            print("Recieved create event: {}".format(event.src_path))
            if event.src_path.endswith(".json"):
                import_json(event.src_path)
        elif event.event_type == 'modified':
            print("Received modified event: {}".format(event.src_path))
            if event.src_path.endswith(".json"):
                import_json(event.src_path)
        else:
            print("Received event type: {} - src: {}".format(event.event_type, event.src_path))


if __name__ == '__main__':
    watch = WatchDir(sys.argv[1] if len(sys.argv) > 1 else '.')
    watch.run()
