class Car(object):
    def __init__(self, model=None):
        self.model = model


class AdvancedCar(Car):
    def __init__(self, model='SUV', enable_auto_run=False):
        super().__init__(model)
        self._enable_auto_run = enable_auto_run

    @property
    def enable_auto_run(self):
        return self._enable_auto_run


addvanced_car = AdvancedCar('SUV')
print(addvanced_car._enable_auto_run)
