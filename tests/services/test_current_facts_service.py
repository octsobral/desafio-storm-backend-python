import pytest

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

def test_empty_schema():

    facts = [('gabriel', 'endereço', 'av rio branco, 109', True),
             ('joão', 'endereço', 'rua alice, 10', True),
             ('joão', 'endereço', 'rua bob, 88', True),
             ('joão', 'telefone', '234-5678', True),
             ('joão', 'telefone', '91234-5555', True),
             ('joão', 'telefone', '234-5678', False),
             ('gabriel', 'telefone', '98888-1111', True),
             ('gabriel', 'telefone', '56789-1010', True)]

    schema = []

    current_facts_service = CurrentFactsService()

    with pytest.raises(Exception) as e:
        current_facts_service.get_current_facts(facts, schema)

    assert e.value.args[0] == 'Schema not found'

def test_empty_facts():

    facts = []

    schema = [('endereço', 'cardinality', 'one'), ('telefone', 'cardinality', 'many')]

    current_facts_service = CurrentFactsService()

    with pytest.raises(Exception) as e:
        current_facts_service.get_current_facts(facts, schema)

    assert e.value.args[0] == 'Facts not found'

def test_invalid_facts_format():

    facts = [('gabriel', 'endereço', 'av rio branco, 109', True, 'tecnologo'),
             ('joão', 'endereço', 'rua alice, 10', True, 'advogado'),
             ('joão', 'endereço', 'rua bob, 88', True),
             ('joão', 'telefone', '234-5678', True),
             ('joão', 'telefone', '91234-5555', True),
             ('joão', 'telefone', '234-5678', False, 'tradutor'),
             ('gabriel', 'telefone', '98888-1111', True),
             ('gabriel', 'telefone', '56789-1010', True)]

    schema = [('endereço', 'cardinality', 'one'), ('telefone', 'cardinality', 'many')]

    current_facts_service = CurrentFactsService()

    with pytest.raises(Exception) as e:
        current_facts_service.get_current_facts(facts, schema)

    assert e.value.args[0] == 'Facts format not supported'

def test_invalid_schema_format():

    facts = [('gabriel', 'endereço', 'av rio branco, 109', True),
             ('joão', 'endereço', 'rua alice, 10', True),
             ('joão', 'endereço', 'rua bob, 88', True),
             ('joão', 'telefone', '234-5678', True),
             ('joão', 'telefone', '91234-5555', True),
             ('joão', 'telefone', '234-5678', False),
             ('gabriel', 'telefone', '98888-1111', True),
             ('gabriel', 'telefone', '56789-1010', True)]

    schema = [('endereço', 'one'), ('telefone', 'cardinality', 'two')]

    current_facts_service = CurrentFactsService()

    with pytest.raises(Exception) as e:
        current_facts_service.get_current_facts(facts, schema)

    assert e.value.args[0] == 'Schema format not supported'

def test_schema_without_address():

    facts = [('gabriel', 'endereço', 'av rio branco, 109', True),
             ('joão', 'endereço', 'rua alice, 10', True),
             ('joão', 'endereço', 'rua bob, 88', True),
             ('joão', 'telefone', '234-5678', True),
             ('joão', 'telefone', '91234-5555', True),
             ('joão', 'telefone', '234-5678', True),
             ('gabriel', 'telefone', '98888-1111', True),
             ('gabriel', 'telefone', '56789-1010', True)]

    schema = [('telefone', 'cardinality', 'many')]

    expected = [('joão', 'telefone', '91234-5555', True),
                ('gabriel', 'telefone', '98888-1111', True),
                ('gabriel', 'telefone', '56789-1010', True)]

    current_facts_service = CurrentFactsService()
    current_facts = current_facts_service.get_current_facts(facts, schema)

    assert current_facts == expected

def test_schema_without_phone_number():

    facts = [('gabriel', 'endereço', 'av rio branco, 109', True),
             ('joão', 'endereço', 'rua alice, 10', True),
             ('joão', 'endereço', 'rua bob, 88', True),
             ('joão', 'telefone', '234-5678', True),
             ('joão', 'telefone', '91234-5555', True),
             ('joão', 'telefone', '234-5678', False),
             ('gabriel', 'telefone', '98888-1111', True),
             ('gabriel', 'telefone', '56789-1010', True)]

    schema = [('endereço', 'cardinality', 'one')]

    expected = [('gabriel', 'endereço', 'av rio branco, 109', True),
                ('joão', 'endereço', 'rua bob, 88', True)]

    current_facts_service = CurrentFactsService()
    current_facts = current_facts_service.get_current_facts(facts, schema)

    assert current_facts == expected

def test_facts_with_wrong_information():

    facts = [('gabriel', 23567, 'av rio branco, 109', True),
             ('joão', 'endereço', 'rua alice, 10', True),
             ('joão', 'endereço', 'rua bob, 88', True),
             ('joão', 'telefone', '234-5678', True),
             ('joão', False, '91234-5555', True),
             ('joão', 'telefone', '234-5678', False),
             ('gabriel', 'telefone', '98888-1111', True),
             ('gabriel', 'telefone', '56789-1010', True)]

    schema = [('endereço', 'cardinality', 'one'), ('telefone', 'cardinality', 'many')]

    current_facts_service = CurrentFactsService()

    with pytest.raises(Exception) as e:
        current_facts_service.get_current_facts(facts, schema)

    assert e.value.args[0] == 'Facts format not supported'