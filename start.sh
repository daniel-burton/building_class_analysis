#! /bin/bash
echo "Downloading PLUTO..."
wget -P ./original_data/pluto https://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/nyc_pluto_18v1.zip
echo "Unzipping PLUTO..."
unzip ./original_data/pluto/nyc_pluto_18v1.zip -d ./original_data/pluto
echo "Putting PLUTO away..."
mv ./original_data/pluto/PLUTO_for_WEB/* ./original_data/pluto
rm -rf ./original_data/pluto/PLUTO_for_WEB
rm ./original_data/pluto/nyc_pluto_18v1.zip
