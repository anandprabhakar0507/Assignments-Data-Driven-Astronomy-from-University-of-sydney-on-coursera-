#This only works if you have an odd number of elements

fluxes = [17.3, 70.1, 22.3, 16.2, 20.7]
fluxes.sort()
mid = len(fluxes)//2
median = fluxes[mid]
print(median)

#If there are an even number of elements there are two middle ones, 
#so you have to find both and take their average:

fluxes = [17.3, 70.1, 22.3, 16.2, 20.7, 19.3]
fluxes.sort()
mid = len(fluxes)//2
median = (fluxes[mid - 1] + fluxes[mid])/2
print(median)