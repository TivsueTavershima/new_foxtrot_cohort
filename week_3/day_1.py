# -------- CONTROL STRUCTURES -----------

# Condition
# IF STATEMENT

destination_fee = 1000
transport_fee = 1200
train = "unavailable"

if transport_fee <= destination_fee and train == "available":
    print(f"{"==" * 24}\nGetting to destination A successful.\n{"==" * 24}")
elif transport_fee <= destination_fee and train != "available": 
    print(f"{"==" * 24}\nGetting to destination A through train successful.\n{"==" * 24}")
else:
    print(f"{"==" * 24}\nGetting to destination unsuccessful.\n{"==" * 24}")


if False:
    print("road a")
elif False:
    print("train a")
elif True:
    print("train b")
elif True:
    print("train c")
elif True:
    print("train d")
else:
    print(f"road b")