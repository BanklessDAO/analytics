from json import dumps
from faker import Faker
import collections


database = []
filename = 'bountycard_faker2'
length = 20
fake = Faker()

# fake.word(ext_word_list=)
random_currencies = ['BANK', 'ETH', 'BTC']

random_guilds = ["Marketing Guild", "Treasury Guild",
                 "Developer's Guild", "Analytics Guild", "Writer's Guild", "Legal Guild", "Operations Guild"]

discord_handle = ["@bob#8888", "@alice#1234",
                  "@carol#5555", "@delta#2222", "@lambda#3333", "@alpha#1111", "@echo2222"]

bounty_status = ['Open', 'Draft', 'In-Progress',
                 'In-Review', 'Completed', 'Deleted']

skills = ["writing",
          "design",
          "software development",
          "strategic planning",
          "data analysis",
          "grant writing",
          "proposal development",
          "team building",
          "marketing"]

for x in range(length):
    database.append(collections.OrderedDict([
        ('season', fake.random_int(0, 10)),
        ('Title', fake.sentence()),
        ('Description', fake.sentence()),
        ('Criteria', fake.sentence()),
        ('Reward', collections.OrderedDict([
            ('currency', fake.word(ext_word_list=random_currencies)),
            ('amount', fake.random_int(0, 50000))
        ])),
        # list of dictionaries
        ('applicableGuilds', [collections.OrderedDict(
            [('guildName', fake.word(ext_word_list=random_guilds))]), collections.OrderedDict([('guildName', fake.word(ext_word_list=random_guilds))])]),
        ('CreatedBy', fake.bothify(
            text='ObjectId(##?####?###?##???###?#?#)', letters='aBcDe')),
        ('CreatedAt', fake.iso8601()),
        ('DueAt', fake.iso8601()),
        ('Image', "https://pbs.twimg.com/profile_images/1389400052448247816/qsOU0pih_400x400.jpg"),
        ('ActivatedAt', fake.iso8601()),
        ('ClaimedBy', collections.OrderedDict([
            ('user', fake.bothify(
                text='ObjectId(##?####?###?##???###?#?#)', letters='aBcDe')),
            ('user', fake.bothify(
                text='ObjectId(##?####?###?##???###?#?#)', letters='aBcDe'))
        ])),
        ('ClaimedAt', fake.iso8601()),
        ('SubmittedBy', fake.word(ext_word_list=random_guilds)),
        ('SubmittedAt', fake.iso8601()),
        ('SubmissionLink', "www." + fake.safe_domain_name()),
        # list of dictionaries
        ('Status', [collections.OrderedDict([
            ('status', fake.word(ext_word_list=bounty_status)),
            ('StatusTime', fake.iso8601())
        ])]),
        ('Hash', fake.md5(raw_output=False)),
        # list of words
        ('skillsRequired', [fake.word(ext_word_list=skills),
                            fake.word(ext_word_list=skills)])
    ]))

with open('%s.json' % filename, 'w') as output:
    # turns date_between into string, circumvent json serialization
    output.write(dumps(database, indent=4, sort_keys=False, default=str))
print("Done.")
