import os
import rule_engine
import yaml


class RuleEngineManager:
    def __init__(self) -> None:
        self.rules = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.rules = None

    def execute(self, utf_rule, data) -> bool:
        re_rule = rule_engine.Rule(utf_rule["expression"])
        return re_rule.matches(data)

    def evaluate_expression(self, expression, data) -> bool:
        re_rule = rule_engine.Rule(expression)
        return re_rule.matches(data)

    def execute_message(self, utf_rule, data) -> str:
        if self.execute(utf_rule, data):
            return utf_rule["message"]["success"]

        return utf_rule["message"]["failure"]

    def load_rules(self, path=None):
        if path is None:
            rule_path = (
                os.path.dirname(
                    os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
                )
                + "/config/rules"
            )
            path = os.path.join(rule_path, "rules_default.yaml")

        try:
            # Read the rules
            with open(path, "r") as rule_file:
                file_contents = yaml.safe_load(rule_file)
                self.rules = file_contents["rules"]
        except Exception as e:
            raise RuntimeError(f"unable to load the Rules, path: {path}, error: {e}")

    def get_rule(self, rule_name):
        if self.rules:
            return self.rules[rule_name]
        else:
            raise RuntimeError("Rules are not loaded, please load the rules to get it")


if __name__ == "__main__":
    with RuleEngineManager() as ure:
        # works with Regualar expressions also and
        #  rule = rule_engine.Rule(
        #     'email =~ ".*@silabs.com$"'
        # https://zerosteiner.github.io/rule-engine/syntax.html

        root_dir = (
            os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
            + "/config/rules"
        )

        ure.load_rules(os.path.join(root_dir, "rules_default.yaml"))
        rule = ure.get_rule("cpu_usage")

        input_data = {"cpu_usage": 40}

        # Execute the rules
        response = ure.execute(rule, input_data)
        print(response)

        # Execute the rules with response Success/Failure
        response = ure.execute_message(rule, input_data)
        print(response)