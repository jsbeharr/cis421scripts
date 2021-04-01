# CIS421 Project Scripts
## About
This script is used to add country and continent information to 
the meteorite landings dataset on kaggle. It uses existing latitude 
and longitude data with the position stack reverse geocoding api 
to obtain the country and continent for each meteorite in the data set. 
Once finished a new csv will be generated with the newly obtained data.
## Requirements
This script was tested on Python 3.9.1 on a Windows machine. It also uses 
the following python libraries:
- csv
- os
- requests

Make sure these python libaries are installed to run the script.

For convenience the meteorite landings from kaggle is already in 
the repository, therefore their is no need to download it. Certain
modification have been made to the data set for our purposes, so the original 
data set can be found in the [Links](#Links) section.

This project also makes use of the position stack reverse geocoding api. 
An api key can be obtained from the website (located in [Links](#Links)). The 
the free tier allows for 25,000 request but it should be noted that
the table has 45,717 rows in total. Information on pricing can be found 
on the position stack website. Once an api key is obtained a **keys.py** 
file must be created in the repo. In it add the following code:
```python
API_KEY = '[Your generated key]'
```
After this the script should be able to run.
## Running Code
Run the following command to run the code:

**WINDOWS**:
```powershell
py script.py
```
**MAC**:
```sh
python3 script.py
```
Their is a lot of data in the meteorite-landings.csv file, so this script 
may run for a long time. Either up to or more than hour. After the script 
has finished it will print out to the console that it has finished running 
and a file name 'new-meteorite-landings.csv' should be located in the repository.

Beware, this script has not been tested on Mac and may not work.

## Links
Here are a following links that may give more information regarding the meteorite 
landing data and the position stack api.
- [Meteorite Landing Dataset](https://www.kaggle.com/nasa/meteorite-landings)
- [Position Stack API](https://positionstack.com/)
