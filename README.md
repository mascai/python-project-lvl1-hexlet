<a href="https://codeclimate.com/github/codeclimate/codeclimate/maintainability"><img src="https://api.codeclimate.com/v1/badges/a99a88d28ad37a79dbf6/maintainability" /></a>

<a href="https://codeclimate.com/github/codeclimate/codeclimate/test_coverage"><img src="https://api.codeclimate.com/v1/badges/a99a88d28ad37a79dbf6/test_coverage" /></a>

[![Build Status](https://travis-ci.org/mascai/python-project-lvl1-hexlet.svg?branch=master)](https://travis-ci.org/mascai/python-project-lvl1-hexlet)

# 0 Installation
- ``` pip install --user --extra-index-url  https://test.pypi.org/simple/ mascai-brain-games ```
- Enjoy the games

[![asciicast](https://asciinema.org/a/yFKN0SjkgUmR7htHeiRWDMCvJ.svg)](https://asciinema.org/a/yFKN0SjkgUmR7htHeiRWDMCvJ)

# 1 Games

### 1.1 Even numbers
[![asciicast](https://asciinema.org/a/lQSODtjVzlSOWvyv5HQfDT2vb.svg)](https://asciinema.org/a/lQSODtjVzlSOWvyv5HQfDT2vb)

### 1.2 Calculator
[![asciicast](https://asciinema.org/a/EWKAyFWVsPWclONYPNAxh16bi.svg)](https://asciinema.org/a/EWKAyFWVsPWclONYPNAxh16bi)

### 1.3 Gratest Common Divider (GCD)
[![asciicast](https://asciinema.org/a/lB5O0XErNQq93ELtdRGpvIgTK.svg)](https://asciinema.org/a/lB5O0XErNQq93ELtdRGpvIgTK)

### 1.4 Prime numbers
[![asciicast](https://asciinema.org/a/OkLJ2TM4a8Wv2xqRwUoaNXvJE.svg)](https://asciinema.org/a/OkLJ2TM4a8Wv2xqRwUoaNXvJE)

### 1.5 Progression
[![asciicast](https://asciinema.org/a/UEAzmP08RnSqO7kOMXN0BkYt9.svg)](https://asciinema.org/a/UEAzmP08RnSqO7kOMXN0BkYt9)

# 2 Publication
poetry build

poetry config repositories.test_repo https://test.pypi.org/legacy

poetry publish --repository test_repo


