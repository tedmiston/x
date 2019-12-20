setup:
	@wget https://chromedriver.storage.googleapis.com/79.0.3945.36/chromedriver_linux64.zip && unzip chromedriver_linux64.zip && rm chromedriver_linux64.zip

build:
	@# docker build -t tedmiston/x/selenium-ci-example:latest
	@echo todo

run:
	@# docker run tedmiston/x/selenium-ci-example:latest
	@python3 -m app
