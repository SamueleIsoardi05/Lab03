from strumento import Strumento
from prestito import Prestito

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self.nome = nome
        self.responsabile = responsabile

        self.strumenti = []
        self.prestiti = []
        self._numeroPrestiti = 1#serve per generare i codici per i prestiti in maniera univoca

    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""
        # TODO
        lista_strumenti = []
        with open(file_path, 'r', encoding='utf-8') as csvfile:
            for row in csvfile:
                r=row.rstrip().split(',')
                strumento =Strumento(r[0], r[1], r[2], int(r[3]), float(r[4]))
                lista_strumenti.append(strumento)
        self.strumenti=lista_strumenti
        return lista_strumenti


    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        # TODO
        idNuovoStrumento=f"S{len(self.strumenti)+1}"
        nuovoStrumento = Strumento(idNuovoStrumento, tipo, marca, anno_acquisto,  valore)
        self.strumenti.append(nuovoStrumento)
        return nuovoStrumento

    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        # TODO
        strumentiOrdinati = sorted(self.strumenti, key=lambda strumento: strumento.marca.lower())
        return strumentiOrdinati

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        # TODO
        strumentoEsistente= False
        for s in self.strumenti:
            if s.id_strumento==id_strumento:#Controlla se lo strumento esiste
                strumentoEsistente = True
                break
        if not strumentoEsistente:
            raise Exception(f"errore, lo strumento richiesto non è presente nel sistema")
        for p in self.prestiti:
            if p.id_strumento==id_strumento:#Qui invece controlla se lo strumento è già in prestito
                raise Exception(f"lo strumento è già in prestito")


        id_nuovoPrestito = f"P{self._numeroPrestiti}"
        self._numeroPrestiti += 1  # Criterio necessario per creare il codice del prestito
        nuovoPrestito = Prestito(id_nuovoPrestito, data, id_strumento, cognome_allievo)
        self.prestiti.append(nuovoPrestito)
        return nuovoPrestito


    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        # TODO
        for p in self.prestiti:
            if p.id_prestito==id_prestito:
                self.prestiti.remove(p)
                return True
        raise Exception(f"non è stato trovato nessun prestito con questo codice: {id_prestito}")


