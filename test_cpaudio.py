import cpaudio
import pytest

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
            mc.svol(4.5) # no floats
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
    def test_smute_TypeErrors(self):
        with pytest.raises(TypeError):
            mc.smute(0)
        with pytest.raises(TypeError):
            mc.smute(1)
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

class test_cpaudio_platforms():
    def __init__(self):
        
        import cpaudio.Platforms.Windows as cpaudio_windows
        import cpaudio.Platforms.Darwin as cpaudio_darwin
        import cpaudio.Platforms.Linux as cpaudio_linux
        
        self.cpaudio_windows = cpaudio_windows
        self.cpaudio_darwin = cpaudio_darwin
        self.cpaudio_linux = cpaudio_linux
        
        self.cpaudio_all_platforms = [self.cpaudio_windows,
                                      self.cpaudio_darwin,
                                      self.cpaudio_linux]
        
        self.universal_classes = ['MixerController']
        self.MixerController_methods = ['svol','gvol','smute','gmute']
        
    def test_classes(self):
        
        assert self.universal_classes in dir(self.cpaudio_windows)
        assert self.universal_classes in dir(self.cpaudio_darwin)
        assert self.universal_classes in dir(self.cpaudio_linux)
        
    def test_mixer_functions(self):
        
        MixerController_windows = self.cpaudio_windows.MixerController()
        MixerController_darwin = self.cpaudio_windows.MixerController()
        MixerController_linux = self.cpaudio_windows.MixerController()
        
        for m in self.MixerController_methods:
            assert m in dir(MixerController_windows)
            assert m in dir(MixerController_darwin)
            assert m in dir(MixerController_linux)

#    def test_submessages(self):
#        assert "parent message | sub-message" in dpm(3,"parent message","sub-message",return_string=True)

#test_cpaudio_platforms().test_classes()
#test_cpaudio_platforms().test_mixer_functions()

print("end of tests")
