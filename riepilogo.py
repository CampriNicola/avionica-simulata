registro_apparati = {}

def crea_riepilogo(apparati: dict) -> dict:
    riepilogo = {
        "apparati": len(apparati),
        "OK": 0,
        "ATTENZIONE": 0,
        "OFFLINE": 0
    }

    for apparato in apparati:
        riepilogo[apparato["stato"]] += 1

    return riepilogo

