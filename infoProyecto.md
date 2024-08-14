# fastapi

## *** Nota (El proyecto no esta terminado y subi lo que tenía. Sorry *** .)

Debido a:
1. Alto Rendimiento
2. Documentación Automática
3. Validación y Serialización de los datos
4. Seguridad y un largo etc.

## Instalación
1. pip install fastapi uvicorn 
2. pip install httpx pydantic 

#### Ejecución de la aplicación:

Dentro de la carpeta de la aplicación

3. uvicorn main:app --reload

### Probar la API:
Una vez que el servidor esté en funcionamiento, abre tu navegador y ve a http://127.0.0.1:8000/docs. Esto te llevará a la documentación automática generada por FastAPI, donde puedes probar el endpoint /github/{username} directamente.

## Relacíón de Archivos

Archivo | Descripción
--- | ---
| main.py | endpoint |  
| models.py | BaseModel |
| github_apy.py | Github integration file |
| metricas  ( Carpeta )|
| activity.py | Contribuciones en los últimos 6 meses |
| activiti_pattern.py | Alta Actividad |
| base.py | Interface de Metricas |
| languages.py | Los 3 lenguajes de programación más usados |
| pull_requests.py | 
 

