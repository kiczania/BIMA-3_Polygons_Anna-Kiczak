import math

numOfPoints = int(input('Give the number of points in a polygon : '))

# Asking for number of polygon points
while (numOfPoints)<3:
    # a figure/polygon must have at least 3 points
    numOfPoints = int (input('Needs more than three points: '))

print('Give the x and y values in counter clockwise direction (in rows - value of x + enter, value y + enter): ')
# Creating empty lists for x and y s
x = []
y = []   

n =  numOfPoints
for i in range( 0, n):
    print( 'Point ' + str(i) + ':' )
    #[a, b] = map( lambda x: int( x ), input('').split(' ') )
    a = int(input(''))
    b = int(input(''))
    x.append( a ) # syntax for adding input s to created empty lists
    y.append( b ) # syntax for adding input s to created empty lists


# table header
print (f"{'Point':<7} {'x':<7} {'y':<7}")
print("-" * 20)

for i in range(0,n): # printing entered s
    print(f"{(i+1):<6} {x[i]:<7.2f} {y[i]:<7.2f}")

Ax = 0.0
Sx = 0.0
Sy = 0.0
Ix = 0.0
Iy = 0.0
Ixy = 0.0

for i in range(0, n):
    Ax += ((x[i] + x[(i+1)%n]) * (y[(i+1)%n] - y[i])) / 2.0
    Sx += ((x[(i+1)%n] - x[i]) * (y[(i+1)%n]**2 + y[i] * y[(i+1)%n] + y[i]**2 )) /-6.0
    Sy += ((y[(i+1)%n] - y[i]) * (x[(i+1)%n]**2 + x[(i+1)%n]* x[i] + x[i]**2)) / 6.0
    Ix += ((x[(i+1)%n] - x[i]) * (y[(i+1)%n]**3 + y[(i+1)%n]**2 *y[i] + y[(i+1)%n]* y[i]**2 + y[i]**3)) / -12.0
    Iy += ((y[(i+1)%n] - y[i]) * (x[(i+1)%n]**3 + x[(i+1)%n]**2 *x[i] + x[(i+1)%n]* x[i]**2 + x[i]**3)) / 12.0 
    Ixy += ((y[(i+1)%n] - y[i]) * ((y[(i+1)%n] * (3 * x[(i+1)%n]**2 + 2 * x[(i+1)%n] * x[i] + x [i]**2)) + (y[i] * (3 * x[i]**2 + 2 * x[(i+1)%n] * x [i] + x[(i+1)%n]**2)))) / -24.0

print("-" * 20)
print( 'Geometric characteristics:' )
print(f"{'Ax:':10}{Ax:>5.2f}")
print(f"{'Sx:':10}{Sx:>5.2f}")  
print(f"{'Sy:':10}{Sy:>5.2f}")
print(f"{'Ix:':10}{Ix:>5.2f}")
print(f"{'Iy:':10}{Iy:>5.2f}")
print(f"{'Ixy:':10}{Ixy:>5.2f}")

Xt=Sy/Ax
Yt=Sx/Ax
Ixt=Ix-((Yt**2)*Ax)
Iyt=Iy-((Xt**2)*Ax)
Ixyt=Ixy+(Xt*Yt*Ax)

print(f"{'Xt:':10}{Xt:>5.2f}")
print(f"{'Yt:':10}{Yt:>5.2f}")
print(f"{'Ixt:':10}{Ixt:>5.2f}")
print(f"{'Iyt:':10}{Iyt:>5.2f}")
print(f"{'Ixyt:':10}{Ixyt:>5.2f}")

#Output:
#Point   x       y      
#--------------------
#1      1.00    1.00
#2      3.00    1.00
#3      3.00    3.00
#0      1.00    3.00
#--------------------
#Geometric characteristics:
#Ax:        4.00
#Sx:        8.00
#Sy:        8.00
#Ix:       17.33
#Iy:       17.33
#Ixy:      -16.00
#Xt:        2.00
#Yt:        2.00
#Ixt:       1.33
#Iyt:       1.33
#Ixyt:      0.00