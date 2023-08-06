import requests
import re
from bs4 import BeautifulSoup


def read_website(url):
    """
    Reads the HTML content of a website using BeautifulSoup and compiles an array of inner-most HTML tags.

    Args:
        url (str): The URL of the website to be read.

    Returns:
        list: A list of inner-most HTML tags.
    """
    try:
        # Send a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')

            # Define a helper function to recursively find inner-most HTML tags, excluding script and other common
            # JavaScript or HTML code tags, and tags with less than 100 characters of text
            def find_inner_most_tags(tag):
                inner_most_tags = []
                if not tag.find_all():
                    if len(tag.get_text(strip=True)) >= 100:
                        inner_most_tags.append(tag)
                else:
                    for child in tag.find_all(recursive=False):
                        if child.name not in ['script', 'style'] and len(child.get_text(strip=True)) >= 100:
                            inner_most_tags.extend(find_inner_most_tags(child))
                return inner_most_tags

            # Find inner-most HTML tags, excluding script and other common JavaScript or HTML code tags, and tags with
            # less than 100 characters of text
            inner_most_tags = find_inner_most_tags(soup)

            # Extract text content from inner-most HTML tags
            text_list = [tag.get_text(strip=True) for tag in inner_most_tags]
            full_text = ' '.join(text_list)
            # Remove newline characters from the combined string
            full_text = full_text.replace('\n', '')

            # Replace multiple spaces with a single space using regex
            full_text = re.sub(r'\s+', ' ', full_text)
            return full_text
        else:
            print(f'Request to {url} failed with status code {response.status_code}')
    except Exception as e:
        print(f'Error reading website: {e}')


if __name__ == '__main__':
    full_text = read_website("https://www.indiatoday.in/india/story/will-fulfill-all-promises-karnataka-chief-minister-siddaramaiah-5-points-2381929-2023-05-20?utm_source=rss")
    print(full_text)

