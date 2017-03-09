class Box(object):
 
    length=int(input("Please enter the Length: "))

    width=int(input("Please enter the Widtht:"))

    height=int(input("Please enter the Height: "))

    def __init__(self, length=0,width=0,height=0):

        self.length=length

        self.width=width

        self.height=height

    volume=length*width*height

    print("The volume is:")

    print(volume)
    
class matchbox(Box):
    "class matchbox inheriting from class Box"

    def __init__(self, l,w,h):

     super().__init__(length,width,height)

     self.length=l

     self.width=w

     self.height=h
   
     volume_Of_matchbox=l*w*h
     
     print(volume_0f_room)