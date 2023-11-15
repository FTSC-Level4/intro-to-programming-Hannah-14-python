def describe_city(city, country='uae'):
    """Describe a city."""
    msg = city.title() + " is in " + country.title() + "."
    print(msg)

describe_city('abu dhabi')
describe_city('cebu', 'philippines')
describe_city('dubai')