<div id="top"></div>



<br />
<div align="center">
  <a href="https://github.com/transientCloud/gdpr-sota/tree/main/pygdpr">
    <img src="images/logo.png" alt="Logo" width="90" height="90">
  </a>

  <h3 align="center">GDPRxiv Crawler (README)</h3>

  <p align="center">
    An efficient tool to crawl GDPR legal documents!
    
  </p>
</div>


## About The Project

With the introduction of the Europeans Union's General Data Protection Regulation (GDPR), there has been an explosion in the number of legal 
documents pertaining to case reviews, analyses, legal decisions, etc... that mark the enforcement of the GDPR.
Additionally, these documents are spread across over 30 Data Protection (DPA) and Supervisory Authorities. As a result, it is 
cumbersome for researchers/legal teams to access and download a large quantity of GDPR documents at once.

To address this, we have created GDPRxiv Crawler, a command-line tool that allows users to efficiently filter and
download GDPR documents. Users may select their desired DPA and document_type, and GDPRxiv Crawler will scrape the web
and download all up-to-date documents. 

Of course, it is impossible to entirely keep up with DPA website redesigns and newly added document categories. 
However, we hope that this tool will eliminate the bulk of the workload and allow users to focus on more important tasks.



### Built With

* [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [Selenium](https://www.selenium.dev/)
* [Add more later...](https://www.example.com)



## Getting Started

### Prerequisites

Python 3.9 is required. This python version includes the pip installer and the venv module, which is needed to create a 
virtual environment.

It is strongly recommended that users utilize a virtual environment when installing this package. 
See below to create and activate one.

_In a directory:_
1. venv:

    ```sh
    virtualenv <virtual env name>
     ```
  
2. Activate the virtual environment:

    ```sh
    source <virtual env name>/bin/activate
    ```

### Installation
_At any moment, use command 'pip3 list' to view all installed packages._

1. Download [requirements.txt](https://github.com/transientCloud/gdpr-sota/blob/main/pygdpr/requirements.txt)
    and place it in the directory that contains the virtual environment.
2. Install package requirements
   ```sh
   pip3 install -r requirements.txt
   ```
3. Install the GDPRxiv Crawler package
   ```sh
   pip3 install -i https://test.pypi.org/simple/ gdprCrawlerTest15
   ```



## Usage
Downloaded documents will be organized into a set of folders based on DPA and document type.

A file called visitedDocs.txt is always created upon an initial run within a new directory. This file records each downloaded document's
unique hash, which allows the tool to avoid overwriting existing documents (if desired) in future runs. 

* Scrape desired documents:
   ```sh
   gdprCrawler scrape --country <country name> --document_type <document type> --path <directory to store documents>
   ```
    _The same directory can be used for multiple countries: the scraper automatically organizes documents based on country and document type._

* Optionally, the --overwrite argument can be included if users would like to overwrite existing documents:

   ```sh
      gdprCrawler scrape --country <country name> --document_type <document type> --path <directory to store documents> --overwrite <True/False>
   ```
    _Overwrite is False by default._

&nbsp; 

**Country and document type arguments should be written exactly as they appear below:**

<pre>
SUPPORTED COUNTRIES:     DOCUMENTS TYPES:

        Austria                  Decisions
        Belgium                  Annual Reports, Decisions, Opinions
        Bulgaria                 Annual Reports, Opinions
        Croatia                  Decisions
        Cyprus                   Annual Reports, Decisions
        Czech Republic           Annual Reports, Completed Inspections, Court Rulings, Decisions, Opinions, Press Releases
        Denmark                  Annual Reports, Decisions, Permissions
        EDPB (Agency)            Annual Reports, Decisions, Guidelines, Letters, Opinions, Recommendations
        Estonia                  Annual Reports, Instructions, Prescriptions
        Finland                  Advice, Decisions, Guides, Notices
        France                   FUTURE UPDATE
        Germany                  N/A
        Greece                   Annual Reports, Decisions, Guidelines, Opinions, Recommendations
        Hungary                  Annual Reports, Decisions, Notices, Recommendations, Resolutions
        Ireland                  Decisions, Judgements, News
        Italy                    Annual Reports, Hearings, Injunctions, Interviews, Newsletters, Publications
        Latvia                   Annual Reports, Decisions, Guidances, Opinions, Violations
        Lithuania                Decisions, Guidelines, Inspection Reports
        Luxembourg               Annual Reports, Opinions
        Malta                    Guidelines, News Articles
        Netherlands              Decisions, Opinions, Public Disclosures, Reports
        Poland                   Decisions, Tutorials
        Portugal                 Decisions, Guidelines, Reports
        Romania                  Decisions, Reports
        Slovakia                 Fines, Opinions, Reports
        Slovenia                 Blogs, Guidelines, Infographics, Opinions, Reports
        Spain                    Blogs, Decisions, Guides, Infographics, Reports
        Sweden                   Decisions, Guidances, Judgements, Publications
        United Kingdom           Decisions, Judgements, Notices
</pre>



## Contributing

All suggestions and contributions you make are **greatly appreciated**.



## License

Distributed under the MIT License. See `LICENSE.txt` for more information.




## Contact

<!--- Put Research Group Info here - email@example.com --->

Project Link: [https://github.com/GDPRxiv/crawler](https://github.com/GDPRxiv/crawler)




## Acknowledgments

Thank you to everyone who has supported the project in any way. We greatly appreciate your time and effort!

* [Choose an Open Source License](https://choosealicense.com)
* [Img Shields](https://shields.io)



<p align="right">(<a href="#top">back to top</a>)</p>




