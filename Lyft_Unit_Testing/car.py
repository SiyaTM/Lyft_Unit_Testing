from serviceable import Serviceable


class Car(Serviceable):
    def __init__(self, engine, battery, lightbulb, exhaust):
        self.engine = engine
        self.battery = battery
        self.lightbulb = lightbulb
        self.exhaust = exhaust

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service() or self.lightbulb.needs_service() or self.exhaust.needs_service()
