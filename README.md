# QA-Project
## Josh Early and Ian McCracken
### Installation
First, clone this repository by running `git clone https://github.com/PapiJoker/QA-Project.git` in the folder where you want the project located.
Then, install the dependencies by running `pip install -r requirements.txt`.
If you're missing `pip`, try `python -m pip install -r requirements.txt`.
Visit [here](https://packaging.python.org/en/latest/tutorials/installing-packages/) if you're still having trouble.
Finally, run the app with `python run.py`.

### Running Tests
Have one terminal open which is running the server locally on your machine (follow the above commands).
Then, open another terminal and run `python -m pytest`.
This command will run all the tests found by `pytest`; both end-to-end and unit tests.