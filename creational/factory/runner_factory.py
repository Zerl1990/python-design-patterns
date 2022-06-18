from creational.factory.rabbit import Rabbit
from creational.factory.rturtle import RTurtle


class RunnerFactory:
    _X = -100
    _Y = 20

    @staticmethod
    def get_runner(runner_type: str):
        if runner_type == 'rabbit':
            return Rabbit(RunnerFactory._X, RunnerFactory._Y)
        else:
            return RTurtle(RunnerFactory._X, RunnerFactory._Y + 20)
