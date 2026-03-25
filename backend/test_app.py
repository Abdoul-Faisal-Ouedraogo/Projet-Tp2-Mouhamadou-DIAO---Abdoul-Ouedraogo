# backend/test_app.py
from app import app

def test_app_exists():
    """Vérifie que l'application Flask est bien instanciée."""
    assert app is not None

def test_cors_enabled():
    """Vérifie que les CORS sont bien activés pour le frontend."""
    assert 'cors' in app.extensions