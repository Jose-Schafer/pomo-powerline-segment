# vim:fileencoding=utf-8:noet
"""
    USE THIS FILE TO DEBUG ERRORS IN CONFIGURATION.

    If everyhting going well don't forget to run:
        > powerline-daemon --replace
"""

from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import re
import datetime


class PomoTimer(object):
    def __init__(self):
        patterns = ["*"]
        ignore_patterns = None
        ignore_directories = True
        case_sensitive = True
        self.my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)
        self.my_event_handler.on_created = self.on_created
        path = "/home/krypton/.config/powerline/python_pomo/"
        go_recursively = True
        my_observer = Observer()
        my_observer.schedule(self.my_event_handler, path, recursive=go_recursively)
        my_observer.start()

    def on_created(self, event):
        print("on_create")
        if event.src_path == "/home/krypton/.config/powerline/python_pomo/pomo.txt":
            with open("/home/krypton/.config/powerline/python_pomo/pomo.txt") as f:
                command = re.sub('\n', '', f.readlines()[0])
            str_ = command
            comm_def_time = int(re.findall('\d+', str_)[0])
            self.now = datetime.datetime.now()
            self.pomo_length = datetime.timedelta(minutes=comm_def_time)


    def show_time(self):

        delta_time = (now + pomo_length - datetime.datetime.now())
        hours = str(divmod(delta_time.seconds, 3600)[0])
        minutes, seconds = divmod(delta_time.seconds, 60)
        minutes, seconds = str(minutes), str(seconds)
        timer = "{}:{}:{}".format(hours.zfill(2), minutes.zfill(2), seconds.zfill(2))

        timer_funcionando = delta_time.days == 0
        return timer

pomo = PomoTimer()
