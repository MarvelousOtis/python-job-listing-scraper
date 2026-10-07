import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://realpython.github.io/fake-jobs/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

job_title = soup.find("h2", class_="title is-5")
print(job_title.text)

company = soup.find("h3", class_="company")
print(company.text)

location = soup.find("p", class_="location")
print(location.text.strip())

job_link = soup.find("a", class_="card-footer-item", string="Apply")
print(job_link["href"])

job_cards = soup.find_all("div", class_="card")
print(len(job_cards))

first_job = job_cards[0]
print(first_job)

title = first_job.find("h2", class_="title is-5").text.strip()
print(title)

company = first_job.find("h3", class_="company").text.strip()
print(company)

location = first_job.find("p", class_="location").text.strip()
print(location)

job_link = first_job.find("a", class_="card-footer-item", string="Apply")
print(job_link["href"])

data = []

for job in job_cards:
    title = job.find("h2", class_="title is-5").text.strip()
    company = job.find("h3", class_="company").text.strip()
    location = job.find("p", class_="location").text.strip()

    job_link = job.find("a", class_="card-footer-item", string="Apply")
    url = job_link["href"]

    row = {
        "job_title": title,
        "company": company,
        "location": location,
        "job_url": url
    }

    data.append(row)
print(len(data))

df = pd.DataFrame(data)
print(df.head())

df.to_csv("fake_jobs.csv", index=False)
