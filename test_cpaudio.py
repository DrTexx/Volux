import cpaudio
import pytest
from time import sleep

# create a mixer class
mc = cpaudio.MixerController()

# store volume before tests
_volume_before_tests = mc.gvol()
_mute_before_tests = mc.gmute()

class Test_cpaudio():
    def test_svol(self):
        mc.svol(2)
        assert mc.gvol() == 2
        mc.svol(98)
        assert mc.gvol() == 98
    def test_svol_TypeErrors(self):
        with pytest.raises(TypeError):
            mc.svol(4.5) # no decimals
        with pytest.raises(TypeError):
            mc.svol("30") # no strings
    def test_svol_ValueErrors(self):
        with pytest.raises(ValueError):
            mc.svol(101) # too high
        with pytest.raises(ValueError):
            mc.svol(-2) # too low
    def test_smute(self):
        mc.smute(True)
        assert mc.gmute() == 1
        mc.smute(False)
        assert mc.gmute() == 0
        mc.smute(1)
        assert mc.gmute() == 1
        mc.smute(0)
        assert mc.gmute() == 0
    def test_smute_TypeErrors(self):
        with pytest.raises(TypeError):
            mc.smute("True")
        with pytest.raises(TypeError):
            mc.smute(2)
        with pytest.raises(TypeError):
            mc.smute(-1)
        with pytest.raises(TypeError):
            mc.smute(0.5)
        with pytest.raises(TypeError):
            mc.smute(1.1)
    def test_vol_reset(self):
        print(mc.gvol())
        mc.svol(_volume_before_tests)
        print(mc.gvol())
        assert mc.gvol() == _volume_before_tests
    def test_mute_reset(self):
        print(mc.gmute())
        mc.smute(_mute_before_tests)
        print(mc.gmute())
        assert mc.gmute() == _mute_before_tests

#    def test_submessages(self):
#        assert "parent message | sub-message" in dpm(3,"parent message","sub-message",return_string=True)

tcpa = Test_cpaudio()
tcpa.test_vol_reset()
tcpa.test_mute_reset()
print("end of tests")

