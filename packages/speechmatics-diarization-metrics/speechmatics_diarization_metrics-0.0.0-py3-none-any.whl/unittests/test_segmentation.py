import numpy.testing as npt
import pytest
from pyannote.core import Annotation, Segment

from aladdin.diarization.metrics.sm_diarisation_metrics.metrics import segmentation as MetricsSegmentation


@pytest.fixture
def reference():
    reference = Annotation()
    reference[Segment(0.0, 5.0)] = "A"
    reference[Segment(5.0, 20.0)] = "B"
    reference[Segment(22.0, 25.0)] = "A"
    reference[Segment(26.0, 30.0)] = "B"
    return reference


@pytest.fixture
def reference_gaps_within_speaker():
    reference = Annotation()
    reference[Segment(0.0, 5.0)] = "A"
    reference[Segment(5.0, 8.0)] = "B"
    reference[Segment(9.0, 12.0)] = "B"
    reference[Segment(14.0, 20.0)] = "B"
    reference[Segment(22.0, 25.0)] = "A"
    reference[Segment(26.0, 30.0)] = "B"
    return reference


@pytest.fixture
def hypothesis_perfect():
    hypothesis = Annotation()
    hypothesis[Segment(0.0, 5.0)] = "A"
    hypothesis[Segment(5.0, 20.0)] = "B"
    hypothesis[Segment(22.0, 25.0)] = "A"
    hypothesis[Segment(26.0, 30.0)] = "B"
    return hypothesis


@pytest.fixture
def hypothesis_gaps_within_speaker():
    hypothesis = Annotation()
    hypothesis[Segment(0.0, 5.0)] = "A"
    hypothesis[Segment(5.0, 8.0)] = "B"
    hypothesis[Segment(9.0, 12.0)] = "B"
    hypothesis[Segment(14.0, 20.0)] = "B"
    hypothesis[Segment(22.0, 25.0)] = "A"
    hypothesis[Segment(26.0, 30.0)] = "B"
    return hypothesis


@pytest.fixture
def hypothesis_close():
    hypothesis = Annotation()
    hypothesis[Segment(0.1, 4.7)] = "A"
    hypothesis[Segment(4.8, 20.1)] = "B"
    hypothesis[Segment(22.1, 25.2)] = "A"
    hypothesis[Segment(26.0, 30.0)] = "B"
    return hypothesis


@pytest.fixture
def hypothesis_early_ends():
    hypothesis = Annotation()
    hypothesis[Segment(0.0, 3.0)] = "A"
    hypothesis[Segment(5.0, 17.0)] = "B"
    hypothesis[Segment(22.0, 24.0)] = "A"
    hypothesis[Segment(26.0, 27.0)] = "B"
    return hypothesis


@pytest.fixture
def hypothesis_late_starts():
    hypothesis = Annotation()
    hypothesis[Segment(0.2, 3.0)] = "A"
    hypothesis[Segment(5.3, 17.0)] = "B"
    hypothesis[Segment(22.1, 24.0)] = "A"
    hypothesis[Segment(26.0, 27.0)] = "B"
    return hypothesis


@pytest.fixture
def hypothesis_false_alarms():
    hypothesis = Annotation()
    hypothesis[Segment(0.0, 5.0)] = "A"
    hypothesis[Segment(5.0, 10.0)] = "B"
    hypothesis[Segment(11.0, 13.0)] = "A"
    hypothesis[Segment(14.0, 20.0)] = "B"
    hypothesis[Segment(22.0, 25.0)] = "A"
    hypothesis[Segment(26.0, 29.0)] = "B"
    hypothesis[Segment(29.0, 30.0)] = "A"
    return hypothesis


@pytest.fixture
def hypothesis_misses():
    hypothesis = Annotation()
    hypothesis[Segment(0.0, 20.0)] = "B"
    hypothesis[Segment(22.0, 25.0)] = "A"
    hypothesis[Segment(26.0, 30.0)] = "B"
    return hypothesis


# Tests of recall function


def test_recall_perfect_match(reference, hypothesis_perfect):
    """Standard case where all the points match precisely"""
    metric = MetricsSegmentation.SegmentationRecall()
    recall = metric(reference, hypothesis_perfect)
    assert recall == 1.0


def test_recall_gaps_within_speaker_ref(reference_gaps_within_speaker, hypothesis_perfect):
    """Test behaviour if reference has gaps between regions of same speaker (has an impact)"""
    metric = MetricsSegmentation.SegmentationRecall()
    recall = metric(reference_gaps_within_speaker, hypothesis_perfect)
    npt.assert_almost_equal(recall, 0.666, decimal=3)


def test_recall_gaps_within_speaker_hyp(reference, hypothesis_gaps_within_speaker):
    """Test behaviour if hypothesis has gaps between regions of same speaker (has no impact)"""
    metric = MetricsSegmentation.SegmentationRecall()
    recall = metric(reference, hypothesis_gaps_within_speaker)
    assert recall == 1.0


def test_recall_close_match_normal_tolerance(reference, hypothesis_close):
    """Test behaviour if a close match, all within tolerance"""
    metric = MetricsSegmentation.SegmentationRecall(tolerance=0.5)
    recall = metric(reference, hypothesis_close)
    assert recall == 1.0


