import os
import requests

# Folder where files will be saved
output_folder = "gadm_states"
os.makedirs(output_folder, exist_ok=True)

# List of all ISO3 country codes (GADM-supported)
iso3_list = [
    "AFG","ALB","DZA","AND","AGO","ATG","ARG","ARM","AUS","AUT","AZE","BHS","BHR","BGD","BRB","BLR","BEL","BLZ","BEN",
    "BTN","BOL","BIH","BWA","BRA","BRN","BGR","BFA","BDI","CPV","KHM","CMR","CAN","CAF","TCD","CHL","CHN","COL","COM",
    "COG","CRI","CIV","HRV","CUB","CYP","CZE","COD","DNK","DJI","DMA","DOM","ECU","EGY","SLV","GNQ","ERI","EST","SWZ",
    "ETH","FJI","FIN","FRA","GAB","GMB","GEO","DEU","GHA","GRC","GRD","GTM","GIN","GNB","GUY","HTI","HND","HUN","ISL",
    "IND","IDN","IRN","IRQ","IRL","ISR","ITA","JAM","JPN","JOR","KAZ","KEN","KIR","PRK","KOR","KWT","KGZ","LAO","LVA",
    "LBN","LSO","LBR","LBY","LIE","LTU","LUX","MDG","MWI","MYS","MDV","MLI","MLT","MHL","MRT","MUS","MEX","FSM","MDA",
    "MCO","MNG","MNE","MAR","MOZ","MMR","NAM","NRU","NPL","NLD","NZL","NIC","NER","NGA","MKD","NOR","OMN","PAK","PLW",
    "PSE","PAN","PNG","PRY","PER","PHL","POL","PRT","QAT","ROU","RUS","RWA","KNA","LCA","VCT","WSM","SMR","STP","SAU",
    "SEN","SRB","SYC","SLE","SGP","SVK","SVN","SLB","SOM","ZAF","SSD","ESP","LKA","SDN","SUR","SWE","CHE","SYR","TWN",
    "TJK","TZA","THA","TLS","TGO","TON","TTO","TUN","TUR","TKM","TUV","UGA","UKR","ARE","GBR","USA","URY","UZB","VUT",
    "VAT","VEN","VNM","YEM","ZMB","ZWE"
]

base_url = "https://geodata.ucdavis.edu/gadm/gadm4.1/json/"

for code in iso3_list:
    filename = f"gadm41_{code}_1.json"
    url = base_url + filename
    save_path = os.path.join(output_folder, filename)

    print(f"Downloading {filename}...")

    try:
        r = requests.get(url, timeout=20)
        if r.status_code == 200:
            with open(save_path, "wb") as f:
                f.write(r.content)
            print(f"✔ Saved {filename}")
        else:
            print(f"✖ Failed (Status {r.status_code})")
    except Exception as e:
        print(f"✖ Error downloading {filename}: {e}")

print("\nDone! All files downloaded.")
