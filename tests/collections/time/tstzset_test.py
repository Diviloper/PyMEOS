from copy import copy
from datetime import datetime, timedelta, timezone

import pytest

from pymeos import (
    TsTzSet,
    TsTzSpan,
    TsTzSpanSet,
)
from tests.conftest import TestPyMEOS


class TestTsTzSet(TestPyMEOS):
    ts_set = TsTzSet("{2019-09-01 00:00:00+0, 2019-09-02 00:00:00+0, 2019-09-03 00:00:00+0}")

    @staticmethod
    def assert_tstzset_equality(ts_set: TsTzSet, timestamps: list[datetime]):
        assert ts_set.num_elements() == len(timestamps)
        assert ts_set.elements() == timestamps


class TestTsTzSetConstructors(TestTsTzSet):
    def test_string_constructor(self):
        self.assert_tstzset_equality(
            self.ts_set,
            [
                datetime(2019, 9, 1, 0, 0, 0, tzinfo=timezone.utc),
                datetime(2019, 9, 2, 0, 0, 0, tzinfo=timezone.utc),
                datetime(2019, 9, 3, 0, 0, 0, tzinfo=timezone.utc),
            ],
        )

    def test_list_constructor(self):
        ts_set = TsTzSet(
            elements=[
                datetime(2019, 9, 1, 0, 0, 0, tzinfo=timezone.utc),
                datetime(2019, 9, 2, 0, 0, 0, tzinfo=timezone.utc),
                datetime(2019, 9, 3, 0, 0, 0, tzinfo=timezone.utc),
            ]
        )
        self.assert_tstzset_equality(
            ts_set,
            [
                datetime(2019, 9, 1, 0, 0, 0, tzinfo=timezone.utc),
                datetime(2019, 9, 2, 0, 0, 0, tzinfo=timezone.utc),
                datetime(2019, 9, 3, 0, 0, 0, tzinfo=timezone.utc),
            ],
        )

    def test_hexwkb_constructor(self):
        ts_set = TsTzSet.from_hexwkb(
            TsTzSet(
                elements=[
                    datetime(2019, 9, 1, 0, 0, 0, tzinfo=timezone.utc),
                    datetime(2019, 9, 2, 0, 0, 0, tzinfo=timezone.utc),
                    datetime(2019, 9, 3, 0, 0, 0, tzinfo=timezone.utc),
                ]
            ).as_hexwkb()
        )
        self.assert_tstzset_equality(
            ts_set,
            [
                datetime(2019, 9, 1, 0, 0, 0, tzinfo=timezone.utc),
                datetime(2019, 9, 2, 0, 0, 0, tzinfo=timezone.utc),
                datetime(2019, 9, 3, 0, 0, 0, tzinfo=timezone.utc),
            ],
        )

    def test_from_as_constructor(self):
        assert self.ts_set == TsTzSet(str(self.ts_set))
        assert self.ts_set == TsTzSet.from_wkb(self.ts_set.as_wkb())
        assert self.ts_set == TsTzSet.from_hexwkb(self.ts_set.as_hexwkb())

    def test_copy_constructor(self):
        ts_set_copy = copy(self.ts_set)
        assert self.ts_set == ts_set_copy
        assert self.ts_set is not ts_set_copy


class TestTsTzSetOutputs(TestTsTzSet):
    def test_str(self):
        assert str(self.ts_set) == '{"2019-09-01 00:00:00+00", "2019-09-02 00:00:00+00", "2019-09-03 00:00:00+00"}'

    def test_repr(self):
        assert (
            repr(self.ts_set)
            == 'TsTzSet({"2019-09-01 00:00:00+00", "2019-09-02 00:00:00+00", "2019-09-03 00:00:00+00"})'
        )

    def test_as_hexwkb(self):
        assert self.ts_set == TsTzSet.from_hexwkb(self.ts_set.as_hexwkb())


class TestTimestampConversions(TestTsTzSet):
    def test_to_tstzspanset(self):
        assert self.ts_set.to_spanset() == TsTzSpanSet(
            "{[2019-09-01 00:00:00+00, 2019-09-01 00:00:00+00], "
            "[2019-09-02 00:00:00+00, 2019-09-02 00:00:00+00], "
            "[2019-09-03 00:00:00+00, 2019-09-03 00:00:00+00]}"
        )


