from qiskit import QuantumCircuit, Aer, execute
from qiskit.utils import QuantumInstance
import string
import random
import sys  # Import the sys module to access command-line arguments

def quantum_random_bit():
    """Generate a random bit using quantum computation."""
    qc = QuantumCircuit(1, 1)
    qc.h(0)
    qc.measure([0], [0])

    backend = Aer.get_backend('qasm_simulator')
    result = execute(qc, backend, shots=1).result()
    counts = result.get_counts()

    return int(list(counts.keys())[0])

def generate_password(length=12):
    """Generate a password of a given length using quantum randomness."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''

    for _ in range(length):
        random_bit = quantum_random_bit()
        random_index = random.randint(0, len(characters) - 1) if random_bit else random.randrange(len(characters))
        password += characters[random_index]

    return password

# Check if a command-line argument is provided for the password length
if len(sys.argv) > 1:
    try:
        length = int(sys.argv[1])
    except ValueError:
        print("Provided length argument is not a valid number. Using default length of 12.")
        length = 12
else:
    length = 12

# Generate and print a quantum-generated password using the specified or default length
print(generate_password(length))
