
arr = [2,1,4,7,3,2,5]

# timeLaunch = "19 50"
# timeTravel = "02 20"
#
# departureTimeHH,departureTimeMM = input().split(" ")
# TravelTimeHH,TravelTimeMM = input().split(" ")
# departureTimeHH = int(departureTimeHH)
# departureTimeMM = int(departureTimeMM)
# TravelTimeHH = int(TravelTimeHH)
# TravelTimeMM = int(TravelTimeMM)
#
# totalMinutesOfTravel = (TravelTimeHH * 60) + TravelTimeMM
# print(totalMinutesOfTravel)
# for x in range(1, totalMinutesOfTravel+1):
#     departureTimeMM += 1
#     if departureTimeMM > 59:
#         departureTimeMM = 0
#         departureTimeHH += 1
#         if departureTimeHH > 23:
#             departureTimeHH = 0
#
# print(f"{departureTimeHH:02d}", f"{departureTimeMM:02d}")


a = input()
for i in range(int(a)):
    giftToBuy = int(input())
    numberOfgift = int(input())
    allGift = list(map(int , input().split()))
    allGift.sort()
    print(giftToBuy , numberOfgift , allGift)
    print(allGift[:giftToBuy])