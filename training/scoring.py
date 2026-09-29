class Score:
    def __init__(self):
        self.total = 0
        self.checkpoint_points = 0
        self.landing_points = 0
        self.flight_points = 0
        self.penalty_points = 0

    def add_checkpoint_points(self, points):
        self.checkpoint_points += points
        self.total += points

    def add_landing_points(self, points):
        self.landing_points += points
        self.total += points

    def add_flight_points(self, points):
        self.flight_points += points
        self.total += points

    def add_penalty(self, points):
        self.penalty_points += points
        self.total -= points

    def reset(self):
        self.total = 0
        self.checkpoint_points = 0
        self.landing_points = 0
        self.flight_points = 0
        self.penalty_points = 0