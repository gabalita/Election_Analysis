counties_dict = {}
counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438

#for county, voters in counties_dict.items():
 #   print (county,voters)
    
#voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]

#for i in range(len(voting_data)):
#    print (i)
#    print (voting_data[i]['county'])


for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters.")