class TestTsTzSetAccessors(TestTsTzSet):
    def test_duration(self):
        assert self.ts_set.duration() == timedelta(days=2)

    def test_tstzspan(self):
        assert self.ts_set.to_span() == TsTzSpan("[2019-09-01 00:00:00+00, 2019-09-03 00:00:00+00]")

    def test_num_timestamps(self):
        assert self.ts_set.num_elements() == 3
        assert len(self.ts_set) == 3

    def test_start_timestamp(self):
        assert self.ts_set.start_element() == datetime(2019, 9, 1, 0, 0, 0, tzinfo=timezone.utc)

    def test_end_timestamp(self):
        assert self.ts_set.end_element() == datetime(2019, 9, 3, 0, 0, 0, tzinfo=timezone.utc)

    def test_timestamp_n(self):
        assert self.ts_set.element_n(1) == datetime(2019, 9, 2, 0, 0, 0, tzinfo=timezone.utc)

    def test_timestamp_n_out_of_range(self):
        with pytest.raises(IndexError):
            self.ts_set.element_n(3)

    def test_timestamps(self):
        assert self.ts_set.elements() == [
            datetime(2019, 9, 1, 0, 0, 0, tzinfo=timezone.utc),
            datetime(2019, 9, 2, 0, 0, 0, tzinfo=timezone.utc),
            datetime(2019, 9, 3, 0, 0, 0, tzinfo=timezone.utc),
        ]

    def test_hash(self):
        assert hash(self.ts_set) == 527267058


class TestTsTzSetPositionFunctions(TestTsTzSet):
    timestamp = datetime(year=2020, month=1, day=1)
    tstzset = TsTzSet("{2020-01-01 00:00:00+0, 2020-01-31 00:00:00+0}")

    @pytest.mark.parametrize("other, expected", [(tstzset, False)], ids=["tstzset"])
    def test_is_contained_in(self, other, expected):
        assert self.ts_set.is_contained_in(other) == expected

    @pytest.mark.parametrize("other", [timestamp, tstzset], ids=["timestamp", "tstzset"])
    def test_contains(self, other):
        self.ts_set.contains(other)
        _ = other in self.tstzset

    @pytest.mark.parametrize("other", [tstzset], ids=["tstzset"])
    def test_overlaps(self, other):
        self.ts_set.overlaps(other)

    @pytest.mark.parametrize("other", [timestamp, tstzset], ids=["timestamp", "tstzset"])
    def test_is_before(self, other):
        self.ts_set.is_before(other)

    @pytest.mark.parametrize("other", [timestamp, tstzset], ids=["timestamp", "tstzset"])
    def test_is_over_or_before(self, other):
        self.ts_set.is_over_or_before(other)

    @pytest.mark.parametrize("other", [timestamp, tstzset], ids=["timestamp", "tstzset"])
    def test_is_after(self, other):
        self.ts_set.is_after(other)

    @pytest.mark.parametrize("other", [timestamp, tstzset], ids=["timestamp", "tstzset"])
    def test_is_over_or_after(self, other):
        self.ts_set.is_over_or_after(other)

    @pytest.mark.parametrize("other", [timestamp, tstzset], ids=["timestamp", "tstzset"])
    def test_distance(self, other):
        self.ts_set.distance(other)


class TestTsTzSetSetFunctions(TestTsTzSet):
    timestamp = datetime(year=2020, month=1, day=1)
    tstzset = TsTzSet("{2020-01-01 00:00:00+0, 2020-01-31 00:00:00+0}")
    tstzspan = TsTzSpan("(2020-01-01 00:00:00+0, 2020-01-31 00:00:00+0)")
    tstzspanset = TsTzSpanSet(
        "{(2020-01-01 00:00:00+0, 2020-01-31 00:00:00+0), (2021-01-01 00:00:00+0, 2021-01-31 00:00:00+0)}"
    )

    @pytest.mark.parametrize(
        "other",
        [tstzspan, tstzspanset, timestamp, tstzset],
        ids=["tstzspan", "tstzspanset", "timestamp", "tstzset"],
    )
    def test_intersection(self, other):
        self.tstzset.intersection(other)
        self.tstzset * other

    @pytest.mark.parametrize(
        "other",
        [tstzspan, tstzspanset, timestamp, tstzset],
        ids=["tstzspan", "tstzspanset", "timestamp", "tstzset"],
    )
    def test_union(self, other):
        self.tstzset.union(other)
        self.tstzset + other

    @pytest.mark.parametrize(
        "other",
        [tstzspan, tstzspanset, timestamp, tstzset],
        ids=["tstzspan", "tstzspanset", "timestamp", "tstzset"],
    )
    def test_minus(self, other):
        self.tstzset.minus(other)
        self.tstzset - other


