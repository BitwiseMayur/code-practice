# Project: Right or Left

## Project Idea
The goal of "Right or Left" is to determine if a news article leans towards the right or left politically.

We often know the political leanings of news based on the publisher. This project's idea is to scrape news articles, analyze the words, and then give a lean rating.

## Observations and Challenges
Starting this project, I learned that many news publishers restrict web scraping to protect their revenue. The "Read More" button, now common on sites, limits the information scrapers can access.

I used the Python module `newspaper3k` but could only fetch headlines due to sites' restrictions on content.

### Understanding `robots.txt`
An important aspect is the `robots.txt` file, which tells web crawlers which URLs can or cannot be scraped. For example, checking `www.thequint.com/robots.txt` gives insights into allowed and disallowed paths.

## Conclusion
Throughout this project, I observed ChatGPT's ability to interpret webpages and provide insights, the specifics of its operational mechanisms remain largely behind the scenes. 
For now not proceeding with this project

