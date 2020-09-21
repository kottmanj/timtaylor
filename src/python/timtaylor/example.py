import tequila as tq

def run_example()
    
    mol = tq.chemistry.Molecule(geometry="he 0.0 0.0 0.0", basis_set="6-31G")
    U = mol.make_upccgsd_ansatz()
    H = mol.make_hamiltonian()
    E = tq.ExpectationValue(U=U, H=H)
    result = tq.minimize(method="bfgs", objective=E, gradient="2-point")

    message = "Small demo calculation"

    message_dict = {}
    message_dict["message"] = message
    message_dict["schema"] = "message"
    message_dict["energy"] = result.energy
    message_dict["iterations"] = len(result.history.extract_energies())
    message_dict["angles"] = result.angles

    with open("result.json",'w') as f:
        f.write(json.dumps(message_dict, indent=2)) # Write message to file as this will serve as output artifact
