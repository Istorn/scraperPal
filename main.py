from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import csv
from time import sleep

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.paypal.com/billing/subscriptions/list/all?page_size=20&page=1")



ok =input("Press key to proceed after you logged into your PayPal account")
print("Login completed.")
sleep(3)

"""number of pages given by PayPal business paginated table. 
Change it accordingly to the number of pages you'll have over the platform
"""
number_of_pages=1


print(f"Number of pages {number_of_pages}")
print("I'm gonna take out IDs and emails of your subscribers")

subcription_ids=driver.find_elements_by_class_name("list-plan__link")
email_ids=[]
for i in range(0,19):
    subscriber_id=subcription_ids[i].text
    subscriber_email=driver.find_element_by_id(f"email_address_{i}").text
    email_ids.append([subscriber_id,subscriber_email])


next_pages_link="https://www.paypal.com/billing/subscriptions/list/all?page_size=20&page="

print("salvo nel file")
with open("abbonamenti_nnullati.csv", mode="a") as file_csv:
    print("scrivo di riga in riga")
    writer=csv.writer(file_csv,delimiter=",",quotechar='"')
    for k in range(0,len(email_ids)):
        writer.writerow([email_ids[k]])

driver.close()
email_ids=[]
        


for pagina in range(2,number_of_pages):
    print(f"vado alla pagina {pagina}")
    driver.get(next_pages_link+str(pagina))
    sleep(3)
    email_ids=[]
    subcription_ids=driver.find_elements_by_class_name("list-plan__link")
    for i in range(0,20):
        subscriber_id=subcription_ids[i].text
        subscriber_email=driver.find_element_by_id(f"email_address_{i}").text
        email_ids.append([subscriber_id,subscriber_email])


    next_pages_link="https://www.paypal.com/billing/subscriptions/list/all?page_size=20&page="

    print("I'm saving into the 'subscribers_list.csv' file")
    with open("subscribers_list.csv", mode="a") as file_csv:
        print("I'm writing line by line")
        writer=csv.writer(file_csv,delimiter=",",quotechar='"')
        for k in range(0,len(email_ids)):
            writer.writerow([email_ids[k]])



driver.close()