import sys
if len(sys.argv) > 1:
    scores = [float(x) for x in sys.argv[1:]]
    print("User provided scores:")
else:
    scores = [50, 60, 70, 80, 90]
    print("No input given - using default scores:")

total = sum(scores)
average = total / len(scores)
maximum = max(scores)
minimum = min(scores)

print("Scores:", scores)
print("Sum of scores:",total)
print("Average score:",average)
print("Maximum score:",maximum)
print("Minimum score:",minimum)
