# michael-scott-bot

Want advice from Michael Scott? You got it!

### Set up a dev env
`virtualenv .venv`

`source .venv/bin/activate`

### Talk to Michael Scott

Make sure you set OPENAI_KEY environment variable (or enter it in the streamlit UI)

`OPENAI_KEY=$OPENAI_KEY streamlit run michael_scott_bot/core/michael_scott.py`

### Install requirements
`pip install -r requirements.txt`

`pip install -r requirements-dev.txt`


### Install pre commit hooks
`pre-commit install`


### Verify your code before pushing a commit
`pre-commit run --all-files`

If you are committing to a branch that is in DRAFT mode or work in progress and if you want to commit without having to worry about formatting, one could always use the "no-verify" flag

`git commit -m "Some comments" --no-verify`
