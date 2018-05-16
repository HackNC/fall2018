# fall2018

## Development Setup
Developed on Python 2.7.13. Not tested with Python 3, but should work fine (?).

0. (Recommended) Set up a python virtual environment
1. Install requirements 
    - Eg. `pip install -r requirements.txt`
2. Copy `config_example.py` to `config.py`
3. Change `EMAIL_SHEET_SCRIPT_URL` in `config.py`
    - If you don't want to write emails to a Google Sheet, then leave `EMAIL_SHEET_SCRIPT_URL` undefined (delete it) or as an empty string
        - The emails will still be written locally to `email_list`
    - Follow [this repo](https://github.com/jamiewilson/form-to-google-sheets) to setup your own Google Sheet 
    - HackNC organizers, if you would like to write to our email list, please ask in Slack 
4. `python server.py`

## Future notes
- We will probably use [Sass](https://sass-lang.com/) at some point