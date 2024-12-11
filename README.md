# Weather Data Automation Project

#  Computer Infrastructure

## Author: Gabriela Domiciano Avellar
Teacher: Ian McLoughlin

I study at [ATU](https://www.atu.ie).

![weather](https://www.acetireland.ie/wp-content/uploads/2019/06/4-seasons-1024x1024.jpg)

### Overview

This project automates the process of downloading weather data from the [Met Eireann](https://data.gov.ie/dataset/todays-weather-athenry) and stores it in a timestamped format. The data is then pushed to a GitHub repository daily, utilizing GitHub Actions for automation.


### Project Structure 📁

data/  - Directory that contains the weather data and timestamps.

timestamps/ - Contains timestamped files.

weather/ - Contains weather data.

weather.sh - Bash script to download and store weather data.

weather.ipynb - Jupyter notebook summarizing the tasks and data analysis.

github/workflows/ - Contains the GitHub Actions workflow to automate the script


### How to Get Started 🛠️

Follow these steps to get started with the Weather Data Automation Project:

- Clone the Repository with git clone.
- Open in VSCode, to open the project locally or Codespaces, to work directly in the browser.
- Make sure you have Python installed and run.
- Run the Scripts. Download the data manually with bash weather.sh and analyze the data by opening the jupyter notebook weather.ipynb.
- The project is already configured with GitHub Actions.

### Running the Project 💻

The project is automated using GitHub Actions. Data is downloaded every day at 10am and pushed to the repository.


### References 📚

- Classes we had over the semester [Professor Ian McLoughlin Git Hub](https://github.com/ianmcloughlin/2425_computer_infrastructure).

- I used ChatGpt to help understand and write some codes, asking to explain in simple ways. Write the script in weather-data.yml.

- GitHub Codespaces overview [GitHub](https://docs.github.com/en/codespaces/overview).

- Understand what is important to analyze in weather data [A Guide to Climate Analysis](https://blog.weatherstack.com/blog/leveraging-historical-weather-data-for-climate-analysis/).

- Information about de [Today's weather Athenry](https://data.gov.ie/dataset/todays-weather-athenry).

- Command Line for Beginners [How to Use the Terminal Like a Pro](https://www.freecodecamp.org/news/command-line-for-beginners/).
