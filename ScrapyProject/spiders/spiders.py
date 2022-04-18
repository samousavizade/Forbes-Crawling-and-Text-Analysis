import scrapy
from scrapy import Selector, Spider
from ScrapyProject.items import StackItem, QuoteItem
from scrapy.http import TextResponse
import re
from itertools import chain


class ForbesSpider(Spider):
    name = "forbes"

    def start_requests(self):
        urls = [
            "https://www.forbes.com/money/",
            "https://www.forbes.com/leadership/",
            "https://www.forbes.com/worlds-billionaires/",
            "https://www.forbes.com/business/",
            "https://www.forbes.com/small-business/",
            "https://www.forbes.com/lifestyle/",
            "https://www.forbes.com/real-estate/",
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response: TextResponse, **kwargs):

        context_header = response.css("h1.chansec-header div.fs-content::text").get()

        pattern = "https://www.forbes.com/sites/\w*/\d{4}/\d{2}/\d{2}/.*"

        total_links = set()

        links = response.css("div.card a::attr(href)").getall()
        links = set(filter(lambda link: re.search(pattern, link), links))
        total_links = total_links.union(links)

        links = response.css("article.stream-item a.stream-item__title::attr(href)").getall()
        links = set(filter(lambda link: re.search(pattern, link), links))
        total_links = total_links.union(links)

        for link in total_links:
            result = response.meta.get("result", dict())
            result['context_header'] = context_header
            yield response.follow(link, self.parse_corpus, meta={'result': result})

    def parse_corpus(self, response: TextResponse, **kwargs):

        result = response.meta['result']

        result['corpus_date_ymd'] = response.css("div.header-content-container div.content-data time::text").get()
        result['corpus_date_hm'] = response.css("div.header-content-container div.content-data span.time time::text").get()
        result['corpus_title'] = response.css("div.article-headline-container h1.fs-headline ::text").get()

        author_elems = response.css("div.top-contrib-block div.contribs")
        for author_elem in author_elems:
            author_link = author_elem.css("div.contrib-container a.fs-author-avatar::attr(href)").get()
            yield response.follow(author_link, self.parse_author, meta={'result': result})

        corpus_content_parts = response.css("div.article-body > p ::text,  div.article-body div > p ::text, div.article-body > p > a ::text, div.article-body > ol > li *::text, div.article-body ul > li *::text, div.article-body > h1 ::text, div.article-body > h2 ::text, div.article-body > h3 ::text, div.article-body > h4 ::text, div.article-body > h5 ::text").getall()
        result['corpus_content_parts'] = corpus_content_parts

        yield result

    def parse_author(self, response: TextResponse, **kwargs):
        result = response.meta['result']

        author_forbes_url = response.request.url
        author_name = response.css("h1.contributor-details__name span::text").get()

        author_contrib_type = response.css("div.contributor-details__type span::text").get()
        author_subcontext_header = response.css("a.contributor-details__display-channel::text").get()

        author_about_paragraphs = response.css("div.contributor-about__full-description p::text").getall()
        author_about = " ".join(author_about_paragraphs)

        author_social_links = response.css("div.contributor-social a::attr(href)").getall()

        variables_dict = {
            'author_forbes_url': author_forbes_url,
            'author_name': author_name,
            'author_contrib_type': author_contrib_type,
            'author_subcontext_header': author_subcontext_header,
            'author_about': author_about,
            'author_social_links': author_social_links
        }

        result['author_var_dict'] = variables_dict

        yield result
