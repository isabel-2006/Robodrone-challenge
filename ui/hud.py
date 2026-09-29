class HUD:
    def __init__(self):
        self.enabled = True

        self.altitude = 0.0
        self.speed = 0.0
        self.throttle = 0.0
        self.score = 0

    def show(self):
        self.enabled = True

    def hide(self):
        self.enabled = False

    def update(self, altitude, speed, throttle, score):
        self.altitude = altitude
        self.speed = speed
        self.throttle = throttle
        self.score = score