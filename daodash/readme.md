# DAODash pipeline readme

This directory contains various DAODash pipelines. This is a work-in-progress.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install foobar
```

## Environment Variable Setup

Pipelines will require API keys, secrets and other confidential information. To prevent this info from being uploaded to Github, please implement the following steps for _each_ pipeline.

1. Ensure `.gitignore` is setup at the root directory (i.e., analytics (root directory))
2. Add `.env` to `.gitignore`
3. Use one `.env` file per pipeline to store sensitive info like API keys, secret and other authorization info.

We can use the `dotenv` module in python.

```python
#.gitignore
# Environents
.env

# inside each .env file, example
API_KEY='fakeconsumerkey'
API_SECRET='fakeconsumersecret'

# inside a pipeline script
import os
from dotenv import load_dotenv   #for python-dotenv method
load_dotenv()                    #for python-dotenv method

api_key = os.environ.get('API_KEY')
api_secret = os.environ.get('API_SECRET')

```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

TBD

## Pipeline Progress

### Snapshot Proposal

- Update: Jan 29, 2022
- encountered a bug with pipeline: `snapshot_proposal_bankless_snapshot_header_1_weekly_dev.py`
- when querying our postgres db, the SQL query on line 32 "ORDER BY id", should be "ORDER BY start_date" for a more accurate sorting
- the `bankless_snapshot_header_1` table is not ordering all proposals by time, so a new table `bankless_snapshot_header_2` was created.
- created `temp_snapshot_proposal.py` as an an updated pipeline.

### Coordinape

- Update: Jan 30, 2022
- use new api endpoint: `https://api.coordinape.com/api/v2/users?circle_id` (previously: ../v2/token_gifts?circle_id)
- select specific columns: name, discord_username, address, circle_id
- concatenate df across several coordinape rounds
- need to automate pipeline

- Update: Feb 2, 2022
- create file: `coordinape_establish_api_connection.py` for documentating the process
