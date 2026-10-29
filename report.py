registro_apparati = {}

def filtra_per_stato(apparati: dict, stato: str) -> list:

    stato_foramt = stato.upper()

    result = []
    for apparato in apparati:
        if apparato["stato"] == stato_foramt:
            result.Append(apparato)

    return result

def filtra_per_bus(apparati: dict, bus: str) -> list:
    result = []
    for apparato in apparati:
        if apparato["bus"] == bus:
            result.append(apparato)

    return result
