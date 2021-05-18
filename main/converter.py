from datetime import datetime


class DateConverter:
    regex = '[0-9]{4}-[0-9]{1,2}-[0-9]{1,2}'

    def to_python(self, value):
        return datetime.strptime(value, '%Y-%d-%m')

    def to_url(self, value):
        return value.strftime('%Y-%d-%m')