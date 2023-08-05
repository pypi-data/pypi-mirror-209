import os

import pytest
from pyannote.core import Segment

from aladdin.diarization.metrics.sm_diarisation_metrics import cookbook


def get_resources_dir():
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), "resources")


def test_get_word_level_metrics_for_files():
    lab_file_path = os.path.join(get_resources_dir(), "20050111_totn_03.lab")
    json_file_path = os.path.join(get_resources_dir(), "20050111_totn_03.json")
    result = cookbook.get_word_level_metrics_for_files(lab_file_path, json_file_path)
    assert result[0] == pytest.approx(0.21654545454545454)
    assert result[1] == pytest.approx(5500)
    assert len(result[2]) == 5500
    assert result[3] == pytest.approx(0.02563636363636363)


def test_get_segmentation_metrics_for_files():
    lab_file_path = os.path.join(get_resources_dir(), "20050111_totn_03.lab")
    json_file_path = os.path.join(get_resources_dir(), "20050111_totn_03.json")
    result = cookbook.get_segmentation_metrics_for_files(lab_file_path, json_file_path)
    assert result == (
        pytest.approx(0.9662614257524555),
        pytest.approx(0.879760257660641),
        pytest.approx(0.75),
        pytest.approx(0.4891304347826087),
    )


def test_get_segmentation_metrics_for_files_gaps_in_hyp():
    """Check that having gaps within speaker in the hypothesis has no impact on the segmentation result"""
    ref_file_path = os.path.join(get_resources_dir(), "20050111_totn_03_short.lab")
    hyp_file_path = os.path.join(get_resources_dir(), "20050111_totn_03_short_gaps.lab")
    result = cookbook.get_segmentation_metrics_for_files(ref_file_path, hyp_file_path)
    assert result == (pytest.approx(1.0), pytest.approx(1.0), pytest.approx(1.0), pytest.approx(1.0))


def test_get_segmentation_metrics_for_files_gaps_in_ref():
    """Check that having gaps within speaker in the reference has no impact on the segmentation result"""
    ref_file_path = os.path.join(get_resources_dir(), "20050111_totn_03_short_gaps.lab")
    hyp_file_path = os.path.join(get_resources_dir(), "20050111_totn_03_short.lab")
    result = cookbook.get_segmentation_metrics_for_files(ref_file_path, hyp_file_path)
    assert result == (pytest.approx(1.0), pytest.approx(1.0), pytest.approx(1.0), pytest.approx(1.0))


def test_get_segmentation_metrics_for_files_low_tolerance():
    lab_file_path = os.path.join(get_resources_dir(), "20050111_totn_03.lab")
    json_file_path = os.path.join(get_resources_dir(), "20050111_totn_03.json")
    result = cookbook.get_segmentation_metrics_for_files(lab_file_path, json_file_path, tolerance=0.5)
    assert result == (
        pytest.approx(0.9922999988634685),
        pytest.approx(0.8796469933058293),
        pytest.approx(0.6666666666666666),
        pytest.approx(0.43478260869565216),
    )


def test_get_der_component_details_for_files():
    lab_file_path = os.path.join(get_resources_dir(), "20050111_totn_03.lab")
    json_file_path = os.path.join(get_resources_dir(), "20050111_totn_03.json")
    result = cookbook.get_der_component_details_for_files(lab_file_path, json_file_path)
    assert result == (
        pytest.approx(0.21784572761903773),
        pytest.approx(0.010463089648752132),
        pytest.approx(0.029441987476085042),
        pytest.approx(0.17794065049420055),
    )


def test_get_jaccard_error_rate_for_files():
    lab_file_path = os.path.join(get_resources_dir(), "20050111_totn_03.lab")
    json_file_path = os.path.join(get_resources_dir(), "20050111_totn_03.json")
    result = cookbook.get_jaccard_error_rate_for_files(lab_file_path, json_file_path)
    assert result == pytest.approx(0.422112267283915)


def test_get_speaker_count_metrics_for_files():
    lab_file_path = os.path.join(get_resources_dir(), "20050111_totn_03.lab")
    json_file_path = os.path.join(get_resources_dir(), "20050111_totn_03.json")
    result = cookbook.get_speaker_count_metrics_for_files(lab_file_path, json_file_path)
    assert result == (pytest.approx(8.0), pytest.approx(13.0))


