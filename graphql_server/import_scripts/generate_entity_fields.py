# simple helper script to convert csv column headers to entity class fields

# todo: - use csv parser to read in the column headers
#       - get path to csv from args

daily_tweet_activity_columns = [
    'Date',
    'Tweets published',
    'impressions',
    'engagements',
    'engagement rate',
    'retweets',
    'replies',
    'likes',
    'user profile clicks',
    'url clicks',
    'hashtag clicks',
    'detail expands',
    'permalink clicks',
    'app opens',
    'app installs',
    'follows',
    'email tweet',
    'dial phone',
    'media views',
    'media engagements',
    'promoted impressions',
    'promoted engagements',
    'promoted engagement rate',
    'promoted retweets',
    'promoted replies',
    'promoted likes',
    'promoted user profile clicks',
    'promoted url clicks',
    'promoted hashtag clicks',
    'promoted detail expands',
    'promoted permalink clicks',
    'promoted app opens',
    'promoted app installs',
    'promoted follows',
    'promoted email tweet',
    'promoted dial phone',
    'promoted media views',
    'promoted media engagements'
]


def field_name_format(header):
    return header.lower().replace(' ', '_')


def generate_entity_fields(column_headers):
    for header in column_headers:
        print('@Field()')
        print('@Column()')
        print(f'{field_name_format(header)}: any')
        print()


# simply copy console output and merge it into entity class
# add typing information for each field manually
generate_entity_fields(daily_tweet_activity_columns)
