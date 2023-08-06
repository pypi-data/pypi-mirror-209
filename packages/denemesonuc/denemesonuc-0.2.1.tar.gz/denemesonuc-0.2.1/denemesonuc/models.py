"""Models for denemesonuc package."""
from dataclasses import InitVar, dataclass, field
from typing import NamedTuple


@dataclass
class Result(object):
    """Store result of a test."""

    true: int
    """True question count"""
    false: int
    """False question count"""
    empty: int
    """Empty question count"""
    net: float
    """Net value"""
    question_count: int
    """Question count"""

    @classmethod
    def create_empty(cls, question_count: int):
        """Create an empty result."""
        return cls(
            true=0,
            false=0,
            empty=question_count,
            net=0,
            question_count=question_count,
        )


@dataclass
class LessonBasedResult(Result):
    """Store result of a test based on lesson."""

    full_name: str
    """Full name of the lesson"""
    # short_name: str
    # """Short name of the lesson, generally first three letters of the full name"""

    @classmethod
    def create_empty(cls, question_count: int, full_name: str):
        """Create an empty result."""
        return cls(
            true=0,
            false=0,
            empty=question_count,
            net=0,
            question_count=question_count,
            full_name=full_name,
        )


# @dataclass
# class TotalResult(Result):
#     """Store result of a test based on all lessons."""
#     pass


class Ranking(NamedTuple):
    """Store ranking of a test."""

    class_: int
    """Ranking in class"""
    school: int
    """Ranking in school"""
    district: int
    """Ranking in district"""
    province: int
    """Ranking in province"""
    total: int
    """Ranking in total"""
    class_attandance: int
    """Attandance in class"""
    school_attandance: int
    """Attandance in school"""
    district_attandance: int
    """Attandance in district"""
    province_attandance: int
    """Attandance in province"""
    total_attandance: int
    """Attandance in total"""

    def to_list(self):
        """Return a list of rankings."""
        return ((self[i], self[i + 4]) for i in range(4))


class LessonResultContainer(object):
    """Store a list of lesson based results.

    Class attributes are shortcuts for accessing results and they may vary between denemes.
    """

    # docstring/typing stuff for standard lessons
    edb: LessonBasedResult
    """Result for lesson `Edebiyat`"""
    trh: LessonBasedResult
    """Result for lesson `Tarih`"""
    cog: LessonBasedResult
    """Result for lesson `Coğrafya`"""
    fel: LessonBasedResult
    """Result for lesson `Felsefe`"""
    din: LessonBasedResult
    """Result for lesson `Din Kültürü ve Ahlak Bilgisi`"""
    sfl: LessonBasedResult
    """Result for lesson `Seçmeli Felsefe`"""
    mat: LessonBasedResult
    """Result for lesson `Matematik`"""
    fiz: LessonBasedResult
    """Result for lesson `Fizik`"""
    kim: LessonBasedResult
    """Result for lesson `Kimya`"""
    biy: LessonBasedResult
    """Result for lesson `Biyoloji`"""

    def __init__(self, results: dict[str, LessonBasedResult]) -> None:
        """Initialize a LessonResultContainer.

        Args:
            results: A dict of results. Keys are short names of the lessons and values are results.
        """
        self._results = results
        self.__dict__.update(self._results)

    def __getitem__(self, key: str) -> LessonBasedResult:
        """Get a result by its short name."""
        try:
            return self._results[key]
        except KeyError:
            raise KeyError(f"Lesson `{key}` not found") from None

    def __iter__(self):
        """Iterate over the results."""
        return iter(self._results)

    def __len__(self) -> int:
        """Get the number of the results."""
        return len(self._results)

    def __repr__(self) -> str:
        """Get a string representation of the object."""
        return f"LessonResultContainer({self._results!r})"


class Report(NamedTuple):
    """Deneme report."""

    score: float
    """Score of the deneme"""
    denek_class: str
    """Class of the denek"""
    deneme_name: str
    """Name of the deneme"""
    ranking: Ranking
    """Ranking of the deneme"""
    result: LessonBasedResult
    """Result of the deneme"""
    lessons: LessonResultContainer
    """Lesson based results of the deneme"""


@dataclass
class Denek(object):
    """Store information about a denek."""

    name: str
    """Name of the denek"""
    number: int
    """Number of the denek"""
    school: str
    """School of the denek"""
    district: str
    """District of the denek"""
    province: str
    """Province of the denek"""
    grade_: InitVar[str | int]
    """Grade of the denek. Converted to str if int is given."""
    reports: list[Report] = field(default_factory=list)
    """Deneme reports of the denek"""
    grade: str = field(init=False)
    """Grade of the denek"""

    def __post_init__(self, grade_):
        """Post init method."""
        if isinstance(grade_, int):
            self.grade = str(grade_) + ".Sınıf"
        elif isinstance(grade_, str):
            self.grade = grade_
        else:
            raise TypeError(f"grade must be str or int, not {type(grade_).__name__}")

    def add_report(self, report: Report) -> None:
        """Add a report to the denek.

        Args:
            report: Report to add.
        """
        # delete old report if exists
        self.reports = [r for r in self.reports if r.deneme_name != report.deneme_name]
        self.reports.append(report)

    def get_report(self, deneme_name: str) -> Report:
        """Get report of a deneme.

        Args:
            deneme_name: Name of the deneme to get report of.

        Returns:
            Report of the deneme.

        Raises:
            ValueError: If deneme not found.
        """
        for report in self.reports:
            if report.deneme_name == deneme_name:
                return report
        raise ValueError(f"Deneme `{deneme_name}` not found")

    def del_report(self, deneme_name: str) -> None:
        """Delete report of a deneme.

        Args:
            deneme_name: Name of the deneme to delete.
        """
        self.reports = [r for r in self.reports if r.deneme_name != deneme_name]

    def __str__(self) -> str:
        """Return a string representation of the denek."""
        return f"{self.number}[{self.name}]@({self.school}:{self.grade})[{self.district}, {self.province}]"


class FetchError(Exception):
    """Error while fetching deneme results."""

    pass


class DenekNotFound(FetchError):
    """Denek not found. This may be caused by wrong denek credentials or an escaped denek."""

    pass


class DenekDidntTakeDeneme(DenekNotFound):
    """Denek didn't take the deneme."""

    pass


class DenekProbablyDidntTakeDeneme(DenekNotFound):
    """Denek probably didn't take the deneme."""

    pass
