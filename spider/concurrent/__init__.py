# _*_ coding: utf-8 _*_

"""
define ThreadPool as WebSpider, AsyncPool as WebSpiderAsync
"""

from .concur_threads import ThreadPool as WebSpider
from .concur_async import AsyncPool as WebSpiderAsync
