#Andrew Nally
#CIS261-OOP
#Rectangle
#11/19/2023

def printRectangle(height, width):
    for i in range(height):
        for j in range(width):
            if i == 0 or i == height - 1 or j == 0 or j == width - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print("") 

print("Rectangle Calculator")
print("Let's Begin...!")
height = int(input("Height: "))  
width = int(input("Width: "))    
area = height * width
perimeter = 2 * (height + width)
print(f"Perimeter: {perimeter}")
print(f"Area: {area}")


printRectangle(height, width)


