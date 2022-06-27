import os
from structural.handson.controller.twitter_controller import TwitterController

if __name__ == "__main__":
    os.environ.setdefault("ADMIN", "True")
    controller = TwitterController()
    while True:
        controller.run()
