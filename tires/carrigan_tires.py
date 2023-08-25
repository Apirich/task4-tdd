from tires.tires import Tires

class CarriganTires(Tires):
    def __init__(self, tires_sensors):
        self.tires_sensors = tires_sensors

    def needs_service(self):
        for i in self.tires_sensors:
            if i >= 0.9:
                return True
        return False

