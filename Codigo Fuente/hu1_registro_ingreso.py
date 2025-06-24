# HU1 - Registro de ingreso

def registrar_ingreso(usuario_id):
    from datetime import datetime
    hora_actual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"Usuario {usuario_id} ingresó a las {hora_actual}")
