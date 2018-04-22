# Use return intstead of print, to save/store value
# Use good comments, got good programming style and marks
'''
This function calculates the area of a rectangle given its ;ength and width
Input: length -- is the length of the rectangle
       width -- is the width of the rectangle
Output: the area
'''
def areaRectangle(length, width):
    area = length*width #equation for calculating the area 
    return area 

def perimeterRect(rlength, rwidth):
    perim = 2* (length*width)
    print("The perimeter of the rectangle is", perim)

# eval, is a built in function, but you can also do int or float 
def main():
    length = eval(input("Please enter the length of the rectangle:"))
    width = eval(input("Please enter the width of the rectangle: "))
    theArea = areaRectangle(length,width)
    print("The square of the area is", theArea*theArea)
    perimeterRect(length, width)
    
main()

