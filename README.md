# What is it?

This is a code to show a Heatmap with accidents at state of Espírito Santo - Brazil based on data from Brazilian Federal Police.
Accidents are filtered to show only those with injuried people.


# How to run?

1- First, go to this link, download data you want:

https://www.prf.gov.br/portal/dados-abertos/acidentes

> Obs: Only files from 2017 are structured with latitude and longitude to be drawn in the map


2- Unpack files you've downloded and put them inside `files` folder at root of project


3- Then, you can adusts range date at `chart.py` at line 12

`for year in range(2017, 2020):`

> This one, for example, will consider data from 2017 to 2019


4- Run `python chart.py`


5- Onde file `index.html` on your browser



# What does it use?

- Python
- Pandas
- Folium
- Data from Brazilian Federal Police