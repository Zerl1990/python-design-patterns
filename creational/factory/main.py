from creational.factory.runner_factory import RunnerFactory

if __name__ == '__main__':
    target_distance = 400
    rabbit = RunnerFactory.get_runner('rabbit')
    turtle = RunnerFactory.get_runner('turtle')
    while rabbit.position < target_distance and turtle.position < target_distance:
        rabbit.run()
        turtle.run()
    input("Press any key to exit")
