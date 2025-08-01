"""Tests for the Modbus simulator."""
import time
import unittest
from unittest.mock import patch, MagicMock

from modbusim.simulator import ModbusSimulator


class TestModbusSimulator(unittest.TestCase):
    """Test cases for ModbusSimulator."""

    def setUp(self):
        """Set up test fixtures."""
        self.simulator = ModbusSimulator(
            mode="rtu", port="/dev/null", baudrate=9600, unit_id=1
        )
        # Mock the server to avoid starting a real server
        self.simulator.server = MagicMock()

    def test_set_values(self):
        """Test setting values in the simulator."""
        # Test setting coils
        self.simulator.set_values(0, [1, 0, 1, 0], "co")
        values = self.simulator.get_values(0, 4, "co")
        self.assertEqual(values, [1, 0, 1, 0])

        # Test setting holding registers
        self.simulator.set_values(0, [1234, 5678], "hr")
        values = self.simulator.get_values(0, 2, "hr")
        self.assertEqual(values, [1234, 5678])

    @patch("modbusim.simulator.StartSerialServer")
    def test_start_rtu_server(self, mock_server):
        """Test starting an RTU server."""
        self.simulator.start()
        self.assertTrue(self.simulator.running)
        mock_server.assert_called_once()

    @patch("modbusim.simulator.StartTcpServer")
    def test_start_tcp_server(self, mock_server):
        """Test starting a TCP server."""
        tcp_simulator = ModbusSimulator(mode="tcp", port="localhost")
        tcp_simulator.start()
        self.assertTrue(tcp_simulator.running)
        mock_server.assert_called_once()

    def test_stop_server(self):
        """Test stopping the server."""
        self.simulator.running = True
        self.simulator.server = MagicMock()
        self.simulator.stop()
        self.assertFalse(self.simulator.running)
        self.simulator.server.server_close.assert_called_once()

    def test_context_manager(self):
        """Test using the simulator as a context manager."""
        with patch.object(self.simulator, "start") as mock_start, patch.object(
            self.simulator, "stop"
        ) as mock_stop:
            with self.simulator:
                mock_start.assert_called_once()
            mock_stop.assert_called_once()


if __name__ == "__main__":
    unittest.main()
