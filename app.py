from page_crawler import get_url, load_page


def main():
    url = get_url('Javascript', 'Austin')
    bs_page = load_page(url)
    job_count = parse_result(bs_page)

    print(job_count)


# Return job count as an integer
def parse_result(page):
    result_loc = page.find_all('div', id="searchCountPages")
    result_str = str(result_loc[0])
    count = result_str[58:-11]
    return int(count)


# Run Application
main()
