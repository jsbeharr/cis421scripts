import csv
import os
import requests
import json

try:
    import keys
except ImportError:
    print("Please generate a api key, and store it into a file named keys.py")
    exit(1)


def getLocationData(latitude, longitude):
    """
    Description: Gets the country and continent data
    Input: latitude, longitude
    """
    api_url = f'http://api.positionstack.com/v1/reverse?access_key={keys.API_KEY}&query={latitude},{longitude}'
    try:
        response = requests.get(api_url)
        if not response.json()['data']:
            return '', ''
        country = response.json()['data'][0]['country']
        continent = response.json()['data'][0]['continent']
        return country, continent
    except requests.exceptions.RequestException:
        return '', ''


def createFile(input_file):
    """
    Description: Creates a new csv file with country and continent information
    Input:
            input_file - file to be read from
    """
    with open(input_file, 'r', encoding='utf-8') as csvinput:
        with open('new-meteorite-landings.csv', 'w', encoding='utf-8') as csvoutput:
            writer = csv.writer(csvoutput, lineterminator='\n')
            reader = csv.reader(csvinput)
            # add country and continent columns
            header_row = next(reader)
            header_row.append('Country')
            header_row.append('Continent')
            writer.writerow(header_row)

            for row in reader:
                if row[7] and row[8]:
                    country, continent = getLocationData(
                        row[7], row[8])
                    row.append(country)
                    row.append(continent)
                    writer.writerow(row)

            # writer.writerows(all)


def main():
    createFile('meteorite-landings.csv')


if __name__ == "__main__":
    main()
