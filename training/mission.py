class Mission:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.completed = False
        self.started = False

    def start(self):
        self.started = True

    def update(self):
        pass

    def complete(self):
        self.completed = True


class MissionManager:
    def __init__(self):
        self.missions = []
        self.current_mission = None

    def add_mission(self, mission):
        self.missions.append(mission)

    def start_mission(self, mission):
        self.current_mission = mission
        mission.start()

    def update(self):
        if self.current_mission:
            self.current_mission.update()

    def reset(self):
        self.current_mission = None
        for mission in self.missions:
            mission.started = False
            mission.completed = False