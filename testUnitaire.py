import pytest

# Assurez-vous que les fonctions est_nombre_parfait et liste_nombres_parfaits sont déjà définies

def test_est_nombre_parfait():
    # Tests pour les nombres parfaits
    assert est_nombre_parfait(6) == True
    assert est_nombre_parfait(28) == True
    assert est_nombre_parfait(496) == True
    assert est_nombre_parfait(8128) == True

    # Tests pour les nombres non parfaits
    assert est_nombre_parfait(1) == False
    assert est_nombre_parfait(10) == False
    assert est_nombre_parfait(100) == False
    assert est_nombre_parfait(12345) == False


def test_liste_nombres_parfaits():
    # Tests pour les listes générées
    assert liste_nombres_parfaits(1) == []
    assert liste_nombres_parfaits(6) == [6]
    assert liste_nombres_parfaits(30) == [6, 28]
    assert liste_nombres_parfaits(500) == [6, 28, 496]
    assert liste_nombres_parfaits(10000) == [6, 28, 496, 8128]


if __name__ == "__main__":
    pytest.main()
