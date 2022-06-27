from structural.handson.model.local_model import TwitterLocalModel
from structural.handson.view.terminal_view import TwitterTerminalView


class TwitterController:
    def __init__(self):
        self.model = TwitterLocalModel()
        self.view = TwitterTerminalView()

    def run(self):
        action = self._select_action()
        if action == "search":
            self._search()
        else:
            self._follow()

    def _select_action(self):
        action = None
        while not action:
            action = self.view.select_action()
            if action not in ("search", "follow"):
                self.view.error(f"Invalid action: {action}")
                action = None
        return action

    def _search(self):
        s_type, s_value = None, None
        while not s_type:
            s_type, s_value = self.view.select_search_criteria()
            if s_type not in ("recent", "all"):
                self.view.error(f"Invalid search type: {s_type}")
                s_type = None
            if not s_value:
                self.view.error(f"Search value cannot be None: {s_value}")
        if s_type == "recent":
            self.model.search_recent(s_value)
        else:
            self.model.search_all(s_value)

    def _follow(self):
        try:
            user = self.view.select_user_to_follow()
            self.model.follow(user)
        except AttributeError as error:
            self.view.error(error)
