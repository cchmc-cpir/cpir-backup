import logging
import requests
from git import Repo

API_URL = 'https://api.github.com/orgs/cchmc-cpir/repos'
REM_URL = 'https://github.com/'


def logger_init(logger_name='cchmc-cpir_backup'):
    """Initialize a simple logger."""

    # return a logger for the initialization
    LOGGER = logging.getLogger(logger_name)
    LOGGER.setLevel(logging.DEBUG)

    # handlers for the log statements
    file_handler = logging.FileHandler(logger_name + '.log')
    console_handler = logging.StreamHandler()

    # log statement formatting
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # add both handlers to the current logger
    LOGGER.addHandler(file_handler)
    LOGGER.addHandler(console_handler)


def get_repos(URL):
    """HTTP GET request repository names from GitHub."""

    repos = []
    r = requests.get(URL)
    data = r.json()
    for repo in data:
        repos.append(repo['full_name'])

    return repos


def clone_repos(URL, repo_list):
    """Clone repositories using names from a list."""

    for repository in repo_list:
        Repo.clone_from(URL + '/' + repository, repository)


if __name__ == '__main__':
    logger_init()
    logger = logging.getLogger('cchmc-cpir_backup')

    # get repo names and clone them to specifed directory
    repo_list = get_repos(API_URL)
    clone_repos(REM_URL, repo_list)
    logger.debug("Done. ")
