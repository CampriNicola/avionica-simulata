



stati_ammessi = ("OK", "ATTENZIONE", "OFFLINE")

APPARATI = {
	"NAV-01": {"nome": "Ricevitore navigazione", "bus": "BUS-A", "stato": "OK"},
	"COM-02": {"nome": "Radio comunicazioni", "bus": "BUS-B", "stato": "ATTENZIONE"},
	"SEN-03": {"nome": "Sensore assetto", "bus": "BUS-A", "stato": "OFFLINE"},
}

apparati = APPARATI

def inserire_apparato(codice: str, nome: str, bus: str, stato: str) -> bool:

    stato_format = stato.upper() #Fixed problem

    if codice in apparati or stato_format not in stati_ammessi:
        return False

    apparati[codice] = {"nome": nome, "bus": bus, "stato": stato_format}
    return True

def aggiorna_stato(codice: str, stato: str) -> bool:
    stato_format = stato.upper() #Fixed problem

    if codice not in apparati or stato_format not in stati_ammessi:
        return False

    apparati[codice]["stato"] = stato_format
    return True

