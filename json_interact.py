import json

def get_json_data():
    with open('taches.json', 'r') as openfile:
        return json.load(openfile)
 
def write_json_data(my_dictionary):
    json_object = json.dumps(my_dictionary, indent=4)
    with open("taches.json", "w") as outfile:
        outfile.write(json_object)