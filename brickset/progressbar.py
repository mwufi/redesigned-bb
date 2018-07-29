import time


class ProgressBar:
    def __init__(self, total):
        self.width = 100
        self.total = total

        self.start()

    def start(self):
        self.start = time.time()
        self.i = 0

    def update(self, number):
        ratio = int(number) / self.total
        elapsed = time.time() - self.start
        eta = elapsed / ratio

        arrow = "=" * int(ratio * self.width) + "=>"
        self.i += 1
        if self.i % 5== 0:
            print(arrow + "{} {:2f} eta: {:2f}".format(ratio, elapsed, eta))
