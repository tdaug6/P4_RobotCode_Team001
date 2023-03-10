import os

#Clearing the terminal of clutter
clear = lambda: os.system('cls')
clear()

#Run into output terminal
StrErrMeanY = .003889 #cm/inch (ahead)
StrErrMeanX = .01285 #cm/inch (right)

TurnErrMeanY = .01797 #cm/inch (ahead)
TurnErrMeanX = .02023 #cm/inch (right)

xdistance = 0 #in
ydistance = 0 #in

valid = False

location = input("Please enter the box location (Ex: A2_11): ")
size = len(location)

# Note: distance from center of robot rotation to edge is 4.75 inches
# meaning it should move 1 inch closer to the box to determine
# which box it's going for. For shelf sides facing the start point,
# add 1 inch; for shelf sides facing away, remove 1 inch.

#Shelf A
if ((location[0] == 'A') or (location[0] == 'a')):
    if (location [1] == '1'):
        if (size == 4):
            if (location[3] == '1'):
                ydistance = ydistance + 12 + 1
                xdistance = xdistance + 6 + 3
                valid = True

            elif (location[3] == '2'):
                ydistance = ydistance + 12 + 1
                xdistance = xdistance + 6 + 9
                valid = True

            elif (location[3] == '3'):
                ydistance = ydistance + 12 + 1
                xdistance = xdistance + 6 + 15
                valid = True

            elif (location[3] == '4'):
                ydistance = ydistance + 12 + 1
                xdistance = xdistance + 6 + 21
                valid = True

            elif (location[3] == '5'):
                ydistance = ydistance + 12 + 1
                xdistance = xdistance + 6 + 27
                valid = True

            elif (location[3] == '6'):
                ydistance = ydistance + 12 + 1
                xdistance = xdistance + 6 + 33
                valid = True

            elif (location[3] == '7'):
                ydistance = ydistance + 36 - 1
                xdistance = xdistance + 6 + 3
                valid = True

            elif (location[3] == '8'):
                ydistance = ydistance + 36 - 1
                xdistance = xdistance + 6 + 9
                valid = True

            elif (location[3] == '9'):
                ydistance = ydistance + 36 - 1
                xdistance = xdistance + 6 + 15
                valid = True

        elif (size == 5):
            if (location[4] == '0'):
                ydistance = ydistance + 36 - 1
                xdistance = xdistance + 6 + 21
                valid = True

            elif (location[4] == '1'):
                ydistance = ydistance + 36 - 1
                xdistance = xdistance + 6 + 27
                valid = True

            elif (location[4] == '2'):
                ydistance = ydistance + 36 - 1
                xdistance = xdistance + 6 + 33
                valid = True
    
    if (location [1] == '2'):
        if (size == 4):
            if (location[3] == '1'):
                ydistance = ydistance + 36 + 1
                xdistance = xdistance + 6 + 3
                valid = True

            elif (location[3] == '2'):
                ydistance = ydistance + 36 + 1
                xdistance = xdistance + 6 + 9
                valid = True

            elif (location[3] == '3'):
                ydistance = ydistance + 36 + 1
                xdistance = xdistance + 6 + 15
                valid = True

            elif (location[3] == '4'):
                ydistance = ydistance + 36 + 1
                xdistance = xdistance + 6 + 21
                valid = True

            elif (location[3] == '5'):
                ydistance = ydistance + 36 + 1
                xdistance = xdistance + 6 + 27
                valid = True

            elif (location[3] == '6'):
                ydistance = ydistance + 36 + 1
                xdistance = xdistance + 6 + 33
                valid = True

            elif (location[3] == '7'):
                ydistance = ydistance + 60 - 1
                xdistance = xdistance + 6 + 3
                valid = True

            elif (location[3] == '8'):
                ydistance = ydistance + 60 - 1
                xdistance = xdistance + 6 + 9
                valid = True

            elif (location[3] == '9'):
                ydistance = ydistance + 60 - 1
                xdistance = xdistance + 6 + 15
                valid = True

        elif (size == 5):
            if (location[4] == '0'):
                ydistance = ydistance + 60 - 1
                xdistance = xdistance + 6 + 21
                valid = True

            elif (location[4] == '1'):
                ydistance = ydistance + 60 - 1
                xdistance = xdistance + 6 + 27
                valid = True

            elif (location[4] == '2'):
                ydistance = ydistance + 60 - 1
                xdistance = xdistance + 6 + 33
                valid = True


