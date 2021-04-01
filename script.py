import csv
import os
import requests

try:
    import keys
except ImportError:
    print("Please generate an api key from https://positionstack.com/, and store it into a file named keys.py")
    print("add \"API_KEY=[your generated api key]\" into keys.py")
    exit(1)


def getLocationData(latitude, longitude):
    """
    Description: Gets the country and continent data
    Input: latitude, longitude
    Output: Country, Continent
    """
    url = f'http://api.positionstack.com/v1/reverse?access_key={keys.API_KEY}&query={latitude},{longitude}'
    headers = {'Accept': 'application/json'}
    try:
        # Reach out to api
        response = requests.get(url, headers)
        if response.status_code == 404 or 'data' not in response.json():
            return '', ''
        locationJSON = response.json()['data'][0]
        return locationJSON['country'], locationJSON['continent']
    except requests.exceptions.RequestException:
        return '', ''
    except TypeError:
        return '', ''


def createFile(input_file):
    """
    Description: Creates a new csv file with country and continent information
    Input: input_file - file to be read from
    """
    with open(input_file, 'r', encoding='utf-8') as csvinput:
        with open('new-meteorite-landings.csv', 'w', encoding='utf-8') as csvoutput:
            # initialize writer and reader
            writer = csv.writer(csvoutput, lineterminator='\n')
            reader = csv.reader(csvinput)

            # add country and continent header columns to new csv
            header_row = next(reader)
            header_row.append('Country')
            header_row.append('Continent')
            writer.writerow(header_row)

            # add country and continent data to each row
            for row in reader:
                country, continent = '', ''
                # row has a valid latitude or longitude and are both not zero
                if row[7] and row[8] and float(row[7]) != 0 and float(row[8]) != 0:
                    country, continent = getLocationData(
                        row[7], row[8])
                # add row to new csv
                row.append(country)
                row.append(continent)
                writer.writerow(row)


def main():
    createFile('meteorite-landings.csv')
    print('new-meteorite-landings.csv finished')


if __name__ == "__main__":
    main()
