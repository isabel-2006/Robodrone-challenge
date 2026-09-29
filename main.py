from ursina import Ursina, camera, window, application

from config.settings import (
    WINDOW_TITLE,
    DRONE_START_POSITION,
    CAMERA_POSITION,
    CAMERA_LOOK_AT
)

from environment.world import create_world
from drone.drone import Drone


# Create Ursina application
app = Ursina()

# Set window title
window.title = WINDOW_TITLE

# Create the world
ground, sky = create_world()

# Create the drone
drone = Drone(position=DRONE_START_POSITION)

# Set camera position
camera.position = CAMERA_POSITION
camera.look_at(CAMERA_LOOK_AT)


# Handle keyboard input
def input(key):
    if key == "escape":
        application.quit()


# Start the application
app.run()