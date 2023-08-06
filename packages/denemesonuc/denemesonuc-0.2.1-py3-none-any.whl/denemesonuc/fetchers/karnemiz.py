"""Fetcher module for the `bes.karnemiz.com` (old) type frontend."""

from selenium.webdriver.remote.webdriver import WebDriver

from denemesonuc.models import Denek


def fetch(
    driver: WebDriver,
    denek: Denek,
    deneme_url: str,
    deneme_name: str,
    deneme_lesson_names: dict[str, dict] = {},
    **fetch_options,
) -> None:
    """Fetch the report of the given denek.

    This function implements the logic of fetching the report of the \
        given denek from the remote web server that uses the `bes.karnemiz.com` (old) \
        type frontend.
    
    Args:
        driver: \
            The selenium driver object that will be used to fetch the \
            deneme results.
        denek: The denek that will be fetched.
        deneme_url: The url of the remote web server that \
            contains the deneme results.
        deneme_name: The name of the deneme.
        deneme_lesson_names: The names of the lessons that are in the \
            deneme. The keys are the short names of the lessons and the \
            values are dicts that contain the names of the lessons and the \
            number of questions in the lessons. Total lessons are fetched \
            in a different way, so they don't need to be included in this \
            dict.
        **fetch_options: The options that are used to fetch the \
            deneme results.
    
    Raises:
        ...
    """
    from selenium.common.exceptions import NoSuchElementException, TimeoutException
    from selenium.webdriver.remote.webelement import WebElement
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.select import Select
    from selenium.webdriver.support.wait import WebDriverWait

    from denemesonuc.models import (
        DenekDidntTakeDeneme,
        DenekProbablyDidntTakeDeneme,
        LessonBasedResult,
        LessonResultContainer,
        Ranking,
        Report,
    )
    from denemesonuc.utils import uppercase_tr

    if logout := fetch_options.get("deneme_logout_url"):
        driver.get(logout)

    driver.get(deneme_url)

    # at login page

    # grade
    Select(driver.find_element("id", "seviye")).select_by_visible_text(denek.grade)

    # province
    Select(driver.find_element("id", "ilkodu")).select_by_visible_text(
        uppercase_tr(denek.province)
    )

    # school
    driver.find_element("id", "kurumarama").send_keys(denek.school)
    WebDriverWait(driver, 3).until(EC.presence_of_element_located(("id", "ui-id-2")))
    driver.find_element("id", "ui-id-2").click()

    # number
    driver.find_element("id", "ogrencino").send_keys(denek.number)

    # name
    driver.find_element("id", "isim").send_keys(denek.name)

    # submit
    driver.find_element("name", "bulbtn1").submit()

    # at report page
    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                (
                    "xpath",
                    "/html/body/div[1]/section/div/div/div[1]",
                )  # base xpath for deneme selection
            )
        )
    except TimeoutException as e:
        raise DenekProbablyDidntTakeDeneme(
            f"Denek probably did not take any denemes from {deneme_url}"
        ) from e

    # select correct deneme
    deneme_selector = Select(driver.find_element("id", "digersinavlarcombo"))

    try:
        deneme_selector.select_by_visible_text(deneme_name)
    except NoSuchElementException as e:
        raise DenekDidntTakeDeneme(
            f"Denek did not take the deneme {deneme_name} from {deneme_url}"
        ) from e

    WebDriverWait(driver, 5).until(
        EC.text_to_be_present_in_element(
            ("xpath", "/html/body/div[1]/section/div/div/div[4]/div/div"), deneme_name
        )
    )

    root = driver.find_element("xpath", "/html/body/div[1]/section/div/div")

    rank_root1 = root.find_element("xpath", "./div[5]/div/div[3]/div")
    rank_root2 = root.find_element("xpath", "./div[5]/div/div[5]/div")

    ranks = []
    for i in range(2, 7):
        ranks.append(int(rank_root1.find_element("xpath", f"./div[{i}]").text))
    for i in range(2, 7):
        ranks.append(int(rank_root2.find_element("xpath", f"./div[{i}]").text))

    ranking = Ranking(
        *ranks,
    )

    class_ = root.find_element("xpath", "./div[1]/div[2]/div[3]").text.replace(
        "-", ""
    )  # "-9A", "11A"

    score = float(
        root.find_element("xpath", "./div[5]/div/div[1]/div/div")
        .text.replace(",", ".")
        .split(" ")[-1]
    )  # "score: 123,456"

    result_data = {}

    def to_lesson_result(elem: WebElement) -> LessonBasedResult:
        """Convert the given element to a lesson based result.

        Args:
            elem: The element that will be converted.

        Returns:
            The converted element.
        """
        name = elem.find_element("xpath", "./div[1]/div").text
        count = int(elem.find_element("xpath", "./div[2]/div[2]/div[1]").text)
        true = int(elem.find_element("xpath", "./div[2]/div[2]/div[2]").text)
        false = int(elem.find_element("xpath", "./div[2]/div[2]/div[3]").text)
        empty = count - true - false
        net = float(
            elem.find_element("xpath", "./div[2]/div[2]/div[4]").text.replace(",", ".")
        )
        return LessonBasedResult(
            full_name=name,
            question_count=count,
            true=true,
            false=false,
            empty=empty,
            net=net,
        )

    for i in root.find_elements("xpath", "./div[7]/div/div[*]/div[1]"):
        if i.find_element("xpath", "./div[2]/div[2]/div[1]").text:
            r = to_lesson_result(i)
            result_data[r.full_name] = r

    response = {}
    for export, (d) in deneme_lesson_names.items():
        name = d["name"]
        count = d["question_count"]
        result = result_data.get(name, LessonBasedResult.create_empty(count, name))
        response[export] = result

    total = to_lesson_result(root.find_element("xpath", "./div[6]/div/div/div[1]"))

    result = LessonResultContainer(
        response,
    )

    denek.add_report(
        Report(
            score=score,
            denek_class=class_,
            ranking=ranking,
            result=total,
            lessons=result,
            deneme_name=deneme_name,
        )
    )
