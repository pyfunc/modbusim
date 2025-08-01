"""
Basic usage example for the ModbusIM package.

This script demonstrates how to use the ModbusIM package to create a Modbus RTU simulator
and interact with it programmatically.
"""
import time
from modbusim import ModbusSimulator
PORT1 = "/tmp/ptyp0"
PORT2 = "/dev/ttyACM0"

def main():
    """Run a basic Modbus RTU simulator with test values."""
    # Create a Modbus RTU simulator
    with ModbusSimulator(port=PORT1, baudrate=9600) as simulator:
        # Set some test values
        simulator.set_values(0, [1, 0, 1, 0], "co")  # Coils 0-3
        simulator.set_values(0, [1234, 5678, 9012], "hr")  # Holding Registers 0-2
        
        print("Modbus RTU simulator is running...")
        print("Test values set:")
        print(f"  - Coils 0-3: {simulator.get_values(0, 4, 'co')}")
        print(f"  - Holding Registers 0-2: {simulator.get_values(0, 3, 'hr')}")
        print("Press Ctrl+C to stop")
        
        # Keep the simulator running
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\nShutting down...")

if __name__ == "__main__":
    main()
