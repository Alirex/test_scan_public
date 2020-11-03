import json

from app.typing import T_RESULTS_FOR_DOMAINS, T_QUERIES, T_PATH_TO_REPORT
from config.config import PATH_TO_REPORT_JSON


async def make_report(results_for_domains: T_RESULTS_FOR_DOMAINS, queries: T_QUERIES) -> T_PATH_TO_REPORT:
    # [make_report_structure]-[BEGIN]
    report = {
        'queries': queries,
        'results': results_for_domains,
    }
    # [make_report_structure]-[END]

    # [ensure_directory]-[BEGIN]
    if not PATH_TO_REPORT_JSON.parent.exists():
        PATH_TO_REPORT_JSON.parent.mkdir(parents=True)
    # [ensure_directory]-[END]

    # [save_to_file]-[BEGIN]
    report_as_plain_json = json.dumps(report, indent=2)
    PATH_TO_REPORT_JSON.write_text(report_as_plain_json)
    # [save_to_file]-[END]

    return PATH_TO_REPORT_JSON
