from volux import dp_datatools

class TestDp_datatools():
    def test_clamp(self):
        assert dp_datatools.clamp(30,10,20) == 20
