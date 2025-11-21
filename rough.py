import json

# x =  '{ "name":"John", "age":30, "city":"New York"}'

# to_dict = json.loads(x)

x =  [{"name":"John", "age":30, "city":"New York"}]

# Write
# with open("store.json", "w") as store:
#     convert_to_json = json.dumps(x)
#     store.write(convert_to_json)

# Read
# with open("store.json") as f:
#   content = json.loads(f.read())
#   print(type(content))


# Types if method
class Main:
    # Instance method
    def unique(self):
        pass

    # Class method
    @classmethod
    def general(cls):
        pass


    # Static method
    @staticmethod
    def utility():
        passpython_data = {
    "name": "Alice",
    "age": 30,
    "isStudent": False,
    "courses": ["Math", "Science"]
}

# Convert Python dictionary to JSON string
json_string = json.dumps(python_data, indent=4)
print("JSON String:")
print(json_string)

# Convert JSON string back to Python dictionary
decoded_data = json.loads(json_string)
print("\nDecoded Python Dictionary:")
print(decoded_data)
print(f"Type of decoded_data: {type(decoded_data)}")
