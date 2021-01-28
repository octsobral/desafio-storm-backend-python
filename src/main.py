from src.resources.facts_resource import facts
from src.resources.schema_resource import schema
from src.services.current_facts_service import CurrentFactsService


class Main:

    def __init__(self):
        self.current_facts_service = CurrentFactsService()

    def run(self):

        current_facts_response = self.current_facts_service.get_current_facts(facts=facts, schema=schema)
        for current_facts in current_facts_response:
            print(current_facts)


if __name__ == "__main__":
    MAIN = Main()
    MAIN.run()
