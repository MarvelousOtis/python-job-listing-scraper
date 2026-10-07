# python-job-listing-scraper
# Web Scraping Fake Python Jobs

## Project Description

This project is a beginner-friendly Python web scraping project that collects job listings from the [Fake Python Jobs](https://realpython.github.io/fake-jobs/) website.

The scraper extracts useful information from each job posting, including the job title, company name, location, and job detail page URL. The collected data is then organized into a structured dataset and saved as a CSV file for further analysis.

The website is intentionally designed for learning web scraping, making it suitable for practicing HTML inspection, element selection, data extraction, and data processing without dealing with complex anti-scraping protections.

---

## Project Requirements

* Scrape data from the [Fake Python Jobs](https://realpython.github.io/fake-jobs/) website
* Extract the following fields for each job posting:

  * Job title
  * Company name
  * Location
  * Job detail page URL
* Store the results in a CSV file
* Use clean and readable Python code
* Handle simple edge cases, such as missing fields

---

## Technologies Used

* **Python** – Programming language used to build the scraper
* **Requests** – Used to fetch the webpage
* **Beautiful Soup (bs4)** – Used to parse and navigate the HTML
* **Pandas** – Used to organize the scraped data into a DataFrame and export it as a CSV file

---

## How the Scraper Works

The scraping process follows these steps:

1. Send a request to the Fake Python Jobs website using `Requests`.
2. Retrieve the webpage's HTML.
3. Parse the HTML using Beautiful Soup.
4. Identify the HTML container for each job posting.
5. Loop through each job card.
6. Extract the job title, company name, location, and job detail URL.
7. Store each job as a dictionary.
8. Add each dictionary to a list.
9. Convert the list into a Pandas DataFrame.
10. Export the DataFrame as a CSV file.

### Scraping Workflow

```text
Website
   ↓
Requests
   ↓
HTML
   ↓
Beautiful Soup
   ↓
Find Job Cards
   ↓
Extract Job Information
   ↓
Store in Python List
   ↓
Pandas DataFrame
   ↓
CSV File
```

---

## Key Concepts Practiced

### Inspecting HTML

Browser developer tools were used to inspect the webpage and identify the HTML elements containing the required information.

For example, the job title is contained in:

```html
<h2 class="title is-5">Senior Python Developer</h2>
```

The company name is contained in:

```html
<h3 class="subtitle is-6 company">Payne, Roberts and Davis</h3>
```

The location is contained in:

```html
<p class="location">Stewartbury, AA</p>
```

The job detail page URL is stored in the `href` attribute of the Apply link.

### Finding Multiple Job Listings

Instead of extracting only the first job, the scraper identifies all job cards using:

```python
job_cards = soup.find_all("div", class_="card")
```

The scraper then loops through each job card and extracts the required information.

### Cleaning Extracted Text

The `.strip()` method is used to remove unnecessary spaces and line breaks from extracted text.

```python
location = job.find("p", class_="location").text.strip()
```

### Extracting URLs

The job URL is stored in the `href` attribute of the Apply link.

```python
job_link = job.find(
    "a",
    class_="card-footer-item",
    string="Apply"
)

url = job_link["href"]
```

---

## Output

The scraper collects **100 job postings** from the website.

The final dataset contains four columns:

| Column      | Description                 |
| ----------- | --------------------------- |
| `job_title` | Name of the job             |
| `company`   | Company offering the job    |
| `location`  | Job location                |
| `job_url`   | Link to the job detail page |

The data is saved as:

```text
fake_jobs.csv
```

---

## Example Output

| job_title               | company                      | location         | job_url |
| ----------------------- | ---------------------------- | ---------------- | ------- |
| Senior Python Developer | Payne, Roberts and Davis     | Stewartbury, AA  | Job URL |
| Energy Engineer         | Vance-Fitzpatrick            | Example Location | Job URL |
| Legal Executive         | Jackson, Rhodes and Mccarthy | Example Location | Job URL |

---

## What I Learned

Through this project, I practiced:

* Inspecting webpage HTML using browser developer tools
* Understanding HTML tags, classes, and attributes
* Sending HTTP requests with Python
* Parsing HTML with Beautiful Soup
* Using `find()` and `find_all()`
* Using loops to scrape multiple records
* Extracting text from HTML elements
* Extracting URLs from HTML attributes
* Cleaning scraped text using `.strip()`
* Organizing scraped information using dictionaries and lists
* Creating DataFrames with Pandas
* Exporting data to CSV
* Understanding the basic workflow of web scraping

---

## Future Improvements

Possible improvements for this project include:

* Adding stronger handling for missing fields
* Adding error handling for failed requests
* Cleaning and analyzing the scraped dataset
* Creating visualizations from the scraped data
* Using the dataset for further data analysis projects

---

## Project Structure

```text
web-scraping-fake-jobs/
│
├── scraper.py
├── fake_jobs.csv
└── README.md
```

---

## Source

[Fake Python Jobs](https://roadmap.sh/projects/job-listings-scraper)

This website is designed specifically for practicing web scraping.
