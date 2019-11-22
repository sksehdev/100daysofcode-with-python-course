import bs4
import requests
import collections


scd_diet = collections.namedtuple("scd_diet", "Name , Status")

resp = requests.get("http://www.breakingtheviciouscycle.info/legal/listing/A/")
resp.raise_for_status()

soup = bs4.BeautifulSoup(resp.text, 'html.parser')

scd_items = []

for item in soup.find(id="btvc_tbl_listing").find_all("tr"):
    scd_items.append(scd_diet(item.find_all("td")[0].get_text().rstrip(), item.find_all("td")[1].get_text()))


print(scd_items)