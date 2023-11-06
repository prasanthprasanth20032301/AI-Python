class multiplefunction():
    def Subfields():
        lists=["Sub-fields in AI are:","Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        for sub in lists:
            print(sub)

    def evenodd():
        num=int(input("Enter the number:"))
        if((num%2)==0):
            print("Even number")
            msg="Even number"
        else:
            print("Odd number")
            msg="Odd number"
        return msg 

    def Elegible():
        gender=input("Your Gender:")
        age=int(input("Your Age:"))
        if ((gender=="Male") and (age<=20)):
            print("NOT ELIGIBLE")
            marriage="NOT ELIGIBLE"
        elif  ((gender=="Female") and (age<18)): 
            print("NOT ELIGIBLE")
            marriage="NOT ELIGIBLE"
        else:
            print("ELIGIBLE")
            marriage="ELIGIBLE"
        return marriage  

    def percentage():
        subject1= 98
        subject2= 87
        subject3= 95
        subject4= 95
        subject5= 93
        addition=subject1+subject2+subject3+subject4+subject5
        percentage=(addition/500)*100
        print("Total:",addition)
        marks="Total:"
        print("percentage:",percentage) 
        marks="percentage:"
        return  marks 

    def triangle():
        height=32
        breadth=34
        area=(32*34)/2
        print("Area of Triangle:",area)
        Height1:2
        Height2:4
        Breadth:4
        perimeter=2+4+4
        print("Perimeter of Triangle:",perimeter)
