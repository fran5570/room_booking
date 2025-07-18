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


