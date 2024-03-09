#მომხმარებლის ნიშნებისგან გამოანგარიშება საშვალო არითმეტიკული და თუ ცხრაზე მეტი იქნება

#დაუპრინტეთ გილოცავ მატრიცელო შენ გადმოგეცა 300 ლარიანი ბანძი ტოსტერი რისთვისაც შეალიე შენი ცხოვრების წლები

#თუ ეს იქნება 5ზე ნაკლები დაუპრინტე გილოცავ გაექეცი მატრიცას

#თუ იქნება 5 იდან 9 მდე დაუპრინტე YOU ARE MID

#თუ იქნება 10ზე მეტი ან 0ზე ნაკლები დაუპრინტე there is something wrong with you


user_grade1 = float(input("enter your grade in math: "))
user_grade2 = float(input("enter your grade in history: "))
user_grade3 = float(input("enter your grade in science: "))
user_grade4 = float(input("enter your grade in biology: "))


avg_grade = (user_grade1 + user_grade2 + user_grade3 + user_grade4) / 4


if avg_grade>=9 and avg_grade<=10:
    print("გილოცავ, მატრიცელო. შენი ქულაა: " + str(avg_grade) + " შენ გადმოგეცა 300 ლარიანი ბანძი ტოსტერი, რასაც შეალიე შენი ცხოვრების წლები")
elif avg_grade <=5 and avg_grade >= 0:
    print("შენი ქულაა: " + str(avg_grade) + " გილოცავ გაექეცი მატრიცას")
elif avg_grade >5 and avg_grade <9:
    print("შენი ქულაა: " + str(avg_grade) + " YOU ARE MID")
else:
    print( "შენი ქულაა: " + str(avg_grade + " there is something wrong with you"))



#მომხმარებელს შეეკითხეთ ხელფასი

#თუ 10000ზე მეტია, დაუპრინტეთ, გოა-ში სწავლობდი?

#თუ 1000----10000 -ია , დაუპრინტეთ you mid

#უ 1000-ზე დაბალია, დაუპრინტეთ, შემოსულიყავი გოაში, მატრიცელო 
 
user_salary=int(input("what's your salary?: "))
if user_salary  >10000:
    print("did you studied at goal oriented academy")
elif user_salary >1000 and user_salary <10000:
    print("you are mid join goa be a chad ")
else:
    print("why didn't joined goa" )



