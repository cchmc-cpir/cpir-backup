# cpir-backup

Backup utility for all repositores under this organization.

## Purpose

This tool uses the `requests` module to perform a GET request to the GitHub REST API for the names of all of the repositories contained in the `cchmc-cpir` organization. Then, it uses the `GitPython` module to clone each repository to the current working directory.

If desired, this tool can be used to cut a copy of the `cchmc-cpir` organization's repositories for any reason. However, it is intended to perform a simple backup to ensure files can be recovered in case anything goes south for GitHub.

## Use

This module requires Python 3.x.x (I used 3.6.3, but other versions may be compatible) and the `requests` and `GitPython` modules. It can be used by simply executing the Python script. Various parameters can be changed (e.g. the URLs pointing at the `cchmc-cpir` page specifically, or where the repositories are cloned to).
