from pytest import approx
from water_flow import *

def test_water_column_height():
    assert water_column_height(30.0, 12.0) == approx(36.0)
    assert water_column_height(0.0, 10.0) == approx(5.0)
    assert water_column_height(5.0, 0.0) == approx(5.0)

def test_pressure_gain_from_water_height():
    assert pressure_gain_from_water_height(0.0) == approx(0.0)
    assert pressure_gain_from_water_height(30.0) == approx(2942.0, abs=1)
    assert pressure_gain_from_water_height(50.0) == approx(4903.0, abs=1)

def test_pressure_loss_from_pipe():
    assert pressure_loss_from_pipe(0.048, 200.0, 0.018, 1.75) == approx(-96.6, abs=0.5)
    assert pressure_loss_from_pipe(0.048, 0.0, 0.018, 1.75) == approx(0.0)
    assert pressure_loss_from_pipe(0.048, 100.0, 0.018, 0.0) == approx(0.0)

def test_pressure_loss_from_fittings():
    assert pressure_loss_from_fittings(1.75, 0) == approx(0.0)
    assert pressure_loss_from_fittings(1.75, 2) == approx(-12.2, abs=0.5)
    assert pressure_loss_from_fittings(1.65, 4) == approx(-21.7, abs=0.5)

def test_reynolds_number():
    assert reynolds_number(0.048, 1.75) == approx(83725.8, abs=100)
    assert reynolds_number(0.05, 2.0) == approx(99783.4, abs=100)
    assert reynolds_number(0.1, 1.0) == approx(99660.0, abs=100)

def test_pressure_loss_from_pipe_reduction():
    rn = reynolds_number(0.28687, 1.65)
    loss = pressure_loss_from_pipe_reduction(0.28687, 1.65, rn, 0.048692)
    assert loss == approx(-81.2, abs=1)

def test_kpa_to_psi():
    assert kpa_to_psi(0.0) == approx(0.0)
    assert kpa_to_psi(100.0) == approx(14.5038, abs=0.01)
    assert kpa_to_psi(200.0) == approx(29.0076, abs=0.01)

if __name__ == "__main__":
    import pytest
    pytest.main(["-v", "--tb=line", "-rN", __file__])
