import numpy.testing as npt
import pytest
from pyannote.core import Annotation, Segment

from aladdin.diarization.metrics.sm_diarisation_metrics.metrics import words as MetricsWords


@pytest.fixture
def reference():
    reference = Annotation()
    reference[Segment(0.0, 2.0)] = "A"
    reference[Segment(2.0, 3.0)] = "B"
    reference[Segment(3.0, 5.0)] = "A"
    reference[Segment(5.0, 6.0)] = "C"
    return reference


@pytest.fixture
def reference_short_start():
    reference = Annotation()
    reference[Segment(2.0, 3.0)] = "B"
    reference[Segment(3.0, 5.0)] = "A"
    reference[Segment(5.0, 6.0)] = "C"
    return reference


@pytest.fixture
def reference_short_end():
    reference = Annotation()
    reference[Segment(0.0, 2.0)] = "A"
    reference[Segment(2.0, 3.0)] = "B"
    reference[Segment(3.0, 5.0)] = "A"
    return reference


@pytest.fixture
def hypothesis_perfect():
    hypothesis = Annotation()
    hypothesis[Segment(0.0, 0.5)] = "S1"
    hypothesis[Segment(0.6, 1.1)] = "S1"
    hypothesis[Segment(1.3, 1.5)] = "S1"
    hypothesis[Segment(1.7, 2.1)] = "S1"
    hypothesis[Segment(2.3, 2.5)] = "S2"
    hypothesis[Segment(2.6, 2.8)] = "S2"
    hypothesis[Segment(2.9, 3.4)] = "S1"
    hypothesis[Segment(3.7, 4.1)] = "S1"
    hypothesis[Segment(4.3, 4.7)] = "S1"
    hypothesis[Segment(5.1, 5.9)] = "S3"
    return hypothesis


@pytest.fixture
def hypothesis_errors():
    hypothesis = Annotation()
    hypothesis[Segment(0.0, 0.5)] = "S3"  # incorrect label (label changed S1->S3)
    hypothesis[Segment(0.6, 1.3)] = "S1"
    hypothesis[Segment(1.4, 1.7)] = "S2"  # incorrect label (label changed S1->S2)
    hypothesis[Segment(1.9, 2.3)] = "S1"  # incorrect label (time shifted)
    hypothesis[Segment(2.3, 2.5)] = "S2"
    hypothesis[Segment(2.6, 2.8)] = "S2"
    hypothesis[Segment(2.9, 3.4)] = "S1"
    hypothesis[Segment(3.7, 4.1)] = "S1"
    hypothesis[Segment(4.3, 4.7)] = "S1"
    hypothesis[Segment(5.1, 5.9)] = "S1"  # incorrect label (label changed S3->S1)
    return hypothesis


@pytest.fixture
def hypothesis_short_start():
    hypothesis = Annotation()
    hypothesis[Segment(1.0, 1.5)] = "S1"
    hypothesis[Segment(1.7, 2.1)] = "S1"
    hypothesis[Segment(2.3, 2.5)] = "S2"
    hypothesis[Segment(2.6, 2.8)] = "S2"
    hypothesis[Segment(2.9, 3.4)] = "S1"
    hypothesis[Segment(3.7, 4.1)] = "S1"
    hypothesis[Segment(4.3, 4.7)] = "S1"
    hypothesis[Segment(5.1, 5.9)] = "S3"
    return hypothesis


@pytest.fixture
def hypothesis_short_end():
    hypothesis = Annotation()
    hypothesis[Segment(0.0, 0.5)] = "S1"
    hypothesis[Segment(0.6, 1.1)] = "S1"
    hypothesis[Segment(1.3, 1.5)] = "S1"
    hypothesis[Segment(1.7, 2.1)] = "S1"
    hypothesis[Segment(2.3, 2.5)] = "S2"
    hypothesis[Segment(2.6, 2.8)] = "S2"
    hypothesis[Segment(2.9, 3.4)] = "S1"
    return hypothesis


# Tests on get_overlap


def test_get_partial_overlap_ordered():
    """Test the get overlap case, where the segments are ordered by start time"""
    a = Segment(1.7, 2.1)
    b = Segment(2.0, 3.0)
    overlap = MetricsWords.get_overlap(a, b)
    npt.assert_almost_equal(overlap, 0.100, decimal=3)


def test_get_partial_overlap_reversed():
    """Test the get overlap case, where the segments are in reverse order by start time"""
    a = Segment(2.0, 3.0)
    b = Segment(1.7, 2.1)
    overlap = MetricsWords.get_overlap(a, b)
    npt.assert_almost_equal(overlap, 0.100, decimal=3)


def test_get_full_overlap_ordered():
    """Test the get overlap case, where the segments are ordered by start time"""
    a = Segment(1.5, 2.5)
    b = Segment(1.8, 2.2)
    overlap = MetricsWords.get_overlap(a, b)
    npt.assert_almost_equal(overlap, 0.400, decimal=3)


