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
        pass