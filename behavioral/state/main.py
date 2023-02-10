from behavioral.state.ecommerce import ECommerce
from behavioral.state.test_runner import TestRunner

TC1 = ["open"]
TC2 = ["open", "dummy_action"]

if __name__ == "__main__":
    test_suite = [TC1, TC2]
    for tc in test_suite:
        print("====" * 30)
        tmp_runner = ECommerce()
        for event_name in tc:
            event_method = getattr(tmp_runner, event_name)
            event_method()
