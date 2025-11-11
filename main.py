import webview
import time
import threading

class StopwatchAPI:
    def __init__(self):
        self.running = False
        self.start_time = 0
        self.elapsed_time = 0

    def start(self):
        if not self.running:
            self.running = True
            self.start_time = time.time() - self.elapsed_time
            threading.Thread(target=self.update_time).start()

    def stop(self):
        self.running = False

    def reset(self):
        self.running = False
        self.elapsed_time = 0
        return 0

    def update_time(self):
        while self.running:
            self.elapsed_time = time.time() - self.start_time
            time.sleep(0.1)

    def get_time(self):
        return round(self.elapsed_time, 2)

if __name__ == '__main__':
    api = StopwatchAPI()
    window = webview.create_window('Stopwatch', 'web/index.html', js_api=api, width=300, height=250)
    webview.start()
