import logging
from colorama import init, Fore

init()

logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()

formatter = logging.Formatter(
    f'{Fore.BLUE}[%(appname)s] {Fore.RESET}%(levelname)s: %(message)s'
)

console_handler.setFormatter(formatter)

logger.addHandler(console_handler)


def log_info(message, appname="MyApp"):
    """Log an info-level message."""
    logger.info(format_log_message(message), extra={"appname": appname})


def log_warning(message, appname="MyApp"):
    """Log a warning-level message."""
    logger.warning(format_log_message(message), extra={"appname": appname})


def log_error(message, appname="MyApp"):
    """Log an error-level message."""
    logger.error(format_log_message(message), extra={"appname": appname})


def format_log_message(message):
    """Format the log message."""
    if isinstance(message, (dict, list)):
        return format_complex_type(message)
    return str(message)


def format_complex_type(data):
    """Format dictionaries and arrays."""
    if isinstance(data, dict):
        return format_dict(data)
    elif isinstance(data, list):
        return format_list(data)


def format_dict(data):
    """Format a dictionary."""
    formatted_dict = "{"
    for key, value in data.items():
        formatted_dict += f"{key}: {format_log_message(value)}, "
    formatted_dict = formatted_dict.rstrip(", ")
    formatted_dict += "}"
    return formatted_dict


def format_list(data):
    """Format a list."""
    formatted_list = "["
    for item in data:
        formatted_list += f"{format_log_message(item)}, "
    formatted_list = formatted_list.rstrip(", ")
    formatted_list += "]"
    return formatted_list
