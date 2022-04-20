# NLP Cource Project 2

# Project Structure

This project consists of the following parts:

- Web Crawling
- Text Preprocessing
- Important Chunks Extraction
- Text Classification

********************************
For data, articles on various topics (such as:
[Money](https://www.forbes.com/money/),
[Leadership](https://www.forbes.com/leadership/),
[Worlds-Billionaires](https://www.forbes.com/worlds-billionaires/),
[Business](https://www.forbes.com/business/),
[Small Business](https://www.forbes.com/small-business/),
[Life Style](https://www.forbes.com/lifestyle/),
[Real State](https://www.forbes.com/real-estate/) and etc
)
are extracted from the pages of
[Forbes](www.forbes.com) website.

> [Forbes](https://en.wikipedia.org/wiki/Forbes) is an American business magazine owned by Integrated Whale Media Investments and the Forbes family. Published eight times a year, it features articles on finance, industry, investing, and marketing topics. Forbes also reports on related subjects such as technology, communications, science, politics, and law.

**Scrapy** library in python was used to extract articles. The information extracted corresponding to each
article is as follows:

| Attribute                 | Description                                   | Type         |
| ------------------------- | --------------------------------------------- | ------------ |
| context_header            | category (context) of article                 | String       |
| corpus_date_ymd           | date of article publication (y/m/d)           | String       |
| corpus_date_hm            | date of release (h/m)                         | String       |
| corpus_title              | title of article                              | String       |
| corpus_content_paragraphs | paragraphs of article content                 | List(String) |
| author_var_dict           | profile of article author (described bellow.) | Dictionary   |

So that <code>author_var_dict</code> attribute contains the following fields:

| Attribute                | Description                      | Type         |
| ------------------------ | -------------------------------- | ------------ |
| author_forbes_url        | forbes url of article author     | String       |
| author_name              | article author name              | String       |
| author_contrib_type      | article author contributer type  | String       |
| author_subcontext_header | author field                     | String       |
| author_about             | a paragraph about article author | String       |
| author_social_links      | article author social links      | List(String) |
