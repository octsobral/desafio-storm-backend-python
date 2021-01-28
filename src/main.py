from src.resources.facts_resource import facts
from src.resources.schema_resource import schema
from src.services.current_facts_service import CurrentFactsService


class Main:

    def __init__(self):
        self.current_facts_service = CurrentFactsService()

    def run(self):

        current_facts_response = self.current_facts_service.get_current_facts(facts=facts, schema=schema)
        print(current_facts_response)


if __name__ == "__main__":
    MAIN = Main()
    MAIN.run()