class TestTsTzSetComparisons(TestTsTzSet):
    tstzset = TsTzSet("{2020-01-01 00:00:00+0, 2020-01-31 00:00:00+0}")
    other = TsTzSet("{2020-01-02 00:00:00+0, 2020-03-31 00:00:00+0}")

    def test_eq(self):
        _ = self.tstzset == self.other

    def test_ne(self):
        _ = self.tstzset != self.other

    def test_lt(self):
        _ = self.tstzset < self.other

    def test_le(self):
        _ = self.tstzset <= self.other

    def test_gt(self):
        _ = self.tstzset > self.other

    def test_ge(self):
        _ = self.tstzset >= self.other


class TestTsTzSetFunctionsFunctions(TestTsTzSet):
    tstzset = TsTzSet("{2020-01-01 00:00:00+0, 2020-01-02 00:00:00+0, 2020-01-04 00:00:00+0}")

    @pytest.mark.parametrize(
        "delta,result",
        [
            (
                timedelta(days=4),
                [
                    datetime(2020, 1, 5, tzinfo=timezone.utc),
                    datetime(2020, 1, 6, tzinfo=timezone.utc),
                    datetime(2020, 1, 8, tzinfo=timezone.utc),
                ],
            ),
            (
                timedelta(days=-4),
                [
                    datetime(2019, 12, 28, tzinfo=timezone.utc),
                    datetime(2019, 12, 29, tzinfo=timezone.utc),
                    datetime(2019, 12, 31, tzinfo=timezone.utc),
                ],
            ),
            (
                timedelta(hours=2),
                [
                    datetime(2020, 1, 1, 2, tzinfo=timezone.utc),
                    datetime(2020, 1, 2, 2, tzinfo=timezone.utc),
                    datetime(2020, 1, 4, 2, tzinfo=timezone.utc),
                ],
            ),
            (
                timedelta(hours=-2),
                [
                    datetime(2019, 12, 31, 22, tzinfo=timezone.utc),
                    datetime(2020, 1, 1, 22, tzinfo=timezone.utc),
                    datetime(2020, 1, 3, 22, tzinfo=timezone.utc),
                ],
            ),
        ],
        ids=["positive days", "negative days", "positive hours", "negative hours"],
    )
    def test_shift(self, delta, result):
        shifted = self.tstzset.shift(delta)
        self.assert_tstzset_equality(shifted, result)

    @pytest.mark.parametrize(
        "delta,result",
        [
            (
                timedelta(days=6),
                [
                    datetime(2020, 1, 1, tzinfo=timezone.utc),
                    datetime(2020, 1, 3, tzinfo=timezone.utc),
                    datetime(2020, 1, 7, tzinfo=timezone.utc),
                ],
            ),
            (
                timedelta(hours=3),
                [
                    datetime(2020, 1, 1, tzinfo=timezone.utc),
                    datetime(2020, 1, 1, 1, tzinfo=timezone.utc),
                    datetime(2020, 1, 1, 3, tzinfo=timezone.utc),
                ],
            ),
        ],
        ids=["days", "hours"],
    )
    def test_scale(self, delta, result):
        scaled = self.tstzset.scale(delta)
        self.assert_tstzset_equality(scaled, result)

    def test_shift_scale(self):
        shifted_scaled = self.tstzset.shift_scale(timedelta(days=4), timedelta(hours=3))
        self.assert_tstzset_equality(
            shifted_scaled,
            [
                datetime(2020, 1, 5, tzinfo=timezone.utc),
                datetime(2020, 1, 5, 1, tzinfo=timezone.utc),
                datetime(2020, 1, 5, 3, tzinfo=timezone.utc),
            ],
        )


class TestTsTzSetMiscFunctions(TestTsTzSet):
    tstzset = TsTzSet("{2020-01-01 00:00:00+0, 2020-01-02 00:00:00+0, 2020-01-04 00:00:00+0}")

    def test_hash(self):
        hash(self.tstzset)
