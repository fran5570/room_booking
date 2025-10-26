# 🏨 Sistema de Reserva de Salas

[![CI](https://github.com/fran5570/room_booking/actions/workflows/ci.yml/badge.svg)](https://github.com/fran5570/room_booking/actions)

Sistema de reservas de salas de reuniones, desarrollado con **Python** bajo el paradigma de **Programación Orientada a Objetos (POO)** y el patrón de diseño **MVC (Modelo - Vista - Controlador)**.  
Incluye **integración con Redis**, **API HTTP con endpoints de monitoreo**, y un **pipeline CI/CD automatizado con GitHub Actions**.

---

## Funcionalidades principales

- Crear, listar y buscar usuarios.  
- Crear y listar salas.  
- Realizar reservas de salas con validación de horarios.  
- Consultar reservas por usuario o sala.  
- Persistencia de datos con **SQLite** (soporte Docker).  
- Endpoints `/health`, `/get-responses` y `/clear-responses` integrados con **Redis**.  

################################################################################################################

## Tecnologías utilizadas

- **Python 3.12**  
- **SQLite**  
- **Redis (vía Docker)**  
- **Docker / Docker Compose**  
- **Pytest / Ruff / CodeQL**

#################################################################################################################

## ▶ Ejecución local (sin Docker)

1. Asegurate de tener **Python 3.12+** instalado.  
2. Cloná este repositorio:
```bash
git clone https://github.com/fran5570/room_booking.git
cd room_booking

3. Instalá las dependencias:
```bash
pip install -r requirements.txt


4. Ejecutá la aplicación principal:
```bash
python main.py


O levantá el servidor HTTP (modo endpoints REST):
python server.py


##################################################################################################################

5. Ejecución con Docker Compose

Asegurate de tener Docker Desktop en ejecución.

Iniciá los servicios:
```bash
docker-compose up -d


#####################################################################################################################


6. Pruebas automáticas:
```bash
pytest -q --cov=.


####################################################################################################################
El proyecto incluye tests para:

/health

/get-responses

/clear-responses

Persistencia y validación con Redis


Pipeline CI/CD (GitHub Actions)

El flujo automático (.github/workflows/ci.yml) ejecuta:

Lint: Verifica y corrige estilo con Ruff.

Test: Corre pytest con Redis activo en contenedor.

Build: Genera un paquete comprimido (room_booking.zip).

CodeQL: Analiza seguridad y vulnerabilidades del código.

###############################################################################################################
Artefactos generados

Después de cada ejecución del pipeline:

dist/room_booking.zip → Build comprimido del proyecto.

artifacts/coverage.xml → Reporte de cobertura.

artifacts/htmlcov/ → Reporte HTML navegable.
