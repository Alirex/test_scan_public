from config.config import PATH_TO_QUERIES, PATH_TO_DOMAINS
from app.typing import T_QUERIES, T_DOMAINS, T_DOMAIN, T_BASE_URL, T_QUERY, T_URL


def get_queries() -> T_QUERIES:
    return sorted(list(set(PATH_TO_QUERIES.read_text().splitlines())))


def get_domains() -> T_DOMAINS:
    """
        Get unique domains
    """
    return sorted(list(set(PATH_TO_DOMAINS.read_text().splitlines())))


def make_base_url(domain: T_DOMAIN, scheme: str = 'http') -> T_BASE_URL:
    return f'{scheme}://{domain}'


def make_url_with_query(base_url: T_BASE_URL, query: T_QUERY) -> T_URL:
    return f'{base_url}{query}'
