from swiplserver import PrologMQI, PrologThread

with PrologMQI() as mqi:
    with mqi.create_thread() as main_prolog_thread:
        mpt = main_prolog_thread

        mpt.query(f"A=4.")
