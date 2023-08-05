class InvalidData(Exception):
    pass

class SchemaField:

    def __init__(self, name, field_type, mode = 'Nullable'):
        self.field_type = field_type
        self.name = name
        self.mode = mode

class RowIterator:

    def __init__(self, data):
        self.counter = 0
        self.total_rows = len(data)
        self.data = data
        self.schema = [SchemaField(name = 'todo', field_type='INTEGER')]

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter< self.total_rows:
            self.counter += 1
            return Row(row = self.data[self.counter -1])
        else:
            raise StopIteration

    def result(self):
        return self

class Row():

    def __init__(self, row):
        self.info = {}
        l = []
        for i in row:
            self.info[i[0]] = i[1]
            l.append(i[1])
        self._values = tuple(l)
        self.row = row

    def get(self, *args, **kwargs):
        if args:
            return self.info.get(args[0])
        return self.info.get(kwargs['key'])

    def items(self, *args, **kwargs):
        for i in self.row:
            yield i

    def values(self, *args, **kwargs):
        return self._values

    def keys(self, *args, **kwargs):
        return self.info.keys()

def get_sql_key(query):
    for line in query.split('\n'):
        if 'py-bigquery-mock-register:' in line:
            fields = line.split(':')
            if len(fields) != 2:
                raise InvalidData('hint  should be in format "py-bigquery-mock-register: key"')
            return fields[1].strip()

class Client:

    def _test_valid_data(self, data):
        if not isinstance(data, list):
            raise InvalidData(f'{data} is not a list')
        errors = []
        for n, i in enumerate(data):
            if not isinstance(i, list):
                errors.append((n, i, 'not a list'))
        if len(errors) != 0:
            raise InvalidData(errors)

    def __init__(self, data = []):
        self._test_valid_data(data)
        self.data = data
        self.registered_data = {}

    def register_data(self, key, data):
        self._test_valid_data(data)
        self.registered_data[key] = data

    def query(self, query, *args, **kwargs):
        key = get_sql_key(query)
        if key:
            data = self.registered_data.get(key)
            if not data:
                raise InvalidData(f'{key} not found in registered_data')
        else:
            data = self.data
        return RowIterator(data = data)

    def create_table(self, table):
        return table

    def delete_table(self, table_id, not_found_ok=False):
        pass

class Table:

    def _get_table_info(self, table_id):
        if not isinstance(table_id, str):
            raise InvalidData('table id must be str')
        fields = table_id.split('.')
        if len(fields) != 3:
            raise InvalidData('table id must be in format "project_id.dataset_id.table_id"')
        self.project = fields[0]
        self.dataset_id= fields[1]
        self.table_id = fields[2]


    def __init__(self, table_id, schema):
        self._get_table_info(table_id)
        self.schema = schema
