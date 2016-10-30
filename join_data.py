import json
import os
import time

# pdata -> passatempos data


def join_pdata():
    """Joins all .json files resulting from the crawling into just one, called
    complete.json.

    Each higher-level name of this json is a string representing the name of a
    website and the corresponding value is a list of 'passatempos'.

    Example:



    It also outputs a file named last_update_date.json containing the date of
    the last update.

    Example:

    {"date": "21/10/2016"}
    """

    pdata_path = 'pdata/'
    joined_pdata_filename = 'complete.json'
    last_update_filename = 'last_update_date.json'

    joined_pdata = {}
    for pdata_filename in os.listdir(pdata_path):

        if pdata_filename in [joined_pdata_filename, last_update_filename]:
            continue

        with open(pdata_path + pdata_filename) as pdata_file:
            pdata_str = pdata_file.read()
            # Scrapy escapes some quotations as &QUOT; instead of \". I don't
            # know why, but it raises problems in the front-end. This hack
            # corrects the problem.
            pdata_str_corrected = pdata_str.replace('&QUOT;', '\\"')

            pdata_json = json.loads(pdata_str_corrected)

            # example.json -> I only want the "example" part
            site_name = pdata_filename.split('.')[0]

            joined_pdata[site_name] = pdata_json

    with open(pdata_path + joined_pdata_filename, 'w') as joined_pdata_file:
        json.dump(joined_pdata, joined_pdata_file)

    with open(pdata_path + last_update_filename, 'w') as last_update_file:
        last_update_dict = {}
        last_update_dict['date'] = time.strftime('%d/%m/%Y')
        json.dump(last_update_dict, last_update_file)


if __name__ == '__main__':
    join_pdata()
