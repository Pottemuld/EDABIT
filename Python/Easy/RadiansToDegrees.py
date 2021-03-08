import math
def radToDeg(rad):
    deg = (rad * 180) / math.pi
    deg = round(deg,1)
    print("Radians: " + str(rad) + " -> " + str(deg) + " degrees")

radToDeg(1)
radToDeg(20)
radToDeg(50)