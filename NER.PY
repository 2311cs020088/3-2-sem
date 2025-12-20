data = {
    "location": ["hyderabad", "singatam","giddalur","kakinada","Delhi","goa","kerala"],
    "person": ["vinay", "hajji","Santhosh","naveen","surjan","sai","Mohan(panda)"],
    "organization": ["MDV", "Google","IBM","Amazon","TCS","flipkart","microsoft","MRU","CMR"]
}
for label, entities in data.items():
    for entity in entities:
        print(entity, label.upper())
for label, entities in data.items():
    for entity in entities:
        print(entity, label.lower()) 