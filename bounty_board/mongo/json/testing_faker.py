from json import dumps
from faker import Faker
import collections

database = []
filename = 'testing'
length = 50
fake = Faker()

for x in range(length):
    database.append(collections.OrderedDict([
        ('last_name', fake.last_name()),
        ('first_name', fake.first_name()),
        ('street_address', fake.street_address()),
        ('email', fake.email())
    ]))

with open('%s.json' % filename, 'w') as output:
    output.write(dumps(database, indent=4))
print("Done.")
