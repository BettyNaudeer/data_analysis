
# coding: utf-8

# Create a service that reads the raw gzip files from the input directory.
#
# The service should:
# - Load the files
# - Parse the data
# - Convert IP address to country, city
# - Parse user agent string and detect:
#     - browser family
#     - os family
#
# The service should print to standard out:
# - Top 5 Countries based on number of events
# - Top 5 Cities based on number of events
# - Top 5 Browsers based on number of unique users
# - Top 5 Operating systems based on number of unique users
#
#
#
# Note: The raw files will be provided by us and will be compressed using gzip and are tab separated (“tsv”)
# field header (date, time, user_id, url, IP, user_agent_string)
# url is hashed and has the structure of: “http://hashed_domain/hashed_path”
#
#
# You can use any module or your own algorithms to perform processing such as:
# to derive geographical data
# to parse the user agent string
# to connect to databases
#
#


import pandas as pd
import numpy as np
import geoip2.database
from geoip2.errors import AddressNotFoundError
from user_agents import parse

#Load the files

df = pd.read_table('input_data', header=None)
df.columns = ["date", "time", "user_id", "url", "IP", "user_agent_string"]

unduplicated_df = df.drop_duplicates()


# ### Top 5 Countries based on number of events
# ### Top 5 Cities based on number of events

reader = geoip2.database.Reader('./GeoLite2-City.mmdb')

ip_facts = []

for IP in unduplicated_df['IP']:
    try:
        first_ip = IP.split(', ', 1)[0]
        response = reader.city(first_ip)
        country = response.country.name
        city = response.city.name

    except AddressNotFoundError:
        pass

    except:
        pass

    ip_facts.append([country, city])

reader.close()

ip_facts_np = pd.DataFrame(ip_facts, columns= ['Country','City'])

ip_facts_np.dropna()

### Top 5 Countries based on number of events
print(ip_facts_np.Country.value_counts().nlargest(5))


### Top 5 Cities based on number of events
print(ip_facts_np.City.value_counts().nlargest(5))

unduplicated_df.head()


# ### Top 5 Browsers based on number of unique users
user_details = []

for x in unduplicated_df['user_agent_string']:
    first_try = x.split(' ')[-1]
    result = first_try.split('/')[0]
    user_details.append([result])

user_agent_facts_np = pd.DataFrame(user_details, columns = ['Browser'])

print(user_agent_facts_np.Browser.value_counts().nlargest(5))


# ### Top 5 Operating systems based on number of unique users
user_details = []

for x in unduplicated_df['user_agent_string']:
    user_details.append([x])

user_OS_pd = pd.DataFrame(user_details, columns = ['Details'])

user_agents = []

for x in user_OS_pd['Details']:
    ua_string = x
    user_agent = parse(ua_string)
    os = user_agent.os.family
    user_agents.append([os])

OS_pd = pd.DataFrame(user_agents, columns = ['OS'])

print(OS_pd.OS.value_counts().nlargest(5))
