def registrar_salida(usuario_id):
    from datetime import datetime
    hora_actual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"Usuario {usuario_id} salió a las {hora_actual}")
