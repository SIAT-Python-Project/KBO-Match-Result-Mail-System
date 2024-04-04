# KBO-Match-Result-Mail-System :yellow_heart:

<!-- PROJECT LOGO -->
<br />
<div align="center">

<h3 align="center">KBO-Match-Result-Mail-System</h3>

  <p align="center">
    야구 경기 결과를 매일 찾아보기 힘드셨죠? 메일 아침 8시에 메일로 보내드립니다!!
    <br />
    
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#languages-libraries-and-tools-used">Languages, libraries and tools used</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
    </li>
    <li><a href="#feature">Feature</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#coming-soon">Coming Soon</a></li>
    <li><a href="#bug">Bug</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
네이버, KBO 사이트 등 여러 사이트에서 한국 야구 1부 리그의 경기 결과를 찾아볼 수 있다. 하지만 이러한 방법의 문제점들은 내가 원하는 정보, 원하는 팀의 경기 결과 및 뉴스를 찾는 과정에서 많은 비용이 소모가 되는 것이다. 그래서 이 프로젝트에서 이러한 단점을 해결하고자 한다.<br/>

이 프로젝트는 매일 아침 08시에 [KBO](https://www.koreabaseball.com/) 및 [스포키](https://sporki.com/) 사이트에서 필요한 데이터들을 크롤링하여 HTML문서로 변환하여 메일로 보내준다.


<p align="right">(<a href="#kbo-match-result-mail-system-yellow_heart">back to top</a>)</p>



### Languages, libraries and tools used
#### Languages
* Python3
  - version: 3.11.8
  
#### libraries
* selenium
  - version: 4.19.0
  - used: Data Crawling
* pandas
  - version: 2.2.1 
  - used: Excel File ConversionE
* requests
  - vsrsion: 2.31.0
  - used:Get HTML Resource
* bs4
  - version: 0.0.2
  - used: Data Scraping
* schedule
  - version: 1.2.1
  - used: Mail Schedule

<p align="right">(<a href="#kbo-match-result-mail-system-yellow_heart">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started
1.  Clone the repo
   ```sh
   git clone https://github.com/SIAT-Python-Project/KBO-Match-Result-Mail-System.git
   ```
2. Install libraries
  ```sh
pip install selenium
pip install pandas
pip install requests
pip install bs4
pip install schedule
  ```
3. Run main.py
  ```sh
python ./src/main.py
  ```
<!-- USAGE EXAMPLES -->
<!--Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources. -->


<p align="right">(<a href="#kbo-match-result-mail-system-yellow_heart">back to top</a>)</p>

<!-- FEATURE EXAMPLES -->
## Feature
  1. Input setting-info
  2. Crawling KBO-data
  3. Converting crawled data to HTML
  4. Sending HTML file to mail


<p align="right">(<a href="#kbo-match-result-mail-system-yellow_heart">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap
- [x] Crawling recent match result
- [x] Crawling next match info
- [x] Crawling recent match scoreBox
- [x] Crawling recent match news
- [x] Crawling team ranking
- [x] Crawling pitcher / hitter ranking
- [x] Converting crawled data to HTML
- [x] Sending mail

See the [project issues](https://github.com/SIAT-Python-Project/KBO-Match-Result-Mail-System/issues) for a full list of proposed features(and known issues).

<p align="right">(<a href="#kbo-match-result-mail-system-yellow_heart">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#kbo-match-result-mail-system-yellow_heart">back to top</a>)</p>

<!-- COMING SOON -->

## Coming Soon
- [ ] Saving match info by date
- [ ] Saving team / player rank
- [ ] Changing input environment GUI from Terminal
- [ ] Searching player inho

<p align="right">(<a href="#kbo-match-result-mail-system-yellow_heart">back to top</a>)</p>

## Bug
Sometimes, error occur during crawling. If so, please restart the server. <br/>
We are currently trying to resolve this error.<br/>
Sorry....

<p align="right">(<a href="#kbo-match-result-mail-system-yellow_heart">back to top</a>)</p>

<!-- CONTACT -->
## Contact
hg_yellow
- GitHub: [hg_yellow](https://github.com/jang010505)
- Mail: hgyellow0505@gmail.com

배창민
- GitHub: [Changchang](https://github.com/bbmini96)
- Mail: changmin38@gmail.com

조성민
- GitHub: [Seong Min Cho](https://github.com/EnjoyTime18)
- Mail: ggbb2956@gmail.com


Project Link: [KBO-Match-Result-Mail-System](https://github.com/SIAT-Python-Project/KBO-Match-Result-Mail-System)<br/>
Project Team Link: [SIAT-Python-Project](https://github.com/SIAT-Python-Project)
<p align="right">(<a href="#kbo-match-result-mail-system-yellow_heart">back to top</a>)</p>
