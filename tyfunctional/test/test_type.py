# pylint: disable-all
from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from typing import Any, Iterator, Optional
    from typing_extensions import assert_type
    from tyfunctional import seq, pseq
    from tyfunctional.pipeline import Sequence
    from pandas import DataFrame

    def type_checking() -> None:
        """
        This serves as a test for type annotations. Running mypy against this file will identify any discrepancies between the expected return type and the actual return type.
        """
        num_seq: Sequence[int] = seq([1, 2, 3])
        l: list[Any] = []

        t__evaluate: Iterator[int] = num_seq._evaluate()

        # t__transform = num_seq._transform()

        t_sequence: list[int] = num_seq.sequence

        t_cache: Sequence[int] = num_seq.cache()

        t_head: int = seq([1, 2, 3]).head()

        t_first: int = seq([1, 2, 3]).first()

        t_head_option: int | None = seq([1, 2, 3]).head_option()

        t_last: int = seq([1, 2, 3]).last()

        t_last_option: int | None = seq([1, 2, 3]).last_option()

        t_init: Sequence[int] = seq([1, 2, 3]).init()

        t_tail: Sequence[int] = seq([1, 2, 3]).tail()

        t_inits: Sequence[Sequence[int]] = seq([1, 2, 3]).inits()

        t_tails: Sequence[Sequence[int]] = seq([1, 2, 3]).tails()

        t_cartesian: Sequence[tuple[int, int]] = seq.range(2).cartesian(range(2))

        t_drop: Sequence[int] = seq([1, 2, 3, 4, 5]).drop(2)

        t_drop_right: Sequence[int] = seq([1, 2, 3, 4, 5]).drop_right(2)

        t_drop_while: Sequence[int] = seq([1, 2, 3, 4, 5, 1, 2]).drop_while(
            lambda x: x < 3
        )

        t_take: Sequence[int] = seq([1, 2, 3, 4]).take(2)

        t_take_while: Sequence[int] = seq([1, 2, 3, 4, 5, 1, 2]).take_while(
            lambda x: x < 3
        )

        t_union: Sequence[int] = seq([1, 1, 2, 3, 3]).union([1, 4, 5])

        t_intersection: Sequence[int] = seq([1, 1, 2, 3]).intersection([2, 3, 4])

        t_difference: Sequence[int] = seq([1, 2, 3]).difference([2, 3, 4])

        t_symmetric_difference: Sequence[int] = seq([1, 2, 3, 3]).symmetric_difference(
            [2, 4, 5]
        )

        t_map: Sequence[int] = seq([1, 2, 3, 4]).map(lambda x: x * -1)

        t_select: Sequence[int] = num_seq.select(lambda x: x * -1)

        t_starmap: Sequence[int] = seq([(2, 3), (-2, 1), (0, 10)]).starmap(
            lambda x, y: x + y
        )

        t_smap: Sequence[int] = seq([(2, 3), (-2, 1), (0, 10)]).smap(lambda x, y: x + y)

        t_for_each: None = seq([1, 2, 3, 4]).for_each(l.append)  # type: ignore[func-returns-value]

        t_peek: list[int] = (
            seq([1, 2, 3, 4]).peek(print).map(lambda x: x**2).to_list()
        )

        t_filter2: Sequence[str] = seq(["-1", "1", None, "2"]).remove_none()

        t_filter: Sequence[int] = seq([-1, 1, -2, 2]).filter(lambda x: x > 0)

        t_filter_not: Sequence[int] = seq([-1, 1, -2, 2]).filter_not(lambda x: x > 0)

        t_where: Sequence[int] = seq([-1, 1, -2, 2]).where(lambda x: x > 0)

        t_count: int = seq([-1, -2, 1, 2]).count(lambda x: x > 0)

        t_len: int = seq([1, 2, 3]).len()

        t_size: int = seq([1, 2, 3]).size()

        t_empty: bool = seq([]).empty()

        t_non_empty: bool = seq([1]).non_empty()

        t_any: bool = seq([True, False]).any()

        t_all: bool = seq([True, True]).all()

        t_exists: bool = seq([1, 2, 3, 4]).exists(lambda x: x == 2)

        t_for_all: bool = seq([1, 2, 3]).for_all(lambda x: x > 0)

        t_max: str = seq("aa", "xyz", "abcd", "xyy").max()

        t_min: str = seq("aa", "xyz", "abcd", "xyy").min()

        t_max_by: str = seq("aa", "xyz", "abcd", "xyy").max_by(len)

        t_min_by: int = seq([2, 4, 5, 1, 3]).min_by(lambda num: num % 6)

        t_find: str | None = seq(["abc", "ab", "bc"]).find(lambda x: len(x) == 2)

        t_flatten: Sequence[int] = seq([[1, 2], [3, 4], [5, 6]]).flatten()

        t_flat_map: Sequence[int] = seq([[1, 2], [3, 4], [5, 6]]).flat_map(lambda x: x)

        t_group_by: Sequence[tuple[int, Sequence[str]]] = seq(
            ["abc", "ab", "z", "f", "qw"]
        ).group_by(len)

        t_group_by_key: Sequence[
            tuple[str, list[int]]
        ] = seq(  # pyright: ignore[reportAssignmentType]
            [("a", 1), ("b", 2), ("b", 3), ("b", 4), ("c", 3), ("c", 0)]
        ).group_by_key()

        t_reduce_by_key: Sequence[tuple[str, int]] = seq(
            [("a", 1), ("b", 2), ("b", 3), ("b", 4), ("c", 3), ("c", 0)]
        ).reduce_by_key(lambda x, y: x + y)

        t_count_by_key: Sequence[tuple[str, int]] = seq(
            [("a", 1), ("b", 2), ("b", 3), ("b", 4), ("c", 3), ("c", 0)]
        ).count_by_key()

        t_count_by_value: Sequence[tuple[str, int]] = seq(
            ["a", "a", "a", "b", "b", "c", "d"]
        ).count_by_value()

        t_reduce: int = seq([1, 2, 3]).reduce(lambda x, y: x + y)

        t_accumulate: Sequence[int] = seq([1, 2, 3]).accumulate(lambda x, y: x + y)

        t_make_string: str = seq([1, 2, 3]).make_string("@")

        t_product: float = seq([(1, 2), (1, 3), (1, 4)]).product(lambda x: x[0])

        t_sum: int | float = seq([(1, 2), (1, 3), (1, 4)]).sum(lambda x: x[0])

        t_average: float = seq([("a", 1), ("b", 2)]).average(lambda x: x[1])

        # t_aggregate = num_seq.aggregate()

        t_fold_left: list[str] = seq("a", "b", "c").fold_left(
            ["start"], lambda current, next: current + [next]
        )

        t_fold_right: list[str] = seq("a", "b", "c").fold_right(
            ["start"], lambda next, current: [next] + current
        )

        t_zip: Sequence[tuple[int, int]] = seq([1, 2, 3]).zip([4, 5, 6])

        t_zip_with_index: Sequence[tuple[str, int]] = seq(
            ["a", "b", "c"]
        ).zip_with_index()

        t_zip_with_next: Sequence[tuple[str, str]] = seq(
            ["a", "b", "c"]
        ).zip_with_next()

        t_enumerate: Sequence[tuple[int, str]] = seq(["a", "b", "c"]).enumerate(start=1)

        t_partition: tuple[Sequence[int], Sequence[int]] = seq(
            [-1, 1, -2, 2]
        ).partition(lambda x: x < 0)

        t_grouped: Sequence[Sequence[int]] = seq([1, 2, 3, 4, 5, 6, 7, 8]).grouped(3)

        t_sliding: Sequence[Sequence[int]] = num_seq.sliding(3)

        t_sorted: Sequence[int] = seq([2, 1, 4, 3]).sorted()

        t_order_by: Sequence[tuple[int, str]] = seq(
            [(2, "a"), (1, "b"), (4, "c"), (3, "d")]
        ).order_by(lambda x: x[0])

        t_reverse: Sequence[int] = seq([1, 2, 3]).reverse()

        t_distinct: Sequence[int] = seq([1, 1, 2, 3, 3, 3, 4]).distinct()

        t_distinct_by: Sequence[int] = num_seq.distinct_by(str)

        t_slice: Sequence[int] = seq([1, 2, 3, 4]).slice(1, 3)

        t_to_list: list[int] = seq([1, 2, 3]).to_list()

        t_list: list[int] = seq([1, 2, 3]).list()

        t_to_set: set[int] = seq([1, 1, 2, 2]).to_set()

        t_set: set[int] = seq([1, 1, 2, 2]).set()

        t_to_dict: dict[str, int] = seq(
            [("a", 1), ("b", 2)]
        ).to_dict()  # pyright: ignore[reportAssignmentType]

        t_dict: dict[str, int] = seq(
            [("a", 1), ("b", 2)]
        ).dict()  # pyright: ignore[reportAssignmentType]

        t_to_file: None = num_seq.to_file("/tmp/test.json")  # type: ignore[func-returns-value]

        t_to_jsonl: None = num_seq.to_jsonl("/tmp/test.json")  # type: ignore[func-returns-value]

        t_to_json: None = num_seq.to_json("/tmp/test.json")  # type: ignore[func-returns-value]

        t_to_csv: None = num_seq.to_csv("/tmp/test.csv")  # type: ignore[func-returns-value]

        # t__to_sqlite3_by_query = num_seq._to_sqlite3_by_query()

        # t__to_sqlite3_by_table = num_seq._to_sqlite3_by_table()

        t_to_sqlite3: None = seq([(1, "Tom"), (2, "Jack")]).to_sqlite3(  # type: ignore[func-returns-value]
            "users.db", "INSERT INTO user (id, name) VALUES (?, ?)"
        )

        t_to_pandas: DataFrame = num_seq.to_pandas()

        t_show: None = num_seq.show()  # type: ignore[func-returns-value]

        t__repr_html_: str | None = num_seq._repr_html_()

        t_tabulate: str | None = num_seq.tabulate()

    def type_checking_strict() -> None:
        """
        Strict type assertions using assert_type. Unlike annotated assignments above,
        assert_type fails if the expression's inferred type degrades to Any, so these
        also guard against regressions in overload resolution.
        """
        kv_pairs: list[tuple[str, int]] = [("a", 1), ("b", 2)]
        kv_seq = seq(kv_pairs)
        assert_type(kv_seq, Sequence[tuple[str, int]])

        # Entry points
        assert_type(seq([1, 2, 3]), Sequence[int])
        assert_type(seq(1, 2, 3), Sequence[int])
        assert_type(seq(range(3)), Sequence[int])
        assert_type(seq.range(3), Sequence[int])
        assert_type(seq.chain([1], [2]), Sequence[int])
        assert_type(pseq([1, 2, 3]), Sequence[int])
        assert_type(pseq(1, 2, 3), Sequence[int])
        assert_type(pseq.range(3), Sequence[int])

        # Chained transformations infer through the chain, including lambdas
        assert_type(
            seq([1, 2, 3]).map(lambda x: x * 2).filter(lambda x: x > 2).to_list(),
            list[int],
        )
        assert_type(seq([1, 2, 3]).map(str), Sequence[str])
        assert_type(pseq([1, 2, 3]).map(str).to_list(), list[str])

        # Joins carry key/value types and per-flavor None-ness
        other: list[tuple[str, float]] = [("a", 9.0)]
        assert_type(kv_seq.inner_join(other), Sequence[tuple[str, tuple[int, float]]])
        assert_type(kv_seq.join(other), Sequence[tuple[str, tuple[int, float]]])
        assert_type(
            kv_seq.join(other, "left"),
            Sequence[tuple[str, tuple[int, Optional[float]]]],
        )
        assert_type(
            kv_seq.left_join(other),
            Sequence[tuple[str, tuple[int, Optional[float]]]],
        )
        assert_type(
            kv_seq.right_join(other),
            Sequence[tuple[str, tuple[Optional[int], float]]],
        )
        assert_type(
            kv_seq.outer_join(other),
            Sequence[tuple[str, tuple[Optional[int], Optional[float]]]],
        )

        # starmap/smap infer lambda parameters from the tuple element type
        assert_type(kv_seq.starmap(lambda k, v: v * 1.0), Sequence[float])
        assert_type(kv_seq.smap(lambda k, v: v * 1.0), Sequence[float])

        # aggregate: one, two, and three argument forms
        assert_type(seq([1, 2, 3]).aggregate(lambda a, b: a + b), int)
        assert_type(seq([1, 2, 3]).aggregate("", lambda acc, x: acc + str(x)), str)
        assert_type(seq([1, 2, 3]).aggregate("", lambda acc, x: acc + str(x), len), int)

        # Numeric reductions preserve the element type
        assert_type(seq([1, 2, 3]).sum(), int)
        assert_type(seq([1.0, 2.0]).sum(), float)
        assert_type(seq([(1, 2)]).sum(lambda x: x[0]), int)
        assert_type(seq([1, 2, 3]).product(), int)
        assert_type(seq([1.0, 2.0]).product(), float)
        assert_type(seq([1, 2]).average(), float)
        assert_type(kv_seq.average(lambda x: x[1]), float)

        # Indexing: int index yields an element, slice yields a Sequence
        assert_type(seq([1, 2, 3])[0], int)
        assert_type(seq([1, 2, 3])[0:2], Sequence[int])

        # File and database inputs
        assert_type(seq.open("file.txt"), Sequence[str])
        assert_type(seq.open("file.txt", delimiter=","), Sequence[str])
        assert_type(seq.open("file.bin", mode="rb"), Sequence[bytes])
        assert_type(seq.csv("file.csv"), Sequence[list[str]])
        assert_type(seq.jsonl("file.jsonl"), Sequence[Any])
        assert_type(seq.sqlite3("db.sqlite", "select * from t"), Sequence[Any])
