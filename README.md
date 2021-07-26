# ScraperPal

PayPal for Business does not offer an API endpoint to download all of your subscribers in one fell swoop, neither from the user interface.
This web scraper, based on Selenium, aim to solve this problem and get all of your subscribers in a single CSV file on your computer.

### How does it work

ScraperPal is based on [Selenium](https://selenium-python.readthedocs.io/).
Once you set the number of pages given over the PayPal UI into the `main.py` file, once you start the process, after a successful login into your PayPal business account, the scraper starts it process *automagically*.


### Installation, dependencies and use

ScraperPal requires Python3: https://www.python.org/downloads/

Once you installed Python3 you'll require different packages via pip.
**With a single click you can get [pip](https://pypi.org/project/pip/)**

1. Open a terminal window
2. Launch this command *if you didn't install **pip***:
```curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py```
3. Once you got pip, **install it otherwise go straightforwad to the step 4**:
```python3 get-pip.py```
4. To install all packages locate yourself into the project folder, *for example*:
```cd ~/scraperPal```

    Then, launch this command:

    ```pip install -r requirements.txt```

    After pip concluded its process, **you can finally use ScraperPal**

### How to use ScraperPal

Once you located yourself into the project folder, please launch the following command via CLI:

```python3 main.py```

A Chrome window will appear. *You need to log in PayPal for business, then press any key into the CLI window to proceed with the scraping of all your subscribers.*

The process will conclude automatically **generating a csv file inside of the project folder**.

### License

Creative Commons CC BY-NC 4.0: https://creativecommons.org/licenses/by-nc/4.0/