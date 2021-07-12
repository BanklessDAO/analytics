from json import dumps
from faker import Faker
import collections

database = []
filename = 'testing_bounty'
length = 5
fake = Faker()

# fake.word(ext_word_list=)
random_currencies = ['BANK', 'ETH', 'BTC']

random_guilds = ["Marketing Guild", "Treasury Guild",
                 "Developer's Guild", "Analytics Guild", "Writer's Guild"]

discord_handle = ["@bob#8888", "@alice#1234",
                  "@carol#5555", "@delta#2222", "@lambda#3333"]

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
        ('bounty', fake.sentence()),
        ('bountyDescription', fake.sentence()),
        ('bountyCriteria', fake.sentence()),
        ('bountyReward', collections.OrderedDict([
            ('currency', fake.word(ext_word_list=random_currencies)),
            ('amount', fake.random_int(0, 50000))
        ])),
        # list of dictionaries
        ('applicableGuilds', [collections.OrderedDict(
            [('guildName', fake.word(ext_word_list=random_guilds))]), collections.OrderedDict([('guildName', fake.word(ext_word_list=random_guilds))])]),
        ('bountyCreatedBy', collections.OrderedDict([
            ('isDaoMember', fake.pybool()),
            ('guildName', fake.word(ext_word_list=random_guilds)),
            ('discordHandle', fake.word(ext_word_list=discord_handle))
        ])),
        ('bountyCreatedAt', fake.date_between(start_date='today', end_date='+3m')),
        ('bountyDueAt', fake.date_between(start_date='today', end_date='+1y')),
        ('bountyImage', "https://pbs.twimg.com/profile_images/1389400052448247816/qsOU0pih_400x400.jpg"),
        ('bountyActivatedAt', fake.date_between(
            start_date='today', end_date='+6m')),
        ('bountyClaimedBy', collections.OrderedDict([
            ('guildName', fake.word(ext_word_list=random_guilds)),
            ('discordHandle', fake.word(ext_word_list=discord_handle)),
            ('publicAddress', "0x2d94aa3e47d9d5024503ca8" + fake.pystr())
        ])),
        ('bountyClaimedAt', fake.date_between(start_date='today', end_date='+4m')),
        ('bountySubmittedBy', fake.word(ext_word_list=random_guilds)),
        ('bountySubmittedAt', fake.date_between(
            start_date='today', end_date='+11m')),
        ('bountySubmissionLink', "www." + fake.safe_domain_name()),
        # list of dictionaries
        ('bountyStatus', [collections.OrderedDict([
            ('status', fake.word(ext_word_list=bounty_status)),
            ('bountyStatusTime', fake.date_between(
                start_date='today', end_date='+1y'))
        ])]),
        ('bountyHash', fake.md5(raw_output=False)),
        # list of words
        ('skillsRequired', [fake.word(ext_word_list=skills),
                            fake.word(ext_word_list=skills)])
    ]))

with open('%s.json' % filename, 'w') as output:
    # turns date_between into string, circumvent json serialization
    output.write(dumps(database, indent=4, sort_keys=False, default=str))
print("Done.")
