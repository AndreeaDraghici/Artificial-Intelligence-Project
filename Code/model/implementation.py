from Code.service.search import Problem
''' 
Author: Draghici Andreea
Date: 2021, June
'''

'''
    Specific faptul ca pentru rezolvarea problemei din tema de casa am folosit framework-ul de la 15-puzzle problem aferent platformei de laborator 5,
    adaptand, testand si gasind o euristica aferent potrivita implementarii acestui assigment.
'''


class m_Vehicle(Problem):
    """
       Functia init (self, parking_size, stare_initiala, stare_finala) este constructorul
       folosit pentru inițializarea problemei cu toate valorile de care avem nevoie.
    """

    def value(self, state):
        pass

    def __init__(self, parking_size, stare_initiala, stare_finala):
        """ Declaram starea obiectivului si starea initiala. """
        self.parking_size = parking_size  # dimensiunea parcarii
        self.initial = stare_initiala  # initial state
        self.goal = stare_finala  # goal state
        self.mutare_masina = -1  # indicele pozitiei fiecarui vehicul

        Problem.__init__(self, stare_initiala, stare_finala)

    def actions(self, stare):
        """
          Calculam urmatoare mutare a masinii iar, daca vehiculul dinainte a facut o miscare,
          pozitia vehicului va deveni 0 si va incepe din nou cu primul vehicul.
        """
        if self.mutare_masina == self.parking_size - 1:
            self.mutare_masina = 0  # pozitia vehicului devine 0 si va incepe din nou cu primul vehicul
        else:
            self.mutare_masina = self.mutare_masina + 1  # altfel trecem la pozitia urmatorului vehicul

        """ 
            Returnam actiunile care pot fi executate in starea data.
            Rezultatul este o lista, deoarece exista doar cinci actiuni posibile+salturile peste alte vehicule.
        """
        ListaActiunilorPosibile = ['SUS' + str(self.mutare_masina),
                                   # returneaza actiunea SUS si indicele pozitiei vehiculului
                                   'JOS' + str(self.mutare_masina),
                                   # returneaza actiunea JOS si indicele pozitiei vehiculului
                                   'STANGA' + str(self.mutare_masina),
                                   # returneaza actiunea STANGA si indicele pozitiei vehiculului
                                   'DREAPTA' + str(self.mutare_masina),
                                   # returneaza actiunea DREAPTA si indicele pozitiei vehiculului
                                   'STAY' + str(self.mutare_masina),
                                   # returneaza actiunea STAY si indicele pozitiei vehiculului
                                   'SARITURA STANGA' + str(self.mutare_masina),
                                   # returneaza actiunea SARITURA STANGA si indicele pozitiei vehiculului
                                   'SARITURA DREAPTA' + str(self.mutare_masina),
                                   # returneaza actiunea SARITURA DREAPTA si indicele pozitiei vehiculului
                                   'SARITURA INAINTE' + str(self.mutare_masina),
                                   # returneaza actiunea SARITURA INAINTE si indicele pozitiei vehiculului
                                   'SARITURA INAPOI' + str(
                                       self.mutare_masina)]  # returneaza actiunea SARITURA INAPOI si indicele pozitiei vehiculului

        locatia1 = stare[self.mutare_masina]  # locatia1 va lua valoarea indicelui pozitiei vehiculului
        """
           Verificam directiile pe care vehiculul nostru le poate realiza, conform parcarii. 
        """
        if locatia1 < self.parking_size:
            if 'SUS' + str(
                    self.mutare_masina) in ListaActiunilorPosibile:  # punem conditia daca pozitia actiunii noastre se afla in lista actiunilor posibile
                # convertim cu str ()  valoarea specificata in ListaActiunilorPosibile
                ListaActiunilorPosibile.remove(
                    'SUS' + str(self.mutare_masina))  # eliminam actiunea respectiva din lista de actiuni posibile
                # a.i vehiculul sa nu faca miscari in afara parcarii
        if locatia1 >= self.parking_size * (self.parking_size - 1):
            if 'JOS' + str(
                    self.mutare_masina) in ListaActiunilorPosibile:  # punem conditia daca pozitia actiunii noastre se afla in lista actiunilor posibile
                # convertim cu str ()  valoarea specificata in ListaActiunilorPosibile
                ListaActiunilorPosibile.remove(
                    'JOS' + str(self.mutare_masina))  # eliminam actiunea respectiva din lista de actiuni posibile
                # a.i vehiculul sa nu faca miscari in afara parcarii
        if locatia1 % self.parking_size == 0:
            if 'STANGA' + str(
                    self.mutare_masina) in ListaActiunilorPosibile:  # punem conditia daca pozitia actiunii noastre se afla in lista actiunilor posibile
                # convertim cu str ()  valoarea specificata in ListaActiunilorPosibile
                ListaActiunilorPosibile.remove(
                    'STANGA' + str(self.mutare_masina))  # eliminam actiunea respectiva din lista de actiuni posibile
                # a.i vehiculul sa nu faca miscari in afara parcarii
        if locatia1 % self.parking_size == self.parking_size - 1:
            if 'DREAPTA' + str(
                    self.mutare_masina) in ListaActiunilorPosibile:  # punem conditia daca pozitia actiunii noastre se afla in lista actiunilor posibile
                # convertim cu str ()  valoarea specificata in ListaActiunilorPosibile
                ListaActiunilorPosibile.remove(
                    'DREAPTA' + str(self.mutare_masina))  # eliminam actiunea respectiva din lista de actiuni posibile
                # a.i vehiculul sa nu faca miscari in afara parcarii
        if locatia1 % self.parking_size <= 1:
            if 'SARITURA STANGA' + str(
                    self.mutare_masina) in ListaActiunilorPosibile:  # punem conditia daca pozitia actiunii noastre se afla in lista actiunilor posibile
                # convertim cu str ()  valoarea specificata in ListaActiunilorPosibile
                ListaActiunilorPosibile.remove('SARITURA STANGA' + str(
                    self.mutare_masina))  # eliminam actiunea respectiva din lista de actiuni posibile
                # a.i vehiculul sa nu faca miscari in afara parcarii
        if locatia1 % self.parking_size >= self.parking_size - 2:
            if 'SARITURA DREAPTA' + str(
                    self.mutare_masina) in ListaActiunilorPosibile:  # punem conditia daca pozitia actiunii noastre se afla in lista actiunilor posibile
                # convertim cu str ()  valoarea specificata in ListaActiunilorPosibile
                ListaActiunilorPosibile.remove('SARITURA DREAPTA' + str(
                    self.mutare_masina))  # eliminam actiunea respectiva din lista de actiuni posibile
                # a.i vehiculul sa nu faca miscari in afara parcarii
        if locatia1 < 2 * self.parking_size:
            if 'SARITURA INAINTE' + str(
                    self.mutare_masina) in ListaActiunilorPosibile:  # punem conditia daca pozitia actiunii noastre se afla in lista actiunilor posibile
                # convertim cu str ()  valoarea specificata in ListaActiunilorPosibile
                ListaActiunilorPosibile.remove('SARITURA INAINTE' + str(
                    self.mutare_masina))  # eliminam actiunea respectiva din lista de actiuni posibile
                # a.i vehiculul sa nu faca miscari in afara parcarii
        if locatia1 > (self.parking_size * self.parking_size - 2 * self.parking_size - 1):
            if 'SARITURA INAPOI' + str(
                    self.mutare_masina) in ListaActiunilorPosibile:  # punem conditia daca pozitia actiunii noastre se afla in lista actiunilor posibile
                # convertim cu str ()  valoarea specificata in ListaActiunilorPosibile
                ListaActiunilorPosibile.remove('SARITURA INAPOI' + str(
                    self.mutare_masina))  # eliminam actiunea respectiva din lista de actiuni posibile
                # a.i vehiculul sa nu faca miscari in afara parcarii

        idx = 0  # idx poate fi privit ca un indice al starii vehiculului i
        # il folosesc pentru a cunoaste care dintre vehicule a facut o miscare
        """
           Verificam actiunile pe care le poate face vehiculul nostru, conform celorlalte vehicule.
           Eliminam anumite actiuni in functie de pozitia vehiculelor.
           Spre exemplu sa nu faca miscari in afara parcarii.  
        """
        while idx < self.parking_size:
            locatia2 = stare[
                idx]  # se schimba dupa fiecare miscare a vehicul, pentru a schimba toate pozițiile, precum și starile vehiculelor.

            #  locatia1  reprezinta pozitia vehicului i
            #  locatia2  reprezinta pozitia vehicului i+1
            #  verificam daca vehiculul actual poate face o miscare

            if idx != self.mutare_masina:
                if locatia1 - self.parking_size == locatia2 and 'SUS' + str(
                        self.mutare_masina) in ListaActiunilorPosibile:
                    ListaActiunilorPosibile.remove('SUS' + str(self.mutare_masina))

                if locatia1 + self.parking_size == locatia2 and 'JOS' + str(
                        self.mutare_masina) in ListaActiunilorPosibile:
                    ListaActiunilorPosibile.remove('JOS' + str(self.mutare_masina))

                if locatia1 - 1 == locatia2 and 'STANGA' + str(self.mutare_masina) in ListaActiunilorPosibile:
                    ListaActiunilorPosibile.remove('STANGA' + str(self.mutare_masina))

                if locatia1 + 1 == locatia2 and 'DREAPTA' + str(self.mutare_masina) in ListaActiunilorPosibile:
                    ListaActiunilorPosibile.remove('DREAPTA' + str(self.mutare_masina))

                if locatia1 - 2 == locatia2 and 'SARITURA STANGA' + str(self.mutare_masina) in ListaActiunilorPosibile:
                    ListaActiunilorPosibile.remove('SARITURA STANGA' + str(self.mutare_masina))

                if locatia1 + 2 == locatia2 and 'SARITURA DREAPTA' + str(self.mutare_masina) in ListaActiunilorPosibile:
                    ListaActiunilorPosibile.remove('SARITURA DREAPTA' + str(self.mutare_masina))

                if locatia1 - 2 * self.parking_size == locatia2 and 'SARITURA INAINTE' + str(
                        self.mutare_masina) in ListaActiunilorPosibile:
                    ListaActiunilorPosibile.remove('SARITURA INAINTE' + str(self.mutare_masina))

                if locatia1 + 2 * self.parking_size == locatia2 and 'SARITURA INAPOI' + str(
                        self.mutare_masina) in ListaActiunilorPosibile:
                    ListaActiunilorPosibile.remove('SARITURA INAPOI' + str(self.mutare_masina))
            idx += 1
        return ListaActiunilorPosibile  # returnam lista actiunilor posibile

    def result(self, stare, actiune):
        """
            Avand in vedere starea si actiunea, revenim la o noua stare care reprezinta rezultatul actiunii
            Actiunea se presupune ca este o actiune valida
        """
        locatia1 = stare[self.mutare_masina]  # pozitia vehicului i
        noua_stare = list(stare)  # noua_stare reprezinta rezultatul actiunii

        """ Exprimam delta ca actiune pe care o poate executa o masina """

        delta = {'SUS' + str(self.mutare_masina): -self.parking_size,
                 'JOS' + str(self.mutare_masina): +self.parking_size,
                 'STANGA' + str(self.mutare_masina): -1, 'DREAPTA' + str(self.mutare_masina): +1,
                 'STAY' + str(self.mutare_masina): +0, 'SARITURA STANGA' + str(self.mutare_masina): -2,
                 'SARITURA DREAPTA' + str(self.mutare_masina): +2,
                 'SARITURA INAINTE' + str(self.mutare_masina): -2 * self.parking_size,
                 'SARITURA INAPOI' + str(self.mutare_masina): +2 * self.parking_size}
        noua_stare[self.mutare_masina] = locatia1 + delta[actiune]  # stare noua va fi data de pozitia vehicului i
        # si de actiunea pe care o executa vehiculul
        return tuple(noua_stare)  # returnam rezultatul actiunii ca fiind un tuplu

    def goal_state(self, state):
        """ Avand o stare, returnam True daca starea este o stare a obiectivului sau False, altfel"""
        return state == self.goal

    def manhtDistance(self, node):
        """ Returneaza valoarea euristica pentru o anumita stare. Functia euristica implicita utilizata este
        h (n) = Distanta Manhattan """
        manhattanDistance = sum(abs(s - g) * 2 for (s, g) in zip(node.state, self.goal))
        return manhattanDistance
