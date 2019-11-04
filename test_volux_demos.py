import pytest
import volux

class Test_volux_demos:
    def test_import_demos(self):
        from volux import demos

    def test_messed_up_path(self):
        with pytest.raises(ModuleNotFoundError):
            import demos
