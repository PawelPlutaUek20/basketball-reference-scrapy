# -*- coding: utf-8 -*-
import scrapy
from .table import Table

class ToScrapeSpider(scrapy.Spider):
    name = 'toscrape'
    start_urls = [
        'https://www.basketball-reference.com/leagues/NBA_2018.html',
        'https://www.basketball-reference.com/leagues/NBA_2019.html',
        'https://www.basketball-reference.com/leagues/NBA_2020.html',
        'https://www.basketball-reference.com/leagues/NBA_2021.html',
        'https://www.basketball-reference.com/leagues/NBA_2022.html',
    ]

    def parse(self, response):
        eastern_conference_table = Table(response.xpath('(//table)[1]'))
        western_conference_table = Table(response.xpath('(//table)[2]'))
        # yield all rows
        yield from eastern_conference_table.as_dicts()
        yield from western_conference_table.as_dicts()