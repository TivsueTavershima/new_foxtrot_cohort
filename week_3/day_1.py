# -------- CONTROL STRUCTURES -----------

# Condition
# IF STATEMENT

# destination_fee = 1000
# transport_fee = 1200
# train = "unavailable"

# if transport_fee <= destination_fee and train == "available":
#     print(f"{"==" * 24}\nGetting to destination A successful.\n{"==" * 24}")
# elif transport_fee <= destination_fee and train != "available": 
#     print(f"{"==" * 24}\nGetting to destination A through train successful.\n{"==" * 24}")
# else:
#     print(f"{"==" * 24}\nGetting to destination unsuccessful.\n{"==" * 24}")


# if False:
#     print("road a")
# elif False:
#     print("train a")
# elif True:
#     print("train b")
# elif True:
#     print("train c")
# elif True:
#     print("train d")
# else:
#     print(f"road b")






python_data = {
    "name": "Alice",
    "age": 30,
    "isStudent": False,
    "courses": ["Math", "Science"]
}

import json

# Convert Python dictionary to JSON string
json_string = json.dumps(python_data, indent=0)
print("JSON String:")
print(json_string)

# Convert JSON string back to Python dictionary
decoded_data = json.loads(json_string)
print("\nDecoded Python Dictionary:")
print(decoded_data)
print(f"Type of decoded_data: {type(decoded_data)}")  