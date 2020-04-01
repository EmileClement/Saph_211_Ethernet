# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 15:10:16 2020

@author: Leopold
"""

#%% Element reels

class Domaine():
    def __init__(self, n_machine):
        """


        Parameters
        ----------
        n_machine : int
            nombre de machine sur le dommine

        Returns
        -------
        None.

        """
        self.time = 0
        self.machines = []
        self.etat = Etat_D_Libre()
        self.events = []

        for _ in range(n_machine):
            self.machines.append(Machine(self))

    def __repr__(self):
        """
        Representation d'un domaine

        Returns
        -------
        None.

        """
        C = """Domaine à t={} dans l'etat {}, avec:
    - {} machines,
    - {} evenement"""
        return C.format(self.time, len(self.machines), len(self.events))

    def reagir(self, event):
        #Permet d'exécuter un evenement
        for machine in self.machines:
            machine.reagir(event)
        N_etat = self.etat.reagir(event)
        if N_etat == None:
            pass
        elif isinstance(N_etat, Etat_Domaine):
            self.etat = N_etat
        else:
            raise ValueError

    def goto_next_event(self):
        self.events.sort()
        next_event = self.events.pop(0)
        return next_event

    def visiblement_libre(self):
        return self.etat.visiblement_libre()

    def reelement_libre(self):
        return self.etat.reelement_libre()

class Machine():
    def __init__(self, domaine):
        self.domaine = domaine
        self.etat = Etat_M_Idle()
        self.nombre_echec = 0
        self.longueur_msg = []

    def __repr__(self):
        C = """Machine {} """

    def reagir(self, event):
        N_etat = self.etat.reagir(event)
        if N_etat == None:
            pass
        elif isinstance(N_etat, Etat_Machine):
            self.etat = N_etat
        else:
            raise ValueError

    def parlante(self):
        return self.etat.parlant()

# %% Etat
class Etat():
    def init_E(self, domaine):
        self.temps_depart = domaine

    def etat_suivant(self, event):
        assert 0, "not implement"

class Etat_Domaine(Etat):
    def __init__(self, domaine):
        self.init_E(domaine)
        self.domaine = domaine
        self._visiblement_libre = True
        self._reelement_libre = True
        self._init_particulier()

    def visiblement_libre(self):
        return self._visiblement_libre

    def reelement_libre(self):
        return self._reelement_libre

    def _init_particulier(self):
        pass

class Etat_Machine(Etat):
    def init_M(self, machine, event_fin):
        self.machine = machine
        self.event_fin = event_fin
        self._parlant = False

    def parlant(self):
        return self._parlant

# %% Etat Domaine

class Etat_D_Libre(Etat_Domaine):
    pass

class Etat_D_Risque(Etat_Domaine):
    def _init_particulier(self):
        self._reelement_libre = False

class Etat_D_Occupe(Etat_Domaine):
    def _init_particulier(self):
        self._reelement_libre = False
        self._visiblement_libre = False

class Etat_D_Colision(Etat_Domaine):
    def _init_particulier(self):
        self._reelement_libre = False
        self._visiblement_libre = False
