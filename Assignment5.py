import requests
import smtplib

SHEETY_ENDPOINT = "https://api.sheety.co/b79503c4c22d9c3cd71b8e5a9d6ab1d4/carShowroom/carShowroom"

def car_details() :
    response = requests.get(url=SHEETY_ENDPOINT)
    data = response.json()
    details = data.get("carShowroom")
    return details

def car_details_match(max_car_stock, min_car_stock, car_price, car_name, car_model, car_color, car_condition) :
    car_details_match_list = []
    if min_car_stock < max_car_stock :
        car_details_match_list.append(car_name)
        car_details_match_list.append(car_model)
        car_details_match_list.append(car_color)
        car_details_match_list.append(car_condition)
        car_details_match_list.append(car_price)
        car_details_match_list.append(min_car_stock)
        car_details_match_list.append(max_car_stock)
        return car_details_match_list

    else :
        return


def email_sending(match_car_details) :
    sender_email = "muhammadahmedraza987@gmail.com"
    sender_password = "bppt gjqf yiqk ptxk"
    company_email = "ahmedofficial346@gmail.com"
    subject = f" CAR SHOWROOM "
    body = f""" 
            CAR DETAILS : {match_car_details}
            """
    message = f"Subject: {subject} \n\n {body}"
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(sender_email, sender_password)
    s.sendmail(sender_email, company_email, message)
    print(f"Email sent to {company_email} Successfully !")


for car_detail in car_details() :
    car_name = car_detail["carName"]
    car_model = car_detail["carModel"]
    car_color = car_detail["carColor"]
    car_condition = car_detail["carCondition"]
    car_price = car_detail["carPrice"]
    min_car_stock = car_detail["minimumCarStock"]
    max_car_stock = car_detail["maximumCarStock"]
    match_car_details = car_details_match(max_car_stock, min_car_stock, car_price, car_name, car_model, car_color, car_condition)
    email_sending(match_car_details)