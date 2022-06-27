from structural.handson.access_manager.decorator import admin


class TwitterTerminalView:
    def __init__(self):
        self.name = "[TERMINAL VIEW]"

    def show(self, action: str, response: dict):
        print(f"{self.name} - [{action}]: {response}")

    def error(self, msg: str):
        print(f"{self.name} - Error: {msg}")

    def select_action(self):
        return input(f"{self.name} - Which action to do you want to select (search|follow)?")

    def select_search_criteria(self):
        twitter_type = input(f"{self.name} - Which type of twitter do you want search (recent|all)?")
        twitter_value = input(f"{self.name} Which value do you want to search?")
        return twitter_type, twitter_value

    @admin
    def select_user_to_follow(self):
        return input(f"{self.name} - Which user do you want to follow?")
