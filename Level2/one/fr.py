

class Profile:
    def __init__(self,name,email,languageUsed):
        self.name = name
        self.email = email
        self.languageUsed = languageUsed
userOne=Profile("Badr","ansarinarete@gmail.com","Arabic")
userTwo=Profile("Mohamed","mohamed@gmail.com","English")
userThird=Profile("Ali","Ali@gmail.com","Chinese")
print(f"Name: {userOne.name}\nEmail: {userOne.email}\nLanguage: {userOne.languageUsed}")
print(f"Name: {userTwo.name}\nEmail: {userTwo.email}\nLanguage: {userTwo.languageUsed}")
print(f"Name: {userThird.name}\nEmail: {userThird.email}\nLanguage: {userThird.languageUsed}")
 
class Message:
    def __init__(self,masenger_name,receiver_name,message,date):
        self.masenger_name = masenger_name
        self.receiver_name = receiver_name
        self.message = message
        self.date = date
mesangerOne=Message("Badr","Mohamed","Hello","2025/1/27")
mesangerTwo=Message("Mohamed","Ali","Hi Ali","2025/1/26")
mesangerThird=Message("Sara","kawtar","Hello kawtar","2025/1/28")
print(f"Masenger Name: {mesangerOne.masenger_name}\nReceiver Name: {mesangerOne.receiver_name}\nMessage: {mesangerOne.message}\nDate: {mesangerOne.date}")
print(f"Masenger Name: {mesangerTwo.masenger_name}\nReceiver Name: {mesangerTwo.receiver_name}\nMessage: {mesangerTwo.message}\nDate: {mesangerTwo.date}")
print(f"Masenger Name: {mesangerThird.masenger_name}\nReceiver Name: {mesangerThird.receiver_name}\nMessage: {mesangerThird.message}\nDate: {mesangerThird.date}")


class Product:
    def __init__(self,name_product,price_product,description_product,feedback):
        self.name_product = name_product
        self.price_product = price_product
        self.description_product = description_product
        self.feedback = feedback
productOne=Product("Iphone",1000,"The best phone","Good")
productTwo=Product("Samsung",800,"The best phone","Good")
productThird=Product("Huawei",700,"The best phone","Good")
print(f"Product Name: {productOne.name_product}\nPrice: {productOne.price_product}\nDescription: {productOne.description_product}\nFeedback: {productOne.feedback}")
print(f"Product Name: {productTwo.name_product}\nPrice: {productTwo.price_product}\nDescription: {productTwo.description_product}\nFeedback: {productTwo.feedback}")
print(f"Product Name: {productThird.name_product}\nPrice: {productThird.price_product}\nDescription: {productThird.description_product}\nFeedback: {productThird.feedback}")