#Shelf B ###########################################
elif ((location[0] == 'B') or (location[0] == 'b')):
    if (location [1] == '1'):
        if (size == 4):
            if (location[3] == '1'):
                ydistance = ydistance + 12 + 1
                xdistance = xdistance + 66 + 3
                valid = True

            elif (location[3] == '2'):
                ydistance = ydistance + 12 + 1
                xdistance = xdistance + 66 + 9
                valid = True

            elif (location[3] == '3'):
                ydistance = ydistance + 12 + 1
                xdistance = xdistance + 66 + 15
                valid = True

            elif (location[3] == '4'):
                ydistance = ydistance + 12 + 1
                xdistance = xdistance + 66 + 21
                valid = True

            elif (location[3] == '5'):
                ydistance = ydistance + 12 + 1
                xdistance = xdistance + 66 + 27
                valid = True

            elif (location[3] == '6'):
                ydistance = ydistance + 12 + 1
                xdistance = xdistance + 66 + 33
                valid = True

            elif (location[3] == '7'):
                ydistance = ydistance + 36 - 1
                xdistance = xdistance + 66 + 3
                valid = True

            elif (location[3] == '8'):
                ydistance = ydistance + 36 - 1
                xdistance = xdistance + 66 + 9
                valid = True

            elif (location[3] == '9'):
                ydistance = ydistance + 36 - 1
                xdistance = xdistance + 66 + 15
                valid = True

        elif (size == 5):
            if (location[4] == '0'):
                ydistance = ydistance + 36 - 1
                xdistance = xdistance + 66 + 21
                valid = True

            elif (location[4] == '1'):
                ydistance = ydistance + 36 - 1
                xdistance = xdistance + 66 + 27
                valid = True

            elif (location[4] == '2'):
                ydistance = ydistance + 36 - 1
                xdistance = xdistance + 66 + 33
                valid = True
                
    if (location [1] == '2'):
        if (size == 4):
            if (location[3] == '1'):
                ydistance = ydistance + 36 + 1
                xdistance = xdistance + 66 + 3
                valid = True

            elif (location[3] == '2'):
                ydistance = ydistance + 36 + 1
                xdistance = xdistance + 66 + 9
                valid = True

            elif (location[3] == '3'):
                ydistance = ydistance + 36 + 1
                xdistance = xdistance + 66 + 15
                valid = True

            elif (location[3] == '4'):
                ydistance = ydistance + 36 + 1
                xdistance = xdistance + 66 + 21
                valid = True

            elif (location[3] == '5'):
                ydistance = ydistance + 36 + 1
                xdistance = xdistance + 66 + 27
                valid = True

            elif (location[3] == '6'):
                ydistance = ydistance + 36 + 1
                xdistance = xdistance + 66 + 33
                valid = True

            elif (location[3] == '7'):
                ydistance = ydistance + 60 - 1
                xdistance = xdistance + 66 + 3
                valid = True

            elif (location[3] == '8'):
                ydistance = ydistance + 60 - 1
                xdistance = xdistance + 66 + 9
                valid = True

            elif (location[3] == '9'):
                ydistance = ydistance + 60 - 1
                xdistance = xdistance + 66 + 15
                valid = True

        elif (size == 5):
            if (location[4] == '0'):
                ydistance = ydistance + 60 - 1
                xdistance = xdistance + 66 + 21
                valid = True

            elif (location[4] == '1'):
                ydistance = ydistance + 60 - 1
                xdistance = xdistance + 66 + 27
                valid = True

            elif (location[4] == '2'):
                ydistance = ydistance + 60 - 1
                xdistance = xdistance + 66 + 33
                valid = True

