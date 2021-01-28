from src.services.current_facts_service import CurrentFactsService


def test_valid_current_facts():

    facts = [('gabriel', 'endereço', 'av rio branco, 109', True),
             ('joão', 'endereço', 'rua alice, 10', True),
             ('joão', 'endereço', 'rua bob, 88', True),
             ('joão', 'telefone', '234-5678', True),
             ('joão', 'telefone', '91234-5555', True),
             ('joão', 'telefone', '234-5678', False),
             ('gabriel', 'telefone', '98888-1111', True),
             ('gabriel', 'telefone', '56789-1010', True)]

    schema = [('endereço', 'cardinality', 'one'), ('telefone', 'cardinality', 'many')]

    expected = [('gabriel', 'endereço', 'av rio branco, 109', True),
                ('joão', 'endereço', 'rua bob, 88', True),
                ('joão', 'telefone', '91234-5555', True),
                ('gabriel', 'telefone', '98888-1111', True),
                ('gabriel', 'telefone', '56789-1010', True)]

    current_facts_service = CurrentFactsService()
    current_facts = current_facts_service.get_current_facts(facts, schema)

    assert current_facts == expected

def test_empty_facts():

    facts = []

    schema = [('endereço', 'cardinality', 'one'), ('telefone', 'cardinality', 'many')]

    expected = []

    current_facts_service = CurrentFactsService()
    current_facts = current_facts_service.get_current_facts(facts, schema)

    assert current_facts == expected

def test_empty_schema():
    pass

def test_invalid_facts():
    pass
def test_invalid_schema():
    pass
def test_facts_bool_to_string():
    pass