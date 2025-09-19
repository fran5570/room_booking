# Sistema de Reserva de Salas

Este es un sistema de reservas de salas de reuniones, desarrollado con **Python**  bajo el paradigma de **Programación Orientada a Objetos (POO)** y utilizando el patrón de diseño **MVC (Modelo - Vista - Controlador)**.
---

## Funcionalidades principales

- Crear, listar y buscar usuarios.
- Crear y listar salas.
- Realizar reservas de salas con validación de solapamiento de horarios.
- Consultar reservas por usuario o por sala.
- Persistencia de datos con SQLite (también en Docker).



---

## Tecnologías utilizadas

- Python 3.12
- SQLite
- Docker (opcional)
- Docker Compose (opcional)

---

## ▶Ejecución local (sin Docker)

1. Asegurate de tener Python 3.12 instalado.
2. Cloná este repositorio
3. ejecuta:
python main.py

Ejecución con Docker Compose (opcional):
docker-compose run --rm reserva


##  Pipeline CI
El proyecto incluye un workflow en **GitHub Actions** (`.github/workflows/ci.yml`) que corre automáticamente en cada push/PR:
1. **Lint** → verificación de estilo con Ruff.  
2. **Tests** → ejecución de pruebas unitarias con pytest + cobertura.  
3. **Build** → generación de un ejecutable `.pyz` en la carpeta `dist/`.

##  Endpoint de Health Check
El servicio expone un endpoint de health en:
- python -m controllers.health_controller

## para correr los test localmente:
pytest -q --cov=.