#Shelf C #########################################
if ((location[0] == 'C') or (location[0] == 'c')):
    if (location [1] == '1'):
        if (size == 4):
            if (location[3] == '1'):
                ydistance = ydistance + 60 + 1
                xdistance = xdistance + 6 + 3
                valid = True

            elif (location[3] == '2'):
                ydistance = ydistance + 60 + 1
                xdistance = xdistance + 6 + 9
                valid = True

            elif (location[3] == '3'):
                ydistance = ydistance + 60 + 1
                xdistance = xdistance + 6 + 15
                valid = True

            elif (location[3] == '4'):
                ydistance = ydistance + 60 + 1
                xdistance = xdistance + 6 + 21
                valid = True

            elif (location[3] == '5'):
                ydistance = ydistance + 60 + 1
                xdistance = xdistance + 6 + 27
                valid = True

            elif (location[3] == '6'):
                ydistance = ydistance + 60 + 1
                xdistance = xdistance + 6 + 33
                valid = True

            elif (location[3] == '7'):
                ydistance = ydistance + 84 - 1
                xdistance = xdistance + 6 + 3
                valid = True

            elif (location[3] == '8'):
                ydistance = ydistance + 84 - 1
                xdistance = xdistance + 6 + 9
                valid = True

            elif (location[3] == '9'):
                ydistance = ydistance + 84 - 1
                xdistance = xdistance + 6 + 15
                valid = True

        elif (size == 5):
            if (location[4] == '0'):
                ydistance = ydistance + 84 - 1
                xdistance = xdistance + 6 + 21
                valid = True

            elif (location[4] == '1'):
                ydistance = ydistance + 84 - 1
                xdistance = xdistance + 6 + 27
                valid = True

            elif (location[4] == '2'):
                ydistance = ydistance + 84 - 1
                xdistance = xdistance + 6 + 33
                valid = True

    if (location [1] == '2'):
        if (size == 4):
            if (location[3] == '1'):
                ydistance = ydistance + 84 + 1
                xdistance = xdistance + 6 + 3
                valid = True

            elif (location[3] == '2'):
                ydistance = ydistance + 84 + 1
                xdistance = xdistance + 6 + 9
                valid = True

            elif (location[3] == '3'):
                ydistance = ydistance + 84 + 1
                xdistance = xdistance + 6 + 15
                valid = True

            elif (location[3] == '4'):
                ydistance = ydistance + 84 + 1
                xdistance = xdistance + 6 + 21
                valid = True

            elif (location[3] == '5'):
                ydistance = ydistance + 84 + 1
                xdistance = xdistance + 6 + 27
                valid = True

            elif (location[3] == '6'):
                ydistance = ydistance + 84 + 1
                xdistance = xdistance + 6 + 33
                valid = True

            elif (location[3] == '7'):
                ydistance = ydistance + 108 - 1
                xdistance = xdistance + 6 + 3
                valid = True

            elif (location[3] == '8'):
                ydistance = ydistance + 108 - 1
                xdistance = xdistance + 6 + 9
                valid = True

            elif (location[3] == '9'):
                ydistance = ydistance + 108 - 1
                xdistance = xdistance + 6 + 15
                valid = True

        elif (size == 5):
            if (location[4] == '0'):
                ydistance = ydistance + 108 - 1
                xdistance = xdistance + 6 + 21
                valid = True

            elif (location[4] == '1'):
                ydistance = ydistance + 108 - 1
                xdistance = xdistance + 6 + 27
                valid = True

            elif (location[4] == '2'):
                ydistance = ydistance + 108 - 1
                xdistance = xdistance + 6 + 33
                valid = True


