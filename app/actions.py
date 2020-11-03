import asyncio
from collections import ChainMap

import aiohttp

from app.helpers import make_base_url, make_url_with_query
from app.typing import T_URL, T_REQUEST_RESULT, T_DOMAIN, T_QUERIES, T_RESULTS_FOR_DOMAIN, T_DOMAINS, \
    T_RESULTS_FOR_DOMAINS
from config.config import DEBUG
from config.logging import logger


async def action_per_url(session: aiohttp.ClientSession, url: T_URL) -> T_REQUEST_RESULT:
    logger.debug('action_per_url.start', url=url, )

    if DEBUG:
        logger.debug('action_per_url.end', url=url, )
        return url

    # For send params as dict, see link
    #   https://docs.aiohttp.org/en/v3.0.1/client_quickstart.html#passing-parameters-in-urls
    async with session.get(url=url) as response:
        # Delete this if don't need
        # return await response.text()

        result = response.status
        logger.debug('action_per_url.end', url=url, result=result)
        return result


async def action_per_domain(session: aiohttp.ClientSession, domain: T_DOMAIN,
                            queries: T_QUERIES) -> T_RESULTS_FOR_DOMAIN:
    logger.debug('action_per_domain.start', domain=domain, )

    base_url = make_base_url(domain=domain)

    urls_with_queries = [make_url_with_query(base_url=base_url, query=query) for query in queries]

    request_results = await asyncio.gather(
        *[
            action_per_url(session=session, url=url) for url in urls_with_queries
        ],
        return_exceptions=True,
    )

    logger.debug('action_per_domain.end', domain=domain, )
    return {domain: request_results}


async def make_actions(domains: T_DOMAINS, queries: T_QUERIES) -> T_RESULTS_FOR_DOMAINS:
    async with aiohttp.ClientSession() as session:
        results_for_domains = await asyncio.gather(
            *[
                action_per_domain(session=session, domain=domain, queries=queries) for domain in domains
            ],
            return_exceptions=True,
        )
    return dict(ChainMap(*results_for_domains))
