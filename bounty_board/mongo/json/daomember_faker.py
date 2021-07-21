from json import dumps
from faker import Faker
import collections

database = []
filename = 'daomember'    # change this
length = 5
fake = Faker()


# fake.word(ext_word_list=)
random_guilds = ["Marketing Guild", "Treasury Guild",
                 "Developer's Guild", "Analytics Guild", "Writer's Guild"]

discord_handle = ["@bob#8888", "@alice#1234",
                  "@carol#5555", "@delta#2222", "@lambda#3333"]

for x in range(length):
    database.append(collections.OrderedDict([
        ('isDaoMember', fake.pybool()),
        ('guildName', fake.word(ext_word_list=random_guilds)),
        ('discordHandle', fake.word(ext_word_list=discord_handle))
    ]))

with open('%s.json' % filename, 'w') as output:
    # turns date_between into string, circumvent json serialization
    output.write(dumps(database, indent=4, sort_keys=False, default=str))
print("Done.")
