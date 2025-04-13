class Car(object):
    def __init__(self, model=None):
        self.model = model


class AdvancedCar(Car):
    def __init__(self, model='SUV', enable_auto_run=False, passwd='123'):
        super().__init__(model)
        self._enable_auto_run = enable_auto_run
        self.passwd = passwd

    @property
    def enable_auto_run(self):
        return self._enable_auto_run

    @enable_auto_run.setter
    def enable_auto_run(self, is_enabled):
        if self.passwd == '456':
            self._enable_auto_run = is_enabled
        else:
            raise ValueError


addvanced_car = AdvancedCar('SUV', passwd='456')
addvanced_car.enable_auto_run = True
print(addvanced_car.enable_auto_run)
