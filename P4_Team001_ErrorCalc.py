#Run into output terminal
StrErrMeanY = .003889 #cm/inch (ahead)
StrErrMeanX = .01285 #cm/inch (right)

TurnErrMeanY = .01797 #cm/inch (ahead)
TurnErrMeanX = .02023 #cm/inch (right)

valid = False
TurnStr = ""
Turn = False

while (valid == False):
    TurnStr = (input("Is the robot going to turn? (y/n): "))
    if ((TurnStr == "y") or (TurnStr == "Y")):
        valid = True
        Turn = True
    elif ((TurnStr == "n") or (TurnStr == "N")):
        valid = True
        Turn = False


distance = 0
while not (distance > 0):
    distance = float(input("Please enter the distance (in): "))
    if (distance <= 0):
        print("Please enter a positive value.")

XError = 0
YError = 0

if (Turn):
    YError = distance * TurnErrMeanY
    XError = distance * TurnErrMeanX
else:
    YError = distance * StrErrMeanY
    XError = distance * StrErrMeanX

print("The robot should be (roughly) {0:.2f} cm to the right of the desired X point, and {1:.2f} cm ahead of the desired Y point.".format(XError,YError))