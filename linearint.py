#See Canvas for more details. You are an engineer at NASA monitoring the International Space Station (ISS)
#as it orbits the Earth at a constant rate of speed. Since the ISS is moving at a constant speed, this 
#calculation can be found via linear interpolation. The first measurement was taken at time t=10 minutes, 
#and the second was taken 45 minutes later. At the first measurement, the ISS was 2029 kilometers past Houston, TX. 
#At the second measurement, the ISS was 23029 kilometers past Houston.

#Write a program named linear_interpolation.py that…

#Part 1: Determine, for a time of 25 minutes, where the ISS will be (in terms of kilometers past Houston).
#Part 2: Add to your program to determine, for a time of 300 minutes, where the ISS will be (in terms of kilometers past Houston).
#Use a comment to clearly label the two parts.



print("Part 1:")
speed = (23029-2029)/(45)
distance = speed*25
print(distance)
distance/=25
distance*=300
print("Part 2:")
print(distance)
