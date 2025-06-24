# Análisis de Requerimientos (Historias de Usuario)

**Versión:** 1.1

| ID  | Historia de Usuario                                                                 | Criterios de Aceptación                                       |
|-----|--------------------------------------------------------------------------------------|----------------------------------------------------------------|
| HU1 | Como empleado, quiero registrar mi ingreso para que quede registrado mi horario.     | Botón de "Ingresar" visible y funcional. Registro con fecha/hora. |
| HU2 | Como empleado, quiero registrar mi salida para cerrar mi jornada laboral.            | Botón de "Salir". No debe poder marcar más de una vez por día.  |
| HU3 | Como RRHH, quiero ver un reporte mensual por empleado.                               | Filtrado por mes, exportación PDF/CSV.                         |
| HU4 | Como administrador, quiero poder editar registros manualmente en caso de error.      | Solo usuarios con permiso. Bitácora de cambios.                 |
| HU5 | Como sistema, quiero autenticar empleados mediante credenciales únicas.              | Login seguro JWT, expiración token.                            |
| HU6 | Como RRHH, quiero exportar datos a CSV para planillas.                               | Opción de exportación y descarga.                              |
| HU7 | Como RRHH, quiero estadísticas de horas trabajadas.                                  | Gráficos por empleado / mes.                                   |
| HU8 | Como RRHH, quiero filtrar reportes por período y usuario.                            | Selector de fechas y usuario.                                  |
| HU9 | Como PO, quiero pruebas de usabilidad documentadas.                                  | Informe de hallazgos.                                          |
| HU10| Como usuario, quiero un manual simple de uso.                                        | PDF descargable.                                               |
| HU11| Como admin, quiero optimizar la carga de datos.                                      | Tiempos de respuesta < 1 s.                                    |
| HU12| Como IT, quiero documentación técnica del API.                                      | Swagger ó similar.                                             |
