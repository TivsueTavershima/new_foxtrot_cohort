
# -----------------------CONTROL STRUCTURES--------------------------

# CONTROL STRUCTURES ARE THE BUILDING BLOCK THAT CONTROL THE FLOW OF YOUR PROGRAME.
# condition.

# IF STATEMENT
destination_fee =1000
transport_fee = 900
train = "available"

# if transport_fee <= destination_fee:
#    C
# else:
#   print(f"{"==" + 24}\nGetting to destination successful.\n{"==" + 24}")

# if transport_fee <= destination_fee:
if transport_fee <= destination_fee:
  print(f"{"==" + 24}\nGetting to destination successful.\n{"==" + 24}")
else:
  print(f"{"==" + 24}\nGetting to destination successful.\n{"==" + 24}")


if transport_fee <= destination_fee and train == "available":
  print(f"{"==" + 24}\nGetting to destination A successful.\n{"==" + 24}")
elif transport_fee <= destination_fee and train != "available":
  print(f"{"== * 24"}\nTrain Not Available.\n{"==" + 24}")
else:
  print(f"{"==" + 24}\nGetting to destination A through train successful.\n{"==" + 24}")

if False:
 print("road a")
elif False:
 print("train b")
elif True:
 print("train c")
elif True:
 print("train d")
elif True:
 print("train d")


 