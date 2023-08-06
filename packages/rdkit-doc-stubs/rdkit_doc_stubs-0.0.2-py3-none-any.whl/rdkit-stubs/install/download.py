# %%
import os
import pickle

import requests
from bs4 import BeautifulSoup
from bs4.element import ResultSet, Tag
from tqdm import tqdm

# URL where the links of all RDKit modules are listed
BASE_URL = "https://www.rdkit.org/docs/api-docs.html"

# Base URL for the documentation of RDKit modules
BASE_SOURCE = "https://www.rdkit.org/docs/source/"

# User agent for the requests
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0",
}


def download_url(url: str) -> str:
    """Download the HTML of a URL"""
    item = requests.get(url, headers=HEADERS)
    item.encoding = "utf-8"
    return item.text


def get_base() -> BeautifulSoup:
    """Get the BeautifulSoup node of the base URL"""
    data = download_url(BASE_URL)
    node = BeautifulSoup(data, "html.parser")
    return node


def get_links(node: BeautifulSoup) -> list[str]:
    """Get the links of all RDKit modules"""

    # Find all links
    links: ResultSet[Tag] = node.find_all("a")

    # Filter for links that start with "source"
    href = [link.get("href") for link in links if link.get("href").startswith("source")]

    # Clean up the links
    links = [l.removeprefix("source/").split("#")[0] for l in href]
    links = list(set(links))

    return links


def download_data(links: list[str]) -> dict[str, str]:
    """Download the HTML of all URLs

    Returns a dictionary with the links as keys and the HTML as values.
    """
    data = {}
    for link in tqdm(links):
        url = BASE_SOURCE + link
        data[link] = download_url(url)

    return data


def dump_data(data: dict[str, str], dump: str) -> None:
    """Dump the data to a pickle file"""
    pickle.dump(data, open(dump, "wb"))


def load_data(dump: str) -> dict[str, str]:
    """Load the data from a pickle file"""
    return pickle.load(open(dump, "rb"))


def get_data(file: str) -> dict[str, str]:
    """Get the HTML of all RDKit modules and store them in a pickle file or load them from a pickle file if it exists"""

    # Get node and links from the RDKit documentation
    node = get_base()
    links = get_links(node)

    if not os.path.exists(file):
        # If the pickle file does not exist, download the HTML of all RDKit modules and store them in a pickle file
        data = download_data(links)
        dump_data(data, file)
    else:
        # Else load the HTML from the pickle file
        data = load_data(file)

    return data


# %%
