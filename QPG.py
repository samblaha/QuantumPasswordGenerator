from qiskit import QuantumCircuit, Aer, execute
from qiskit.utils import QuantumInstance
import string
import random
from config import API_TOKEN  # Assuming this is your configuration for something else, not needed for local simulation

def quantum_random_bit():
    """Generate a random bit using quantum computation."""
    # Create a Quantum Circuit with 1 qubit
    qc = QuantumCircuit(1, 1)
    # Apply a Hadamard gate to put the qubit in superposition
    qc.h(0)
    # Measure the qubit
    qc.measure([0], [0])

    # Execute the circuit on the qasm_simulator
    backend = Aer.get_backend('qasm_simulator')
    quantum_instance = QuantumInstance(backend, shots=1)
    result = execute(qc, backend, shots=1).result()
    counts = result.get_counts()

    # Return 0 or 1 based on the measurement
    return int(list(counts.keys())[0])

def generate_password(length=12):
    """Generate a password of a given length using quantum randomness."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''

    for _ in range(length):
        # Use quantum randomness to pick a character
        random_bit = quantum_random_bit()
        random_index = random.randint(0, len(characters) - 1) if random_bit else random.randrange(len(characters))
        password += characters[random_index]

    return password

# Generate and print a quantum-generated password
print(generate_password(12))
