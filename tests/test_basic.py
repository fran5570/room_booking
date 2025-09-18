from controllers import reservation_controller


def test_controller_module_loads():
    assert hasattr(reservation_controller, "__file__")
