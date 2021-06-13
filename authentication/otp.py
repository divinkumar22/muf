from twilio.rest import Client
import random



def gen_otp():
    otp = random.randint(1000, 9999)
    return otp


def OTP(moble_no):
    otp = gen_otp()
    otp = str(otp)
    print(otp)
    
    # Your Account SID from twilio.com/console
    account_sid = "AC40a25ebaf63a399322b3fadb386d4835"
    # Your Auth Token from twilio.com/console
    auth_token  = "7056c503dc09d9ff922c7afe108d6491"

    client = Client("AC40a25ebaf63a399322b3fadb386d4835", "7056c503dc09d9ff922c7afe108d6491")

    message = client.messages.create(
        to="+91"+moble_no,
        from_="+15153617247",
        body=("your otp is "+otp))

    return  (otp)


