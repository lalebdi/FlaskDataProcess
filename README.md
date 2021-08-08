
<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/lalebdi/DataProcess">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Data Processor API</h3>

</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#link">Link</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project



This is a Flask API deployed in AWS Elastic Beanstalk.


* Pay Load:
* {"value": "<value goes here>Insert_value", "mode": "phone || name || amount", "replace_with": "--blank-- || --original--"}
* :smile:



### Built With


* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
* [Flask_restful](https://flask-restful.readthedocs.io/en/latest/)
* [NameParser](https://nameparser.readthedocs.io/en/latest/)



<!-- GETTING STARTED -->
## Getting Started


To get a local copy up and running follow these simple example steps.

### Prerequisites

This is how to setup the software you need to use and how to install them.
* Python 3
  [https://www.python.org/downloads/](https://www.python.org/downloads/) 

### Installation


1. Clone the repo
   ```sh
   git clone https://github.com/lalebdi/DataProcess.git
   cd DataProcess
   ```
  
2. venv
   ```sh
   python3 -m venv .venv
   ```
3. Activate the environment
   ```sh
   source .venv/bin/activate
   ```
4. Install the requirements
   ```sh
   pip install -r requirements.txt
   ```
5. Export the Flask App
   ```sh
   export FLASK_APP="application.py" 
   ```
6. Run the app
   ```sh
   flask run
   ```

Your app will most likely run on  http://127.0.0.1:5000/ 

<!-- USAGE EXAMPLES -->
## Usage

This URL will accept a POST request with the following payload:
* {"value": "<value goes here>Insert_value", "mode": "phone || name || amount", "replace_with": "--blank-- || --original--"}

if input mode = phone:
{"original_value": "the original value property string", "mode": "phone", "output": "10 digit phone number or replace_with value if valid 10 digit phone number cannot be found"}

if input mode = name:
{"original_value": "the original value property string", "mode": "name", "output": {"first": "<first name>", "middle": "<middle name or initial>", "last": "<last name>"}}

* if valid name cannot be found/parsed, then return replace_with value for all 3 parameters (first, middle, last)

if input mode = amount:
{"original_value": "the original value property string", "mode": "amount", "output": "just numeric answer with precision of 2 places or replace_with value if valid numeric value cannot be found"}

In all 3 modes, if replace_with == "--original--", and a valid result cannot be found, then return the original input value for the output values

Some example inbound / expected outbound payloads:

IN:  {"value": "(512) 234-9293", "mode": "phone", "replace_with": "--blank--"}

OUT:  {"original_value": "(512) 234-9293", "mode": "phone", "output": "5122349293"}



IN:  {"value": "unknown", "mode": "phone", "replace_with": "--blank--"}

OUT:  {"original_value": "unknown", "mode": "phone", "output": "--blank--"}



IN:  {"value": "Robert Lance Smith", "mode": "name", "replace_with": "--blank--"}

OUT:  {"original_value": "Robert Lance Smith", "mode": "name", "output": {"first": "Robert", "middle": "Lance", "last": "Smith"}}



<!-- Link -->
## Link

[http://flaskdataprocess-env-1.eba-pnm98v4d.us-east-1.elasticbeanstalk.com/](http://flaskdataprocess-env-1.eba-pnm98v4d.us-east-1.elasticbeanstalk.com/)




<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

This is a private project and usage of anything in the project is prohibited.



<!-- CONTACT -->
## Contact

lalebdi - [https://www.leahwebdev.com](https://www.leahwebdev.com) 

Project Link: [https://github.com/lalebdi/DataProcess](https://github.com/lalebdi/DataProcess)

