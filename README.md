[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

# MediMindeRx Mobile
  
![logo](./assets/logo.png)</br>

* Jordan Shryock
  * [Github](https://github.com/jordy1611) 
  * [LinkedIn](https://www.linkedin.com/in/jordan-shryock-6a48b9113/)

* Kathy Bui
  * [Github](https://github.com/kathybui732) 
  * [LinkedIn](https://www.linkedin.com/)

* Kwibe Merci
  * [Github](https://github.com/jkwibe) 
  * [LinkedIn](https://www.linkedin.com/)


## Abstract
Never forget your medical supplies again! This mobile app serves to track reminders for medical supplies and notify the user at a given time. 

## Set up 
Follow the steps below to get this database up and running on your local environment:

### Prerequisites
* PostgreSQL installed 
  * [Homebrew Install](https://formulae.brew.sh/formula/postgresql)
  * [Browser Install](https://www.postgresql.org/download/)

* Postico Installed 
  * [Homebrew Install](https://formulae.brew.sh/cask/postico)
  * [Browser Install](https://eggerapps.at/postico/)

* Python3 Installed
  * [Homebrew Install](https://formulae.brew.sh/formula/python@3.8)
  * [Browser Install](https://www.python.org/downloads/)


### Installation
* Clone down this repo
  * `git clone git@github.com:MediMindeRx/MediMindeRx_BE.git`

* CD into directory

* Create project database in PostgreSQL
  * In the Terminal
  * `psql` - starts PostgreSQL command line interfac
  * `CREATE DATABASE mediminderx_be;`
  * `\q` or `control d` to exit psql command line interface
  * In regular terminal command line interface
  * `export POSTGRES_URL=“127.0.0.1:5432”`
  * `export POSTGRES_USER=“postgres”`
  * `export POSTGRES_PW=“”`
  * `export POSTGRES_DB=mediminderx_be`

* Initialize database for first time with
  1. `python3 -m venv env`
  2. `source env/bin/activate`
  3. `pip3 install -r requirements.txt`
  4. `python migrate.py db init (this creates a db, so make sure you don’t have one already in postico)`
  5. `python migrate.py db migrate`
  6. `python migrate.py db upgrade`
  7. `python run.py`

* Intialize database after first time

## Tech Stack 
- PostgreSQL
- Postico
- Python3
- Flask
- Testing Software
- Testing Software

### Future Extentensions
- Option to send texts to family members via Twilio api

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/MediMindeRx/MediMindeRx-Mobile.svg?style=flat-square
[contributors-url]: https://github.com/MediMindeRx/MediMindeRx-Mobile/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/MediMindeRx/MediMindeRx-Mobile.svg?style=flat-square
[forks-url]: https://github.com/MediMindeRx/MediMindeRx-Mobile/network/members
[stars-shield]: https://img.shields.io/github/stars/MediMindeRx/MediMindeRx-Mobile.svg?style=flat-square
[stars-url]: https://github.com/MediMindeRx/MediMindeRx-Mobile/stargazers
[issues-shield]: https://img.shields.io/github/issues/MediMindeRx/MediMindeRx-Mobile.svg?style=flat-square
[issues-url]: https://github.com/MediMindeRx/MediMindeRx-Mobile/issues