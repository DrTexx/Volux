import pytest
import volux

# create Volux Operator object (hub for communication between modules)
vlx = volux.VoluxOperator()

class VoluxTestDemo(volux.VoluxDemo):
    def __init__(self,*args,**kwargs):
        super().__init__(
            demo_name="Test Demo",
            demo_method=self.run_demo,
            alias="demo",
        )

    def run_demo(self):

        print("I'm a demo!")

demo = VoluxTestDemo()

class Test_VoluxDemo:
    def test_run_demo(self):
        demo.run()
