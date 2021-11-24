# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 2 works
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

# test function by updating damages
def updated_damages(damages): 
  damages_float = []
  for amount in damages:
    if "M" in amount:
      damages_float.append(float(amount[:-1]) * conversion["M"])
    elif "B" in amount:
      damages_float.append(float(amount[:-1]) * conversion["B"])
    else:
      damages_float.append(amount)
  return damages_float
updated_damages = updated_damages(damages)
# print(updated_damages)

# 3 works -- a little confused by [names[i]]
# Create a Table
def hurricane_table(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths):
  hurricanes = {}
  for i in range(len(names)):
    hurricanes[names[i]] = {"Name": names[i], "Month": months[i],"Year": years[i], "Max Sustained Wind": max_sustained_winds[i], "Areas Affected": areas_affected[i], "Damage": updated_damages[i], "Deaths": deaths[i]}
  return hurricanes

# Create and view the hurricanes dictionary
hurricane_dictionary = hurricane_table(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)
# print(hurricane_dictionary)

# 4 works -- don't understand {value["Year"]:value}, why isn't it key[]:value?
# Organizing by Year
def hurricanes_by_year(hurricane_dictionary):
  hurricane_year = {}
  for key, value in hurricane_dictionary.items():
    hurricane_year.update({value["Year"]:value})
  return hurricane_year
hurricanes_by_year = hurricanes_by_year(hurricane_dictionary)
# print(hurricanes_by_year)

# 5 works -- area_count[area], why not just area_count?
# Counting Damaged Areas
def area_frequency(hurricane_dictionary):
  area_count = {}
  for value in hurricane_dictionary.values():
    for area in value["Areas Affected"]:
      if area in area_count:
        area_count[area] += 1
      else:
        area_count[area] = 1
  return area_count
  
# create dictionary of areas to store the number of hurricanes involved in
affected_areas = area_frequency(hurricane_dictionary)
# print(affected_areas)

# 6 works -- got solution online 
# Calculating Maximum Hurricane Count
def area_most_affected(affected_areas):
  max_value = max(affected_areas.values())
  max_keys = [key for key, value in affected_areas.items() if value == max(affected_areas.values())]
  return max_keys, max_value
# find most frequently affected area and the number of hurricanes involved in
most_affected = area_most_affected(affected_areas)
# print(most_affected)

# 7 works -- what if there are two with the same deadliness? 
# also, not what the instructions ask for: need to use hurricane_dictionary, but don't know how to get the items out I need.
# Calculating the Deadliest Hurricane
def death_frequency(names, deaths):
  names_deaths = list(zip(names, deaths))
  most_deaths = 0
  hurricane_name = "Cuba I"
  for name, death in names_deaths:
    if(death > most_deaths):
      most_deaths = death
      hurricane_name = name
  return hurricane_name, most_deaths

# find highest mortality hurricane and the number of deaths
deadliest_hurricane = death_frequency(names, deaths)
# print(deadliest_hurricane)

# 8 works -- don't quite understand the logic 
# Rating Hurricanes by Mortality
# categorize hurricanes in new dictionary with mortality severity as key
def categorize_by_mortality(hurricane_dictionary):
  mortality_scale = {0: 0,
                 1: 100,
                 2: 500,
                 3: 1000,
                 4: 10000}
  hurricanes_by_mortality = {0:[],1:[],2:[],3:[],4:[],5:[]}
  for cane in hurricane_dictionary:
    num_deaths = hurricane_dictionary[cane]['Deaths']
    if num_deaths == mortality_scale[0]:
      hurricanes_by_mortality[0].append(hurricane_dictionary[cane])
    elif num_deaths > mortality_scale[0] and num_deaths <= mortality_scale[1]:
      hurricanes_by_mortality[1].append(hurricane_dictionary[cane])
    elif num_deaths > mortality_scale[1] and num_deaths <= mortality_scale[2]:
      hurricanes_by_mortality[2].append(hurricane_dictionary[cane])
    elif num_deaths > mortality_scale[2] and num_deaths <= mortality_scale[3]:
      hurricanes_by_mortality[3].append(hurricane_dictionary[cane])
    elif num_deaths > mortality_scale[3] and num_deaths <= mortality_scale[4]:
      hurricanes_by_mortality[4].append(hurricane_dictionary[cane])
    elif num_deaths > mortality_scale[4]:
      hurricanes_by_mortality[5].append(hurricane_dictionary[cane])
  return hurricanes_by_mortality

# categorize hurricanes in new dictionary with mortality severity as key
hurricanes_by_mortality = categorize_by_mortality(hurricane_dictionary)
# print(hurricanes_by_mortality[5])

# 9 works -- don't understand the logic
# Calculating Hurricane Maximum Damage
def highest_damage(hurricane_dictionary):
# Find the highest damage inducing hurricane and its total cost.
  max_damage_cane = 'Cuba I'
  max_damage = 0
  for cane in hurricane_dictionary:
    if hurricane_dictionary[cane]['Damage'] == "Damages not recorded":
      pass
    elif hurricane_dictionary[cane]['Damage'] > max_damage:
      max_damage_cane = cane
      max_damage = hurricane_dictionary[cane]['Damage']
  return max_damage_cane, max_damage

# find highest damage inducing hurricane and its total cost
max_damage_cane, max_damage = highest_damage(hurricane_dictionary)
# print(max_damage_cane, max_damage)


# 10 works -- don't understand the logic
# Rating Hurricanes by Damage
  
# categorize hurricanes in new dictionary with damage severity as key
def categorize_by_damage(hurricane_dictionary):
#  Categorize hurricanes by damage and return a dictionary.
  damage_scale = {0: 0,
                 1: 100000000,
                 2: 1000000000,
                 3: 10000000000,
                 4: 50000000000}
  hurricanes_by_damage = {0:[],1:[],2:[],3:[],4:[],5:[]}
  for cane in hurricane_dictionary:
    total_damage = hurricane_dictionary[cane]['Damage']
    if total_damage == "Damages not recorded":
      hurricanes_by_damage[0].append(hurricane_dictionary[cane])
    elif total_damage == damage_scale[0]:
      hurricanes_by_damage[0].append(hurricane_dictionary[cane])
    elif total_damage > damage_scale[0] and total_damage <= damage_scale[1]:
      hurricanes_by_damage[1].append(hurricane_dictionary[cane])
    elif total_damage > damage_scale[1] and total_damage <= damage_scale[2]:
      hurricanes_by_damage[2].append(hurricane_dictionary[cane])
    elif total_damage > damage_scale[2] and total_damage <= damage_scale[3]:
      hurricanes_by_damage[3].append(hurricane_dictionary[cane])
    elif total_damage > damage_scale[3] and total_damage <= damage_scale[4]:
      hurricanes_by_damage[4].append(hurricane_dictionary[cane])
    elif total_damage > damage_scale[4]:
      hurricanes_by_damage[5].append(hurricane_dictionary[cane])
  return hurricanes_by_damage

# categorize hurricanes in new dictionary with damage severity as key
hurricanes_by_damage = categorize_by_damage(hurricane_dictionary)
# print(hurricanes_by_damage[5])
