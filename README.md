<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

# Adludio Data Engineering and Machine Learning Challenge
## The Data Pipeline
![image](https://user-images.githubusercontent.com/44437166/183882188-001902e3-1054-4dc0-871b-c778a6c7499c.png)
**Table of contents**

- [Overview](#overview)
- [Data](##Data)
- [Requirements](#requirements)
- [Technologies](#Technologies)
- [Install](#install)
- [Usage](#Usage)
- [Licence](#Licence)
- [Author](#Author)
- [Acknowledgement](#Acknowledgement)

## Overview

> The goal of this challenge is to provide an implementation that satisfies the requirements for the tasks listed below and demonstrate coding style, software design and engineering skills. We will evaluate all submissions based on the following criteria
- Understanding of the problem being asked (you can always ask by email if something is not clear in this description)
- Attempting as many of the tasks as possible in the time given, and answering the questions asked. This is our main indicator of hard work.
- Creative and Innovative analysis for informative insights
- Your coding style as well as your software design and engineering skills
- Your communication of the findings or results

### About Adludio business 
> Adludio is an online mobile ad business. It provides the following service to its clients
Design an interactive Ad - what is also called a “creative”. A creative is a rich ad containing interaction elements through a mini-game engine, video, text, images, etc.. 
Serves these creatives to audiences on behalf of a client. In order to do that, adludio buys impressions from an open market through bidding.  
In order to make a good profit while also satisfying clients' needs, adludio employs campaign managers and bidding and other algorithms to optimize the bidding strategy. One of the algorithms we use is called inventory scoring i.e, ranking inventories such as site, and device type based on ads history performance. and it is used to optimize our targeting strategy.   




## Data
-   Please find the data sources in the [dataset folder](https://drive.google.com/drive/folders/1ZbUU43VrPHqJdRecatoZNlmWXcaeVj2G?usp=sharing) attached.
Design data ( global_design_data.json): 
This data is found by analyzing the advertisements using computer vision. It constitutes the ad-unit components. Note that the unique identifier in this data is game_key
Campaigns data (campaigns_inventory.csv) 
Campaign historical performance dataset. It contains historical inventories of the campaign created placed and also KPI events associated with it. The type column is the one you will find the KPI events. 
Briefs data (briefing.csv)
Campaign & creative plan data. 
Creative Assets(Creative_assets_) Zipped File
The data contains images for particular game keys. Use computer vision to extract features that enrich the already existing features in design data.

> please check this [dbt doc] to get a beter insight into the data



- [**Source of data:**]


## Technology Used

* [![DBT][DBT.com]][DBT-url]
* [![Docker][Docker.com]][Docker-url]
* [![Redash][Redash.com]][Redash-url]
* [![Airflow][Airflow.com]][Airflow-url]
* [![Postgres][Postgresql.com]][Postgresql-url]

### Prerequistes

- python 3.8
- Docker
- Docker Compose

### Installation

1. Clone and navigate to repo
    ```sh
    git clone https://github.com/benbel376/adludio_challenge.git
    cd adludio_challenge
    ```
2. Run the docker containers in the following order
    ```sh
    ./setup
    cd docker
    docker-compose -f docker-compose-postgres.yml up --build
    docker-compose -f docker-compose-airflow.yml up --build
    docker-compose -f docker-compose-redash.yml run --rm server create_db
    docker-compose -f docker-compose-redash.yml up --build
    ```
3. Access running applications
    ```JS
    Navigate to `http://localhost:8087/` on the browser to get airflow
    Navigate to `http://localhost:16534/` on the browser to get pgadmin
    Navigate to `http://localhost:11111/` on the browser to get redash

## Usage
### For Development, Please refer the image below to understand the folder structure
![image](https://user-images.githubusercontent.com/44437166/183892133-0f3fa22f-8258-4477-a34b-87b5718455b3.png)

### For Normal Usage, follow the seps below.
- Start by running the "workflow" dag from within the airflow.
- Once all tasks complete executing, you can verify that the data is successfully transfered
  to the warehouse, using either the pgadmin application or redash.
> You can quickly run the queries found in redash_visual.sql to generate a dashboard in redash.

## License
- [MIT License](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwiMqbrwqaz5AhVPiqQKHa5uCtkQFnoECAYQAQ&url=https%3A%2F%2Fopensource.org%2Flicenses%2FMIT&usg=AOvVaw1MsEPekvPKCIceu2jiRDy4)

## Author

👤 **Biniyam Belayneh**

- GitHub: [Biniyam Belayneh](https://github.com/benbel376)
- LinkedIn: [Biniyam Belayneh](https://www.linkedin.com/in/biniyam-belayneh-demisse-42909617a/)
## Acknowledgement
- Thank you [Adludio](https://www.adludio.com/) for this wonderful project.
- Thank you [10 academy]((https://www.10academy.org/)) for preparing us for this kind of challenges.

<!-- CONTRIBUTING -->
## Contributing
Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.
1. Fork the Project
2. Create your Feature Branch
3. Commit your Changes 
4. Push to the Branch 
5. Open a Pull Request

## Show your support

Give a ⭐ if you like this project!


<!-- MARKDOWN LINKS & IMAGES -->
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/biniyam-belayneh-demisse-42909617a//
[contributors-shield]: https://img.shields.io/github/contributors/benbel376/adludio_challenge.svg?style=for-the-badge
[contributors-url]: https://github.com/benbel376/adludio_challenge/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/benbel376/adludio_challenge.svg?style=for-the-badge
[forks-url]: https://img.shields.io/github/forks/benbel376/adludio_challenge?style=for-the-badge
[stars-shield]: https://img.shields.io/github/stars/benbel376/adludio_challenge?style=for-the-badge
[stars-url]: https://github.com/benbel376/adludio_challenge/stargazers
[issues-shield]: https://img.shields.io/github/issues/benbel376/adludio_challenge.svg?style=for-the-badge
[issues-url]: https://img.shields.io/github/issues/benbel376/adludio_challenge?style=for-the-badge
[license-shield]: https://img.shields.io/github/license/benbel376/adludio_challenge?style=for-the-badge
[license-url]: https://github.com/benbel376/adludio_challenge/blob/main/LICENSE
[Postgresql.com]: https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white
[Postgresql-url]: https://www.postgresql.org/
[Airflow.com]: https://img.shields.io/badge/Airflow-017CEE?style=for-the-badge&logo=Apache%20Airflow&logoColor=white
[Airflow-url]: https://airflow.apache.org/
[Docker.com]: https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white
[Docker-url]: https://www.docker.com/
[DBT.com]: https://img.shields.io/badge/DBT-FF694B?style=for-the-badge&logo=dbt&logoColor=white
[DBT-url]: https://docs.getdbt.com/
[Redash.com]: https://img.shields.io/badge/Redash-ef816b?style=for-the-badge&logo=data:image/svg;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPHN2ZyB3aWR0aD0iMzhweCIgaGVpZ2h0PSIzNXB4IiB2aWV3Qm94PSIwIDAgMzggMzUiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayI+CiAgICA8IS0tIEdlbmVyYXRvcjogU2tldGNoIDQ5LjEgKDUxMTQ3KSAtIGh0dHA6Ly93d3cuYm9oZW1pYW5jb2RpbmcuY29tL3NrZXRjaCAtLT4KICAgIDx0aXRsZT5yZWRhc2gtbG9nbzwvdGl0bGU+CiAgICA8ZGVzYz5DcmVhdGVkIHdpdGggU2tldGNoLjwvZGVzYz4KICAgIDxkZWZzPjwvZGVmcz4KICAgIDxnIGlkPSJyZWRhc2gtbG9nbyIgc3Ryb2tlPSJub25lIiBzdHJva2Utd2lkdGg9IjEiIGZpbGw9Im5vbmUiIGZpbGwtcnVsZT0iZXZlbm9kZCI+CiAgICAgICAgPGcgaWQ9Ikdyb3VwLTUiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDYuMDAwMDAwLCAxLjAwMDAwMCkiIGZpbGwtcnVsZT0ibm9uemVybyI+CiAgICAgICAgICAgIDxwYXRoIGQ9Ik0xMiwyNS4zODQ2MTU0IEMyMC43MjYzMzg3LDIwLjIxMTQxNjQgMjQuODI2NTY4NiwxOC4yMjA2MDE0IDI0LjMwMDY4OTcsMTkuNDEyMTcwNCBDMjMuNzc0ODEwOCwyMC42MDM3Mzk0IDE5LjY3NDU4MDksMjUuMTMzMDE2IDEyLDMzIEwxMiwyNS4zODQ2MTU0IFoiIGlkPSJTaGFwZSIgZmlsbD0iI0ZGNzk2NCI+PC9wYXRoPgogICAgICAgICAgICA8cGF0aCBkPSJNMjYsMTMgQzI2LDIwLjE4NjQyMzcgMjAuMTg1MDU4NCwyNiAxMywyNiBDNS44MTQ5NDE1NSwyNiAwLDIwLjE3MjQ0NyAwLDEzIEMwLjAwMDI0MDQ1NTc1Niw1LjgyNzU1Mjk3IDUuODE1MTgyMDEsMCAxMywwIEMyMC4xODQ4MTgsMCAyNiw1LjgyNzU1Mjk3IDI2LDEzIFoiIGlkPSJTaGFwZSIgZmlsbD0iI0ZGNzk2NCI+PC9wYXRoPgogICAgICAgICAgICA8cGF0aCBkPSJNNC44NDA4OTkxLDE0LjcyNjM1MjggTDYuNzYwODg3NzUsMTQuNzI2MzUyOCBDNy4yMjQ2OTkxNCwxNC43Mjc2ODEyIDcuNjAwMzMxMDIsMTUuMDcwNDIxOCA3LjYwMTc4Njg1LDE1LjQ5MzYyMDggTDcuNjAxNzg2ODUsMTcuMjMyNzMyMSBDNy42MDAzMzEwMiwxNy42NTU5MzEgNy4yMjQ2OTkxNCwxNy45OTg2NzE2IDYuNzYwODg3NzUsMTggTDQuODQwODk5MSwxOCBDNC4zNzcwODc3MSwxNy45OTg2NzE2IDQuMDAxNDU1ODMsMTcuNjU1OTMxIDQsMTcuMjMyNzMyMSBMNCwxNS40OTM2MjA4IEM0LjAwMTMyNDIsMTUuMDcwMzcxOSA0LjM3NzAzMjk2LDE0LjcyNzU2MTEgNC44NDA4OTkxLDE0LjcyNjM1MjggWiBNOS4yODM1ODUwNSwxMC44OTAwMTMyIEwxMS4xODk1OTA5LDEwLjg5MDAxMzIgQzExLjY1MzQwMjMsMTAuODkxMzQxNiAxMi4wMjkwMzQxLDExLjIzNDA4MjIgMTIuMDMwNDksMTEuNjU3MjgxMSBMMTIuMDMwNDksMTcuMjMyNzMyMSBDMTIuMDI5MDM0MSwxNy42NTU5MzEgMTEuNjUzNDAyMywxNy45OTg2NzE2IDExLjE4OTU5MDksMTggTDkuMjgzNTg1MDUsMTggQzguODE5NzczNjcsMTcuOTk4NjcxNiA4LjQ0NDE0MTc5LDE3LjY1NTkzMSA4LjQ0MjY4NTk1LDE3LjIzMjczMjEgTDguNDQyNjg1OTUsMTEuNjU3MjgxMSBDOC40NDQwMTAxNiwxMS4yMzQwMzIyIDguODE5NzE4OTEsMTAuODkxMjIxNSA5LjI4MzU4NTA1LDEwLjg5MDAxMzIgWiBNMTMuNzEyMjg4MiwxMyBMMTUuNjMyMjc2OCwxMyBDMTYuMDk2MDg4MiwxMy4wMDEzMjg0IDE2LjQ3MTcyMDEsMTMuMzQ0MDY5IDE2LjQ3MzE3NTksMTMuNzY3MjY3OSBMMTYuNDczMTc1OSwxNy4yMzI3MzIxIEMxNi40NzE3MjAxLDE3LjY1NTkzMSAxNi4wOTYwODgyLDE3Ljk5ODY3MTYgMTUuNjMyMjc2OCwxOCBMMTMuNzEyMjg4MiwxOCBDMTMuMjQ4NDc2OCwxNy45OTg2NzE2IDEyLjg3Mjg0NDksMTcuNjU1OTMxIDEyLjg3MTM4OTEsMTcuMjMyNzMyMSBMMTIuODcxMzg5MSwxMy43NjcyNjc5IEMxMi44NzI3MTMzLDEzLjM0NDAxOSAxMy4yNDg0MjIsMTMuMDAxMjA4MyAxMy43MTIyODgyLDEzIFogTTE4LjI1MzA5NTEsOCBMMjAuMTU5MTAwOSw4IEMyMC42MjI5MTIzLDguMDAxMzI4MzYgMjAuOTk4NTQ0Miw4LjM0NDA2OSAyMSw4Ljc2NzI2NzkzIEwyMSwxNy4yMzI3MzIxIEMyMC45OTg1NDQyLDE3LjY1NTkzMSAyMC42MjI5MTIzLDE3Ljk5ODY3MTYgMjAuMTU5MTAwOSwxOCBMMTguMjUzMDk1MSwxOCBDMTcuNzg5MjgzNywxNy45OTg2NzE2IDE3LjQxMzY1MTgsMTcuNjU1OTMxIDE3LjQxMjE5NiwxNy4yMzI3MzIxIEwxNy40MTIxOTYsOC43NjcyNjc5MyBDMTcuNDEzNTIwMiw4LjM0NDAxOTA0IDE3Ljc4OTIyODksOC4wMDEyMDgyNSAxOC4yNTMwOTUxLDggWiIgaWQ9IlNoYXBlIiBmaWxsPSIjRkZGRkZGIj48L3BhdGg+CiAgICAgICAgPC9nPgogICAgPC9nPgo8L3N2Zz4=&logoColor=white
[Redash-url]: https://redash.io/