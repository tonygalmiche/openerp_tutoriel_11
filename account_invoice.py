# -*- coding: utf-8 -*-

from osv import osv
from osv import fields
from tools.translate import _  #Permet de faire les traductions avec la fonction _()


class account_invoice(osv.osv):

  # Surcharge par héritage du modèle account.invoice
  _name = "account.invoice"
  _inherit = 'account.invoice'

  # Change l'ordre de tri par défaut -> Date de facture décroissant
  _order = "date_invoice desc"

account_invoice()


# Remarque : Cette méthode permet de modifier l'ordre de tri par défaut pour toutes les listes utilisant ce modèle
# il n'existe pas dans OpenEPR d'options pour avoir plusieurs ordre de tris pour un même modèle
# -> http://forum.openerp.com/forum/topic28677.html

