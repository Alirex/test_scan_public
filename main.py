import asyncio

from app.actions import make_actions
from app.helpers import get_queries, get_domains
from app.report import make_report
from config.logging import logger


async def main():
    queries = get_queries()
    logger.info('queries', queries=queries)

    domains = get_domains()
    logger.info('domains', domains=domains, )

    results_for_domains = await make_actions(domains=domains, queries=queries)
    logger.info('results_for_domains', results_for_domains=results_for_domains)

    path_to_report = await make_report(results_for_domains=results_for_domains, queries=queries)
    logger.info('path_to_report', path_to_report=path_to_report, )


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
