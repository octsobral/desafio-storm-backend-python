import pandas as pd

from src.utils.boolean_util import str_to_bool


class CurrentFactsService:

    def get_current_facts(self, facts, schema):

        validated_facts = self._validate_facts(facts)

        loaded_schema = self._load_schema(schema)

        df = pd.DataFrame(validated_facts, columns=['name', 'contact', 'information', 'not_retracted'])

        list_of_dataframes = []

        for key, value in loaded_schema.items():
            if key is 'many':
                intermediate = df.loc[df['contact'] == value]
                list_of_dataframes.append(intermediate)
            elif key is 'one':
                intermediate = df.loc[df['contact'] == value]
                intermediate = intermediate.groupby(['name', 'contact'], as_index=False).last()
                list_of_dataframes.append(intermediate)

        df = pd.concat(list_of_dataframes)

        current_facts = list(df.itertuples(index=False, name=None))

        return current_facts

    @staticmethod
    def _load_schema(schema):

        # validate schema not empty
        if len(schema) == 0:
            raise Exception("Schema not found")

        # validate schema format
        for setup in schema:
            if setup[1] is not 'cardinality' and len(setup) is not 3:
                raise Exception("Schema format not supported")

        loaded_schema = {}

        # loading schema to dict
        try:
            for setup in schema:
                if setup[2] is 'one':
                    loaded_schema['one'] = setup[0]
                elif setup[2] is 'many':
                    loaded_schema['many'] = setup[0]
        except:
            raise Exception("Schema format not supported")

        return loaded_schema

    @staticmethod
    def _validate_facts(facts):

        # validate facts not empty
        if len(facts) == 0:
            raise Exception("Facts not found")

        # validate facts format
        for fact in facts:
            if len(fact) is not 4:
                raise Exception("Facts format not supported")
            if type(fact[0]) is not str or type(fact[1]) is not str or type(fact[2]) is not str:
                raise Exception("Facts format not supported")

        phone_validated_facts = []

        # validate telephone number format
        for fact in facts:
            if fact[1] == 'telefone' and len(fact[2]) is 10:
                phone_validated_facts.append(fact)
            elif fact[1] == 'endereço':
                phone_validated_facts.append(fact)

        # remove retracted information
        validated_facts = [tup for tup in phone_validated_facts if str_to_bool(tup[-1]) is True]

        return validated_facts
