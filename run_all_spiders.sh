#!/bin/bash

# Runs all the spiders in ./pspiders/

pspiders_folder="pspiders/"
pdata_folder="pdata/"

cd $pspiders_folder
for filename in *.py
do
    # Spider python file has a name like "nameofsite_crawler.py". Here we divide
    # the file name by the underscore
    IFS='_' read -r -a site_name <<< "$filename"
    json_name=$site_name".json"
    json_path="../"$pdata_folder$json_name

    # If previous JSON file is not deleted, the new content will be appended
    rm $json_path

    scrapy runspider $filename -o $json_path
done

# Now that the data was extracted, join all the data into one file
cd ..
python join_data.py
