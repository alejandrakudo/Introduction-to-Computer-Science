'''This function calculates the area of a rectangle given its ;ength and width
Input: length -- is the length of the rectangle
       width -- is the width of the rectangle
Output: the area
'''
def areaRectangle(length, width):
    if (length < 0):
        print("the length is less than 0")
        return
    elif (width > 100):
        print("the width is greater than 100")
        return
    elif (length * width == 500):
        print("500 is the value")
        return # the returns in this part are redundant 
    else:
        area = length*width #equation for calculating the area
        return area

def print10Times():
    

def main():
    length = eval(input("Please enter the length of the rectangle:"))
    width = eval(input("Please enter the width of the rectangle: "))
    theArea = areaRectangle(length,width)
   
main()

