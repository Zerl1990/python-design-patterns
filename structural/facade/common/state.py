from enum import Enum


class State(Enum):
    NEW = "new"
    RUNNING = "Running"
    SLEEPING = "Sleeping"
    RESTART = "Restart"
    ZOMBIE = "Zombie"
