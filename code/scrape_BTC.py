import requests
import zipfile
import os
# https://data.binance.vision/data/spot/daily/klines/BTCBUSD/1m/BTCBUSD-1m-2023-01-30.zip
url_template = "https://data.binance.vision/data/spot/daily/klines/BTCBUSD/1h/BTCBUSD-1m-{}-{:02d}-{:02d}.zip"

# Define the date range for which to download the zip files
start_year = 2021
start_month = 3
start_day = 1
end_year = 2022
end_month = 12
end_day = 31

# Loop through the date range to download the zip files
for year in range(start_year, end_year + 1):
    for month in range(start_month, end_month + 1):
        for day in range(start_day, end_day + 1):
            date = f"{year}-{month}-{day}"
            url = url_template.format(year, month, day)
            print(url)
            response = requests.get(url)
            if response.status_code == 200:
                # Save the zip file to the current directory
                with open(f"BTCBUSD-1m-{date}.zip", "wb") as f:
                    f.write(response.content)
                # Extract the contents of the zip file
                with zipfile.ZipFile(f"BTCBUSD-1m-{date}.zip", "r") as z:
                    z.extractall()
                # Delete the zip file after extraction
                os.remove(f"BTCBUSD-1m-{date}.zip")
                print(f"Successfully downloaded and extracted BTCBUSD-1m-{date}.zip")
            else:
                print(f"Unable to download BTCBUSD-1m-{date}.zip, status code: {response.status_code}")
