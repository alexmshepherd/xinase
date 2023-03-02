# owdex
**_open web index_**

![License](https://img.shields.io/github/license/alexmshepherd/owdex?style=flat-square&color=blue)
![Vulnerability Checks](https://img.shields.io/github/actions/workflow/status/alexmshepherd/owdex/codeql.yml?label=vulnerability%20checks&style=flat-square)
![Trans Rights](https://img.shields.io/badge/trans-rights-ff69b4?style=flat-square)

Owdex is an open index of pages from across the web. Instead of crawling through hypertext based
on links, it only indexes pages that its users direct it to. Owdex aims to build a better 
alternative to web search by cutting through the cruft of junk results and bringing focus to real
information.

> **Warning**  
> Owdex is not even working, let alone production-ready. It is not presently usable to fulfill its 
> intended purpose. For that reason, it's not advisable to use it in a production environment. 
> However, I'm making a hard push towards an alpha release soon, which should be ready Eventually 
> (TM). 

## Requirements
_because nobody can spell Prerequisittes_

### For production install
- Docker
- that's it

### For development
- Python 3
    - Flask
    - waitress
- Tailwind CSS
- Apache Solr

## Installation
Start by `git clone`ing the repo to an arbitrary location. Then run `chmod +x setup.sh; sudo ./setup.sh`. 
This creates a `data` directory for Solr to use, fills it with the subdirectories it needs, and 
sets permissions appropriately (this last step is why it has to be run with `sudo`.) 

## Usage
Production users can run `docker-compose up`. This will run the Solr backend and Flask frontend, 
get them talking to each other, and serve a website on port 80. 

Developers should ~~sacrifice their souls to the god of Solr~~ install the dependencies, make sure 
the `src/static/tailwind.css` file is up to date with `tailwindcss -o src/static/tailwind.css -c src/tailwind.config.js`, 
and then can serve the site with `flask --app src/app.py run --debug`. 

## Contribution
First of all, thank you for getting this far! It means a lot to me that you're interested in this 
project and willing to help out. Given that not enough work has been done yet for the project to 
gain momentum in what I feel is the right direction, development of Owdex's core functionality will
probably be done by me for now, until the essentials are complete. However, the Issues tab may list
a number of smaller changes that should be made eventually but are neither critical nor part of the
system's core abilities. If you feel like taking one of them on, I'd love to work with you. 

## Acknowledgement
Thanks to [@4censord](https://github.com/4censord) for exceptional help, suppport and words of advice.

## License 
Owdex is licensed under the [GNU AGPL v3](https://github.com/alexmshepherd/owdex/blob/main/LICENSE).
