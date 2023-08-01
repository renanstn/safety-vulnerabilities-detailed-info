import argparse

import requests
from bs4 import BeautifulSoup


def main(url):
    html = requests.get(url.strip())
    if html.status_code != 200:
        raise Exception("The page can't be loaded")

    # Load parser
    soup = BeautifulSoup(html.text, "html.parser")

    # Get vulnerability severity ----------------------------------------------
    rating_element = soup.find(id="severity-rating")
    level_element = rating_element.find_previous_sibling("span")
    vulnerability_level = level_element.text.strip()

    # Get vulnerability name --------------------------------------------------
    title_element = soup.find("h1")
    title_parent_element = title_element.parent
    vulnerability_title_element = title_parent_element.find_next_sibling("p")
    vulnerability_title = vulnerability_title_element.text.strip()

    # Print results -----------------------------------------------------------
    print(f"- {vulnerability_title} - {vulnerability_level}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Get vulnerability details from a pyup.io page."
    )
    parser.add_argument("url", type=str, help="The pyup.io URL to be scrapped.")

    args = parser.parse_args()
    main(args.url)