# def test_recall_close_match_normal_tolerance(reference, hypothesis_close):
#     """Test behaviour if a close match, but occasionally outside a low tolerance"""
#     metric = MetricsSegmentation.SegmentationRecall(tolerance=0.1)
#     recall = metric(reference, hypothesis_close)
#     npt.assert_almost_equal(recall, 0.5, decimal=3)


def test_recall_close_match_zero_tolerance(reference, hypothesis_close):
    """Test behaviour if a close match, but enforcing zero tolerance"""
    metric = MetricsSegmentation.SegmentationRecall(tolerance=0.0)
    recall = metric(reference, hypothesis_close)
    npt.assert_almost_equal(recall, 0.25, decimal=3)


def test_recall_early_ends(reference, hypothesis_early_ends):
    """Test when the hypothesis segments end early (no impact, as we base change on segment starts)"""
    metric = MetricsSegmentation.SegmentationRecall()
    recall = metric(reference, hypothesis_early_ends)
    assert recall == 1.0


def test_recall_late_starts(reference, hypothesis_late_starts):
    """Test when the hypothesis segments start late (has impact, as we base change on segment starts)"""
    metric = MetricsSegmentation.SegmentationRecall()
    recall = metric(reference, hypothesis_late_starts)
    npt.assert_almost_equal(recall, 0.25, decimal=3)


def test_recall_false_alarms(reference, hypothesis_false_alarms):
    """Test when the hypothesis as false alarms (inserted segments)"""
    metric = MetricsSegmentation.SegmentationRecall()
    recall = metric(reference, hypothesis_false_alarms)
    assert recall == 1.0


def test_recall_misses(reference, hypothesis_misses):
    """Test when the hypothesis as false alarms (inserted segments)"""
    metric = MetricsSegmentation.SegmentationRecall()
    recall = metric(reference, hypothesis_misses)
    npt.assert_almost_equal(recall, 0.75, decimal=3)


# Tests of precision function


def test_precision_perfect_match(reference, hypothesis_perfect):
    """Standard case where all the points match precisely"""
    metric = MetricsSegmentation.SegmentationPrecision()
    precision = metric(reference, hypothesis_perfect)
    assert precision == 1.0


def test_precision_gaps_within_speaker_ref(reference_gaps_within_speaker, hypothesis_perfect):
    """Test behaviour if reference has gaps between regions of same speaker (has no impact)"""
    metric = MetricsSegmentation.SegmentationPrecision()
    precision = metric(reference_gaps_within_speaker, hypothesis_perfect)
    assert precision == 1.0


def test_precision_gaps_within_speaker_hyp(reference, hypothesis_gaps_within_speaker):
    """Test behaviour if hypothesis has gaps between regions of same speaker (has an impact)"""
    metric = MetricsSegmentation.SegmentationPrecision()
    precision = metric(reference, hypothesis_gaps_within_speaker)
    npt.assert_almost_equal(precision, 0.666, decimal=3)


def test_precision_close_match_normal_tolerance(reference, hypothesis_close):
    """Test behaviour if a close match, all within tolerance"""
    metric = MetricsSegmentation.SegmentationPrecision(tolerance=0.5)
    precision = metric(reference, hypothesis_close)
    assert precision == 1.0


# def test_precision_close_match_normal_tolerance(reference, hypothesis_close):
#     """Test behaviour if a close match, but occasionally outside a low tolerance"""
#     metric = MetricsSegmentation.SegmentationPrecision(tolerance=0.1)
#     precision = metric(reference, hypothesis_close)
#     npt.assert_almost_equal(precision, 0.5, decimal=3)


def test_precision_close_match_zero_tolerance(reference, hypothesis_close):
    """Test behaviour if a close match, but enforcing zero tolerance"""
    metric = MetricsSegmentation.SegmentationPrecision(tolerance=0.0)
    precision = metric(reference, hypothesis_close)
    npt.assert_almost_equal(precision, 0.25, decimal=3)


def test_precision_early_ends(reference, hypothesis_early_ends):
    """Test when the hypothesis segments end early (no impact, as we base change on segment starts)"""
    metric = MetricsSegmentation.SegmentationPrecision()
    precision = metric(reference, hypothesis_early_ends)
    assert precision == 1.0


def test_precision_late_starts(reference, hypothesis_late_starts):
    """Test when the hypothesis segments start late (has impact, as we base change on segment starts)"""
    metric = MetricsSegmentation.SegmentationPrecision()
    precision = metric(reference, hypothesis_late_starts)
    assert precision == 0.25


def test_precision_false_alarms(reference, hypothesis_false_alarms):
    """Test when the hypothesis as false alarms (inserted segments)"""
    metric = MetricsSegmentation.SegmentationPrecision()
    precision = metric(reference, hypothesis_false_alarms)
    npt.assert_almost_equal(precision, 0.57, decimal=3)


def test_precision_misses(reference, hypothesis_misses):
    """Test when the hypothesis as false alarms (inserted segments)"""
    metric = MetricsSegmentation.SegmentationPrecision()
    precision = metric(reference, hypothesis_misses)
    assert precision == 1.0
