class Aircraft():
    def __init__(self, model, mass, speed, top):
        if isinstance(model, str):
            self._model = model
        else:
            raise TypeError('Неверный тип аргумента')
        if mass >= 0:
            self._mass = mass
        else:
            raise TypeError('Неверный тип аргумента')
        if speed >= 0:
            self._speed = speed
        else:
            raise TypeError('Неверный тип аргумента')

class PassengerAircraft(Aircraft):
    def __init__(self, model, mass, speed, top,chairs):
        super().__init__(model, mass, speed, top)
        if chairs >= 0:
            self._chairs = chairs
        else:
            raise TypeError('Неверный тип аргумента')

class WarPlane(Aircraft):
    def __init__(self, model, mass, speed, top, weapon):
        super().__init__(model, mass, speed, top)
        if isinstance(weapon, dict):
            self._weapon = weapon
        else:
            raise TypeError('неверный тип аргумента')