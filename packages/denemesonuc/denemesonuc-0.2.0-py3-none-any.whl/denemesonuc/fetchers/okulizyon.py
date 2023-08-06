"""Fetcher module for the `okulizyon` (new) type frontend."""

from selenium.webdriver.remote.webdriver import WebDriver

from denemesonuc.models import Denek


def fetch(
    driver: WebDriver,
    denek: Denek,
    deneme_url: str,
    deneme_name: str,
    deneme_lesson_names: dict[str, dict] = {},
    deneme_logout_url: str = "",
    **fetch_options,
) -> None:
    """Fetch the report of the given denek.

    This function implements the logic of fetching the report of the \
        given denek from the remote web server that uses the `okulizyon` (new) \
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
            number of questions in the lessons. If the lesson is a total \
            lesson, the dict must contain a `total` key that is set to \
            `True`.
        deneme_logout_url: The url of the logout page of the remote web \
            server.
        **fetch_options: The options that are used to fetch the \
            deneme results.

    Raises:
        DenekProbablyDidntTakeExam: If the given denek probably didn't take \
            the exam.
        DenekNotFound: If the given denek is not found.
    """
    from selenium.common.exceptions import NoSuchElementException, TimeoutException
    from selenium.webdriver.support import expected_conditions as EC
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

    if deneme_logout_url:
        driver.get(deneme_logout_url)

    driver.get(deneme_url)

    # at login page

    # grade
    driver.find_element("id", "select2-gt_ogrencino_sinifcombo-container").click()

    grade_selector = driver.find_element(
        "id", "select2-gt_ogrencino_sinifcombo-results"
    )
    grade_selector.find_element("xpath", f"//li[text()='{denek.grade}']").click()

    # province
    driver.find_element("id", "select2-gt_ogrencino_ilcombo-container").click()
    province_selector = driver.find_element(
        "id", "select2-gt_ogrencino_ilcombo-results"
    )
    province_selector.find_element(
        "xpath", f"//li[text()='{uppercase_tr(denek.province)}']"
    ).click()

    # district
    driver.find_element("id", "select2-gt_ogrencino_ilcecombo-container").click()
    district_selector = driver.find_element(
        "id", "select2-gt_ogrencino_ilcecombo-results"
    )
    district_selector.find_element(
        "xpath", f"//li[text()='{uppercase_tr(denek.district)}']"
    ).click()

    # school
    driver.find_element("id", "select2-gt_ogrencino_kurumcombo-container").click()
    school_selector = driver.find_element(
        "id", "select2-gt_ogrencino_kurumcombo-results"
    )
    school_selector.find_element("xpath", f"//li[text()='{denek.school}']").click()

    # number
    driver.find_element("id", "gt_ogrencino_ogrnoedit").send_keys(denek.number)

    # name
    for i in ("gt_ogrencino_adsoyadedit", "gt_ogrencino_adedit"):
        try:
            driver.find_element("id", i).send_keys(denek.name)
        except NoSuchElementException:
            pass
        else:
            break

    # submit
    driver.find_element("id", "gt_ogrencino_girisbtn").submit()

    # at deneme selection page

    try:
        WebDriverWait(driver, 6).until(
            EC.presence_of_element_located(
                (
                    "xpath",
                    "/html/body/section/div/div[1]/div/div/h6[2]",
                )  # base xpath for links
            )
        )
    except TimeoutException as e:
        raise DenekProbablyDidntTakeDeneme(
            f"Denek probably did not take any denemes from {deneme_url}"
        ) from e

    root = driver.find_element("xpath", "/html/body/section")
    try:
        root.find_element("xpath", f".//a[text()='{deneme_name}']").click()
    except NoSuchElementException as e:
        raise DenekDidntTakeDeneme(
            f"Denek did not take the deneme {deneme_name} from {deneme_url}"
        ) from e

    # at deneme result page

    root = driver.find_element("xpath", "/html/body/section")

    rank_base1 = root.find_element("xpath", ".//div[1]/div[5]/div/div/div")
    rank_base2 = root.find_element("xpath", ".//div[1]/div[6]/div/div/div")

    ranks = []
    for i in range(2, 7):
        ranks.append(
            int(rank_base1.find_element("xpath", f".//div[{i}]").text.split("\n")[0])
        )  # "123\n%0.33"
    for i in range(2, 7):
        ranks.append(int(rank_base2.find_element("xpath", f".//div[{i}]").text))

    ranks = Ranking(*ranks)

    class_ = (
        root.find_element("xpath", ".//div/div[1]/div/div/h5")
        .text.replace("-", "")  # "-9A", "11A"
        .split()[0]
    )  # "12C / 987"

    score = float(
        root.find_element("xpath", ".//div[1]/div[3]/div/div/div/div[2]").text.replace(
            ",", "."
        )
    )

    possible_result_divs = root.find_elements("xpath", ".//div[1]/div[*]")
    next_divs = iter(root.find_elements("xpath", ".//div[1]/div[*]"))
    next(next_divs)

    result_data = {}

    for i, j in zip(possible_result_divs, next_divs):
        try:
            data_test = j.find_element("xpath", ".//div[2]/div/div")
            title = i.find_element("xpath", ".//div/div")
        except NoSuchElementException:
            continue

        if data_test.find_elements("tag name", "h3"):
            d = "3"
        elif data_test.find_elements("tag name", "h2"):
            d = "2"
        elif data_test.find_elements("tag name", "h5"):
            d = "5[2]"
        else:
            continue

        result_data[title.text] = LessonBasedResult(
            true=int(j.find_element("xpath", f".//div[2]/div/div/h{d}").text),
            false=int(j.find_element("xpath", f".//div[3]/div/div/h{d}").text),
            empty=int(j.find_element("xpath", f".//div[4]/div/div/h{d}").text),
            net=float(
                j.find_element("xpath", f".//div[5]/div/div/h{d}").text.replace(
                    ",", "."
                )
            ),
            question_count=int(j.find_element("xpath", f".//div[1]/div/div/h{d}").text),
            full_name=title.text,
        )

    response = {}
    total = LessonBasedResult.create_empty(0, "denemesonuc_unset_total")
    for export, (d) in deneme_lesson_names.items():
        name = d["name"]
        istotal = d.get("total", False)
        count = d["question_count"]
        result = result_data.get(name, LessonBasedResult.create_empty(count, name))

        if istotal:
            total = result
            continue

        response[export] = result

    container = LessonResultContainer(response)

    denek.add_report(
        Report(
            score=score,
            ranking=ranks,
            result=total,
            denek_class=class_,
            lessons=container,
            deneme_name=deneme_name,
        )
    )
