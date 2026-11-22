import pytest
import render.animation_layer_blend as mod

CASES = [
    ("weight_normalize", ([1.0, 0.2],)),
    ("second_based_transition", (0.2, 0.3)),
    ("root_motion_single", (1, 2)),
    ("event_dedup", (1, 2)),
    ("mirror_handle", (1, 2)),
    ("keyframe_preserve", (1, 2)),
    ("interrupt_fade", (0.1, 0.2)),
    ("sync_group", (1, 2)),
    ("lod_layer_match", (1, 2)),
    ("mask_bones", (1, 2)),
    ("layer_order", (1, 2)),
    ("additive_blend", (0.5, 0.5)),
    ("pose_snapshot", (1, 2)),
    ("transition_curve", (0.5, 1.0)),
    ("bone_mask", (1, 2)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
