from ursina import Entity, Sky, color


def create_world():
    ground = Entity(
        model="plane",
        scale=(100, 1, 100),
        texture="white_cube",
        texture_scale=(50, 50),
        color=color.rgb(80, 140, 80)
    )

    sky = Sky()

    return ground, sky