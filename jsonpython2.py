import json

print("Started Reading JSON file")
with open("developer.json", "r") as read_file:
    print("Converting JSON encoded data into Python dictionary")
    developer = json.load(read_file)

    print("Decoding JSON Data From File")
    print("Printing JSON values using key")
    print(developer["name"])
    print(developer["salary"])
    print(developer["skills"])
    print(developer["email"])
    print("Done reading json file")