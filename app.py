from page_crawler import Page_Crawler
import csv
import datetime


def main():
    keyword = input('Enter search keyword: ')
    location = input('Enter search location: ')

    indeed_crawler = Page_Crawler(
        keyword, location, exp=r'([Pp]age\s1\sof\s[0-9]*\sjobs)', trim_start=10, trim_end=5)
    indeed_crawler.load_page()
    job_count = indeed_crawler.parse_result()

    write_result(keyword, location, job_count)


def write_result(keyword, location, count):
    dt = datetime.datetime.now()
    writer = csv.writer(open(f'results/{keyword}_{location}.csv', mode='a', newline=''),
                        delimiter=',', quotechar='"')

    writer.writerow([dt.date(), dt.time(), keyword, location, count])


# Run Application
main()

# TODO: separate result CSV's for each tracked keyword
# TODO: automate script at set time daily
# TODO: graphing and data analysis options
