# Infringement detection on Airbnb

We analyze the Airbnb listings of three European cities (Barcelona, Stockholm, Rome). We investigate to what extent the applicable laws are complied with and which patterns indicate that Airbnb is operated commercially and to a critical extent in a city. Based on our findings, we create a machine learning model for Barcelona that detects irregularities and classifies offers accordingly. The model could be used by the city council of Barcelona to check any given listing instantly for irregularities.

Data used in this project is taken from [Inside Airbnb](http://insideairbnb.com/get-the-data). Many thanks!

Some additional data is collected by a webscraper: For Barcelona we scraped the information weather the host is commercial of private. We did that for roughly 11300 listings.

### About Airbnb

Airbnb is an American company operating an online marketplace for short-term homestays and experiences. 

It started as a more evolved version of couch surfing.
The conceit of friendly locals renting out spare rooms has been supplanted by a more mercenary model.

The company acts as a broker and charges a commission from each booking. Both private and commercial landlords rent out accommodations under the mediation of the company, but without Airbnb assuming any legal obligations. 

From its founding in 2008 to March 2020, more than 900 million overnight stays were booked through Airbnb, according to the company.

### Criticism of Airbnb

Airbnb has come under criticism for a number of reasons, including the fact that:
- The mass subletting of housing at high prices for short stays is putting further pressure on the already tight housing market in some cities. Housing is becoming scarcer, rents are rising.
- Fewer taxes are being collected through tourism.
- Municipalities are losing control over the amount of tourism. 
- Residents are annoyed by the many strangers coming in and out of their homes. 

## Setup of virtual environment

```
pyenv local 3.9.8
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```
Technologies and tools used in this project:
- Python
- Unsupervised Learning (Clustering)
- Supervised Learning
- Webscraping
- Tableau
- Jupyter
- Github
- Kanban
