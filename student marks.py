dictionary ={'Nikhil': 95,'Siya': 50,'sara':76,'Alice':85 }
user =(input("Enter the student's name:"))
if user in dictionary :
   print(f"{user}'s marks is {dictionary[user]}")
else :
    print("Student not found")