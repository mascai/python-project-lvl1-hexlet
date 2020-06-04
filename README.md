# 0 Usage
- ``` pip install --user --extra-index-url  https://test.pypi.org/simple/ mascai-brain-games ```
- Input ```brain-calc```
- Enjoy the game

[![asciicast](https://asciinema.org/a/LawHLYmcOdExLAEhhFQGw1wJ9.svg)](https://asciinema.org/a/LawHLYmcOdExLAEhhFQGw1wJ9)


# 1 Initial poetry


# 2 Publication
poetry build

poetry config repositories.test_repo https://test.pypi.org/legacy

poetry publish --repository test_repo

<a href="https://codeclimate.com/github/codeclimate/codeclimate/maintainability"><img src="https://api.codeclimate.com/v1/badges/a99a88d28ad37a79dbf6/maintainability" /></a>

<a href="https://codeclimate.com/github/codeclimate/codeclimate/test_coverage"><img src="https://api.codeclimate.com/v1/badges/a99a88d28ad37a79dbf6/test_coverage" /></a>

[![Build Status](https://travis-ci.org/mascai/python-project-lvl1-hexlet.svg?branch=master)](https://travis-ci.org/mascai/python-project-lvl1-hexlet)
