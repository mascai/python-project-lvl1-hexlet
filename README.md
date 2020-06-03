#1

# 2 Installation
poetry build
poetry config repositories.test_repo https://test.pypi.org/legacy
poetry publish --repository test_repo
