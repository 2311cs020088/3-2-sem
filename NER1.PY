data = {
    "location": ["hyd", "singatam"],
    "person": ["vinay", "hajji"],
    "organization": ["MDV", "Google"]
}
sentence = "Vinay works at Google in Hyd, while Hajji is employed at MDV and lives in Singatam."

ner_tags = []

for word in sentence.split():
    if word.lower() in data["location"]:
        ner_tags.append((word, "LOCATION"))
    elif word.lower() in data["person"]:
        ner_tags.append((word, "PERSON"))
    elif word in data["organization"]:
        ner_tags.append((word, "ORGANIZATION"))
    else:
        ner_tags.append((word, "O"))

print(ner_tags)
