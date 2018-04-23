# data_analysis
Create a service that reads the raw gzip files from the input directory.
The service should:
- Load the files
- Parse the data
- Convert IP address to country, city
- Parse user agent string and detect:
    - browser family
    - os family

The service should print to standard out:
- Top 5 Countries based on number of events
- Top 5 Cities based on number of events
- Top 5 Browsers based on number of unique users
- Top 5 Operating systems based on number of unique users

Note: The raw files will be provided by us and will be compressed using gzip and are tab separated (“tsv”) field header (date, time, user_id, url, IP, user_agent_string) url is hashed and has the structure of: “http://hashed_domain/hashed_path”

You can use any module or your own algorithms to perform processing such as:
- to derive geographical data
- to parse the user agent string
- to connect to databases

#### 1. Clone the service

#### 2. Create virtual env to manage dependencies easily
virtualenv venv

#### 3. Install using pip
pip install -r requirements.txt

#### 4. Run it!!!
python3 data_analysis.py

For the top 5 Countries and Cities I downloaded the GeoLite2_DB which linked IP addresses with physical global addresses.

The top 5 Browsers I tried to use split() which breakups a string. I do realise I could have used the user_agent and parsed it but I had fun playing with split.

For the Top 5 Operating systems I used the user_agent and parsed it.
