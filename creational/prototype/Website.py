
class Website:
    def __init__(self, name: str, domain: str, description: str, author: str, **kwargs):
        self.name = name
        self.domain = domain
        self.description = description
        self.author = author
        for key, val in kwargs.items():
            setattr(self, key, val)

    def __str__(self):
        summary = [f"Website {self.name}\n"]
        info = vars(self).items()
        ordered_info = sorted(info)
        for attr, val in ordered_info:
            if attr == "name":
                continue
            summary.append(f"{attr}: {val}\n")
        return "".join(summary)

