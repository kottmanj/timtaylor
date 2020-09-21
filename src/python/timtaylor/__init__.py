error = None
try:
    import tequila as tq
    from .example import run_example
except Exception as E:
    error = E


def show_me():
    if error is None:
        tq.show_available_simulators()
        tq.show_available_optimizers()
    else:
        print("did not work out")
        print(error)


