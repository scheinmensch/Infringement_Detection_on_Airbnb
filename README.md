# Infringement detection on Airbnb

We analyze the Airbnb listings of three European metropolitan areas (Stockholm, Rome, Barcelona) and examine the extent to which applicable laws are complied with. Based on our findings, we create a model that classifies listings into different categories.

Data used in this project is taken from [Inside Airbnb] (http://insideairbnb.com/get-the-data/) Many thanks!
Some additional data is collected by a webscraper.

## Setup of virtual environment

```
pyenv local 3.9.8
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```
