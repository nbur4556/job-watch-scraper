from page_crawler import get_url, load_page
import csv


def main():
    keyword = 'Javascript'
    location = 'Austin'

    url = get_url(keyword, location)
    bs_page = load_page(url)
    job_count = parse_result(bs_page)

    write_result(keyword, location, job_count)


# Return job count as an integer
def parse_result(page):
    result_loc = page.find_all('div', id="searchCountPages")
    result_str = str(result_loc[0])
    count = result_str[58:-11]
    return int(count)


def write_result(keyword, location, count):
    writer = csv.writer(open('results.csv', mode='a', newline=''),
                        delimiter=',', quotechar='"')

    # TODO: include date in result file
    writer.writerow([keyword, location, count])


# Run Application
main()

# TODO: separate result CSV's for each tracked keyword
# TODO: automate script at set time daily
# TODO: graphing and data analysis options
