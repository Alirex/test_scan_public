import pathlib

PATH_TO_ROOT = pathlib.Path(__file__).parent.parent
PATH_TO_INPUT = PATH_TO_ROOT.joinpath('input')

PATH_TO_DOMAINS = PATH_TO_INPUT.joinpath('domains.txt')
PATH_TO_QUERIES = PATH_TO_INPUT.joinpath('queries.txt')

PATH_TO_OUTPUT = PATH_TO_ROOT.joinpath('output')
PATH_TO_REPORT = PATH_TO_OUTPUT.joinpath('report')
PATH_TO_REPORT_JSON = PATH_TO_REPORT.with_suffix('.json')

DEBUG = True
# DEBUG = False
