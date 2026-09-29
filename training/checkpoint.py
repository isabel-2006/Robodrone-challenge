class Checkpoint:
    def __init__(self, checkpoint_id, position, radius=2.0):
        self.checkpoint_id = checkpoint_id
        self.position = position
        self.radius = radius
        self.completed = False

    def check_drone(self, drone_position):
        pass

    def complete(self):
        self.completed = True

    def reset(self):
        self.completed = False


class CheckpointManager:
    def __init__(self):
        self.checkpoints = []
        self.current_index = 0

    def add_checkpoint(self, checkpoint):
        self.checkpoints.append(checkpoint)

    def get_current_checkpoint(self):
        if self.current_index < len(self.checkpoints):
            return self.checkpoints[self.current_index]

        return None

    def advance(self):
        if self.current_index < len(self.checkpoints):
            self.checkpoints[self.current_index].complete()
            self.current_index += 1

    def reset(self):
        self.current_index = 0

        for checkpoint in self.checkpoints:
            checkpoint.reset()