def test_get_full_overlap_reversed():
    """Test the get overlap case, where the segments are in reverse order by start time"""
    a = Segment(1.8, 2.2)
    b = Segment(1.5, 2.5)
    overlap = MetricsWords.get_overlap(a, b)
    npt.assert_almost_equal(overlap, 0.400, decimal=3)


def test_get_overlap_no_overlap_ordered():
    """Test the get overlap case, where the segments are ordered by start time"""
    a = Segment(1.7, 2.0)
    b = Segment(2.1, 3.0)
    overlap = MetricsWords.get_overlap(a, b)
    npt.assert_almost_equal(overlap, 0.000, decimal=3)


def test_get_overlap_no_overlap_reversed():
    """Test the get overlap case, where the segments are in reverse order by start time"""
    a = Segment(2.1, 3.0)
    b = Segment(1.7, 2.0)
    overlap = MetricsWords.get_overlap(a, b)
    npt.assert_almost_equal(overlap, 0.000, decimal=3)


# Tests on WordDiarizationErrorRate, returning error rate


def test_word_diarization_rate_perfect(reference, hypothesis_perfect):
    """Testing computing error rate in the perfect case, where all words should be correct"""
    metric = MetricsWords.WordDiarizationErrorRate()
    error_rate = metric(reference, hypothesis_perfect)
    npt.assert_almost_equal(error_rate, 0.000, decimal=3)


def test_word_diarization_rate_errors(reference, hypothesis_errors):
    """Testing computing error rate in a mixed case, where we are expecting a number of errors"""
    metric = MetricsWords.WordDiarizationErrorRate()
    error_rate = metric(reference, hypothesis_errors)
    npt.assert_almost_equal(error_rate, 0.400, decimal=3)


# Tests on WordDiarizationErrorRate, returning details


def test_word_diarization_details_perfect(reference, hypothesis_perfect):
    """Testing getting metric details for the perfect case, where all words should be correct"""
    metric = MetricsWords.WordDiarizationErrorRate()
    detailed_results = metric(reference, hypothesis_perfect, detailed=True)
    assert detailed_results[MetricsWords.WDER_TOTAL] == 10
    assert detailed_results[MetricsWords.WDER_INCORRECT] == 0
    assert len(detailed_results[MetricsWords.WDER_WORD_RESULTS]) == 10


def test_word_diarization_details_errors(reference, hypothesis_errors):
    """Testing getting metric details for a mixed case, where we are expecting a number of errors"""
    metric = MetricsWords.WordDiarizationErrorRate()
    detailed_results = metric(reference, hypothesis_errors, detailed=True)
    assert detailed_results[MetricsWords.WDER_TOTAL] == 10
    assert detailed_results[MetricsWords.WDER_INCORRECT] == 4
    assert len(detailed_results[MetricsWords.WDER_WORD_RESULTS]) == 10


def test_word_diarization_details_ref_short_start(reference_short_start, hypothesis_perfect):
    """Testing getting metric details in the case the reference is shorter than the hypothesis (at the start)"""
    metric = MetricsWords.WordDiarizationErrorRate()
    detailed_results = metric(reference_short_start, hypothesis_perfect, detailed=True)
    assert detailed_results[MetricsWords.WDER_TOTAL] == 10
    assert detailed_results[MetricsWords.WDER_INCORRECT] == 4
    assert len(detailed_results[MetricsWords.WDER_WORD_RESULTS]) == 10


def test_word_diarization_details_ref_short_end(reference_short_end, hypothesis_perfect):
    """Testing getting metric details in the case the reference is shorter than the hypothesis (at the end)"""
    metric = MetricsWords.WordDiarizationErrorRate()
    detailed_results = metric(reference_short_end, hypothesis_perfect, detailed=True)
    assert detailed_results[MetricsWords.WDER_TOTAL] == 10
    assert detailed_results[MetricsWords.WDER_INCORRECT] == 1
    assert len(detailed_results[MetricsWords.WDER_WORD_RESULTS]) == 10


def test_word_diarization_details_hyp_short_start(reference, hypothesis_short_start):
    """Testing getting metric details in the case the hypothesis is shorter than the reference (at the start)"""
    metric = MetricsWords.WordDiarizationErrorRate()
    detailed_results = metric(reference, hypothesis_short_start, detailed=True)
    assert detailed_results[MetricsWords.WDER_TOTAL] == 8
    assert detailed_results[MetricsWords.WDER_INCORRECT] == 0
    assert len(detailed_results[MetricsWords.WDER_WORD_RESULTS]) == 8


def test_word_diarization_details_hyp_short_end(reference, hypothesis_short_end):
    """Testing getting metric details in the case the hypothesis is shorter than the reference (at the end)"""
    metric = MetricsWords.WordDiarizationErrorRate()
    detailed_results = metric(reference, hypothesis_short_end, detailed=True)
    assert detailed_results[MetricsWords.WDER_TOTAL] == 7
    assert detailed_results[MetricsWords.WDER_INCORRECT] == 0
    assert len(detailed_results[MetricsWords.WDER_WORD_RESULTS]) == 7
