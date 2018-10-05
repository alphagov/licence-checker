# licence-checker
Check which repos in your Github organisation don't have LICENCE files

This requires you to have an API access token for Github. You can find more information about setting one up at https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/

## Setup
    virtualenv venv
    source ./venv/bin/activate
    pip install -r requirements.txt

## Run
Run using:

    python run.py your-github-access-key organisation-name

For example:

    python run.py abcdeiouhwefoiuhwefoihfjfi alphagov

The script may take a couple of minutes to run.

## Narrow the results to your team

Assuming all the repos for your team begin with the same prefix, for example `pay-`, then you can use grep to narrow your results.

For example:

	python run.py abcdeiouhwefoiuhwefoihfjfi alphagov | grep "pay-"

## License
Distributed under [the MIT License](LICENCE)
