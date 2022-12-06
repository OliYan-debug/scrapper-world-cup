from nations import countries
from unidecode import unidecode
from flags import getCountryFlag
import wikipedia
import requests as r
wikipedia.set_lang("pt")

for nation in countries:
    country = wikipedia.page(nation)
    summary= country.summary
    name_formated = unidecode(country.original_title).lower().replace(" ", "_")
    flag = getCountryFlag(name_formated)
    # print(country.title)
    # print(flag)
    # print(summary)
    data = {"name":country.title, "name_formated": name_formated }
    r.post("http://localhost:2001/update", json=data, headers={"secret":"Brasil"})
    # print("\n=====================================\n")

