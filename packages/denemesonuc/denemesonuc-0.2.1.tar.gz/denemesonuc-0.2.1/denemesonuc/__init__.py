"""Denemesonuc: A package for `orbim ölçme değerlendirme` thing.

This package contains tools for fetching and processing deneme results from \
    remote web servers which their frontend is based on `orbim ölçme \
    değerlendirme` thing.
"""
__version__ = "0.2.1"

from selenium.webdriver.remote.webdriver import WebDriver as __WebDriver

from denemesonuc.models import Denek as __Denek


def fetch_deneme(
    driver: __WebDriver,
    denek: __Denek,
    deneme_url: str,
    deneme_name: str,
    deneme_type: str,
    deneme_lesson_names: dict[str, dict] = {},
    **fetch_options,
) -> None:
    """Fetch the report of the given denek.

    This function is a wrapper function that calls the correct fetcher \
        function according to the given deneme type.
    
    Args:
        driver: \
            The selenium driver object that will be used to fetch the \
            deneme results.
        denek: The denek that will be fetched.
        deneme_url: The url of the remote web server that \
            contains the deneme results.
        deneme_name: The name of the deneme.
        deneme_type: The type of the deneme. This is used to determine \
            which fetcher function will be called.
        deneme_lesson_names: The names of the lessons that are in the \
            deneme. The keys are the short names of the lessons and the \
            values are dicts that contain the names of the lessons and the \
            number of questions in the lessons. Total lessons may need to be \
            included in this dict for some fetchers.
        **fetch_options: The options that are used to fetch the \
            deneme results.
    
    Raises:
        ValueError: If the given deneme type is not supported.
    """
    if deneme_type == "old":
        from denemesonuc.fetchers.karnemiz import fetch

        fetch(
            driver,
            denek,
            deneme_url,
            deneme_name,
            deneme_lesson_names,
            **fetch_options,
        )
    elif deneme_type == "new":
        from denemesonuc.fetchers.okulizyon import fetch

        fetch(
            driver,
            denek,
            deneme_url,
            deneme_name,
            deneme_lesson_names,
            **fetch_options,
        )
    else:
        raise ValueError(f"Unsupported deneme type: {deneme_type}")
