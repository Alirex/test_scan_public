import structlog

structlog.configure(
    
    cache_logger_on_first_use=True,
)

logger = structlog.getLogger()