#Shelf D ###########################################
elif ((location[0] == 'D') or (location[0] == 'd')):
    if (location [1] == '1'):
        if (size == 4):
            if (location[3] == '1'):
                ydistance = ydistance + 60 + 1
                xdistance = xdistance + 66 + 3
                valid = True

            elif (location[3] == '2'):
                ydistance = ydistance + 60 + 1
                xdistance = xdistance + 66 + 9
                valid = True

            elif (location[3] == '3'):
                ydistance = ydistance + 60 + 1
                xdistance = xdistance + 66 + 15
                valid = True

            elif (location[3] == '4'):
                ydistance = ydistance + 60 + 1
                xdistance = xdistance + 66 + 21
                valid = True

            elif (location[3] == '5'):
                ydistance = ydistance + 60 + 1
                xdistance = xdistance + 66 + 27
                valid = True

            elif (location[3] == '6'):
                ydistance = ydistance + 60 + 1
                xdistance = xdistance + 66 + 33
                valid = True

            elif (location[3] == '7'):
                ydistance = ydistance + 84 - 1
                xdistance = xdistance + 66 + 3
                valid = True

            elif (location[3] == '8'):
                ydistance = ydistance + 84 - 1
                xdistance = xdistance + 66 + 9
                valid = True

            elif (location[3] == '9'):
                ydistance = ydistance + 84 - 1
                xdistance = xdistance + 66 + 15
                valid = True

        elif (size == 5):
            if (location[4] == '0'):
                ydistance = ydistance + 84 - 1
                xdistance = xdistance + 66 + 21
                valid = True

            elif (location[4] == '1'):
                ydistance = ydistance + 84 - 1
                xdistance = xdistance + 66 + 27
                valid = True

            elif (location[4] == '2'):
                ydistance = ydistance + 84 - 1
                xdistance = xdistance + 66 + 33
                valid = True
                
    if (location [1] == '2'):
        if (size == 4):
            if (location[3] == '1'):
                ydistance = ydistance + 84 + 1
                xdistance = xdistance + 66 + 3
                valid = True

            elif (location[3] == '2'):
                ydistance = ydistance + 84 + 1
                xdistance = xdistance + 66 + 9
                valid = True

            elif (location[3] == '3'):
                ydistance = ydistance + 84 + 1
                xdistance = xdistance + 66 + 15
                valid = True

            elif (location[3] == '4'):
                ydistance = ydistance + 84 + 1
                xdistance = xdistance + 66 + 21
                valid = True

            elif (location[3] == '5'):
                ydistance = ydistance + 84 + 1
                xdistance = xdistance + 66 + 27
                valid = True

            elif (location[3] == '6'):
                ydistance = ydistance + 84 + 1
                xdistance = xdistance + 66 + 33
                valid = True

            elif (location[3] == '7'):
                ydistance = ydistance + 108 - 1
                xdistance = xdistance + 66 + 3
                valid = True

            elif (location[3] == '8'):
                ydistance = ydistance + 108 - 1
                xdistance = xdistance + 66 + 9
                valid = True

            elif (location[3] == '9'):
                ydistance = ydistance + 108 - 1
                xdistance = xdistance + 66 + 15
                valid = True

        elif (size == 5):
            if (location[4] == '0'):
                ydistance = ydistance + 108 - 1
                xdistance = xdistance + 66 + 21
                valid = True

            elif (location[4] == '1'):
                ydistance = ydistance + 108 - 1
                xdistance = xdistance + 66 + 27
                valid = True

            elif (location[4] == '2'):
                ydistance = ydistance + 108 - 1
                xdistance = xdistance + 66 + 33
                valid = True


#Error Calc
YError = (ydistance * StrErrMeanY) + (xdistance * (0-TurnErrMeanX))
XError = (xdistance * StrErrMeanX) + (ydistance * TurnErrMeanY)

if (valid == True):
    print("The error should be (roughly) {0:.2f} cm to the right and {1:.2f} cm to far.".format(XError, YError))
else:
    print("Please enter a valid box position next time.")