def test_get_data_set_results():
    ref_dbl = os.path.join(get_resources_dir(), "ref.dbl")
    hyp_dbl = os.path.join(get_resources_dir(), "hyp.dbl")
    dbl_root = get_resources_dir()
    overall_results, file_results = cookbook.get_data_set_results(ref_dbl, hyp_dbl, dbl_root=dbl_root)

    print(overall_results)

    # Check at least we have the expected number of file results
    assert len(file_results) == 2

    # Check overall values meet expectations, within a certain level of precision
    abs_approx = 0.001
    assert overall_results["total_audio_duration"] == pytest.approx(1829.34, abs=abs_approx)
    assert overall_results["total_ref_duration"] == pytest.approx(1768.43, abs=abs_approx)
    assert overall_results["total_hyp_duration"] == pytest.approx(1734.20, abs=abs_approx)
    assert overall_results["audio_labelled"] == pytest.approx(0.948, abs=abs_approx)
    assert overall_results["ref_labelled"] == pytest.approx(0.981, abs=abs_approx)
    assert overall_results["average_der"] == pytest.approx(0.217, abs=abs_approx)
    assert overall_results["average_jer"] == pytest.approx(0.422, abs=abs_approx)
    assert overall_results["average_confusion"] == pytest.approx(0.177, abs=abs_approx)
    assert overall_results["average_insertion"] == pytest.approx(0.010, abs=abs_approx)
    assert overall_results["average_deletion"] == pytest.approx(0.030, abs=abs_approx)
    assert overall_results["average_diarisation_coverage"] == pytest.approx(0.833, abs=abs_approx)
    assert overall_results["average_diarisation_purity"] == pytest.approx(0.973, abs=abs_approx)
    assert overall_results["average_segmentation_coverage"] == pytest.approx(0.880, abs=abs_approx)
    assert overall_results["average_segmentation_purity"] == pytest.approx(0.966, abs=abs_approx)
    assert overall_results["average_segmentation_f1"] == pytest.approx(0.593, abs=abs_approx)
    assert overall_results["average_segmentation_precision"] == pytest.approx(0.751, abs=abs_approx)
    assert overall_results["average_segmentation_recall"] == pytest.approx(0.490, abs=abs_approx)
    assert overall_results["average_word_der"] == pytest.approx(0.216, abs=abs_approx)
    assert overall_results["average_speaker_uu_percentage"] == pytest.approx(0.075, abs=abs_approx)
    assert overall_results["average_nspeakers_ref"] == pytest.approx(5.5, abs=abs_approx)
    assert overall_results["average_nspeakers_hyp"] == pytest.approx(7.5, abs=abs_approx)
    assert overall_results["average_nspeakers_discrepancy"] == pytest.approx(2.0, abs=abs_approx)
    assert overall_results["average_nspeakers_abs_discrepancy"] == pytest.approx(3.0, abs=abs_approx)
    assert overall_results["rate_nspeakers_correct"] == pytest.approx(0.0, abs=abs_approx)
    assert overall_results["rate_nspeakers_plus_one"] == pytest.approx(0.0, abs=abs_approx)
    assert overall_results["rate_nspeakers_plus_many"] == pytest.approx(0.5, abs=abs_approx)
    assert overall_results["rate_nspeakers_minus_one"] == pytest.approx(0.5, abs=abs_approx)
    assert overall_results["rate_nspeakers_minus_many"] == pytest.approx(0.0, abs=abs_approx)
    assert overall_results["rate_single_speaker_issue"] == pytest.approx(0.0, abs=abs_approx)


def test_json_to_annotation_sm_v2_format():
    example_json_path = os.path.join(get_resources_dir(), "example_sm_v2.json")
    annotation = cookbook.json_to_annotation(example_json_path)
    assert list(annotation.itersegments()) == [
        Segment(0, 1.8),
        Segment(2, 3.8),
        Segment(10, 11.0),
        Segment(20, 20.8),
        Segment(22, 22.8),
    ]


def test_json_to_annotation_reference_format():
    example_json_path = os.path.join(get_resources_dir(), "example_reference.json")
    annotation = cookbook.json_to_annotation(example_json_path)
    assert list(annotation.itersegments()) == [
        Segment(0, 1.8),
        Segment(2, 3.8),
        Segment(10, 11.0),
        Segment(20, 20.8),
        Segment(21, 21.8),
        Segment(22, 22.8),
    ]
