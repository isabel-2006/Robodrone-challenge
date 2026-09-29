from ursina import Entity, color


class Drone:
    def __init__(self, position=(0, 5, 0)):
        # Main body
        self.body = Entity(
            model="cube",
            color=color.dark_gray,
            scale=(1.2, 0.25, 1.2),
            position=position
        )

        self.arms = []
        self.rotors = []

        # Four rotor positions
        rotor_positions = [
            (0.8, 0, 0.8),
            (-0.8, 0, 0.8),
            (0.8, 0, -0.8),
            (-0.8, 0, -0.8)
        ]

        for x, y, z in rotor_positions:

            # Arm
            arm = Entity(
                parent=self.body,
                model="cube",
                color=color.gray,
                scale=(0.8, 0.08, 0.08),
                position=(x * 0.5, 0, z * 0.5),
                rotation_y=45 if x * z > 0 else -45
            )

            # Rotor
            rotor = Entity(
                parent=self.body,
                model="cylinder",
                color=color.orange,
                scale=(0.45, 0.08, 0.45),
                position=(x, 0.15, z)
            )

            self.arms.append(arm)
            self.rotors.append(rotor)