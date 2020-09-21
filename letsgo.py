import tequila as tq
import json

def run_example():
    
    U = tq.gates.Ry(angle="a", target=0)
    H = tq.paulis.X(0)
    E = tq.ExpectationValue(U=U, H=H)
    result = tq.minimize(method="bfgs", objective=E, gradient="2-point")

    message = "Small demo calculation"

    message_dict = {}
    message_dict["message"] = message
    message_dict["schema"] = "message"
    message_dict["energy"] = result.energy
    message_dict["iterations"] = len(result.history.extract_energies())
    message_dict["angles"] = {k.name:v for k,v in result.variables.items()}

    with open("result.json",'w') as f:
        f.write(json.dumps(message_dict, indent=2)) # Write message to file as this will serve as output artifact
