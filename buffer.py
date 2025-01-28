def cargar_buffer(entrada, inicio, tamano_buffer):
    # If we've reached the end of input, return EOF
    if inicio >= len(entrada):
        return ['eof']
    
    # Extract the next buffer segment
    buffer = entrada[inicio:inicio + tamano_buffer]
    
    # If the buffer is smaller than the buffer size, append EOF
    if len(buffer) < tamano_buffer:
        buffer.append('eof')
    
    return buffer


def procesar_buffer(entrada, tamano_buffer):
    pos_entrada = 0
    lexema_parcial = []
    eof_encontrado = False
    buffer = []
    
    while True:
        # Cargar buffer si está vacío
        if not buffer:
            if lexema_parcial:
                # Calcular cuántos caracteres nuevos se necesitan
                needed = tamano_buffer - len(lexema_parcial)
                new_chars = entrada[pos_entrada : pos_entrada + needed]
                pos_entrada += len(new_chars)
                buffer = lexema_parcial + new_chars
                lexema_parcial = []
                # Añadir 'eof' si es necesario
                if len(buffer) < tamano_buffer and not eof_encontrado:
                    buffer.append('eof')
                    eof_encontrado = True
            else:
                # Cargar buffer normal
                buffer = entrada[pos_entrada : pos_entrada + tamano_buffer]
                pos_entrada += len(buffer)
                if len(buffer) < tamano_buffer and not eof_encontrado:
                    buffer.append('eof')
                    eof_encontrado = True
        
        # Procesar buffer
        inicio = 0
        avance = 0
        while avance < len(buffer):
            if buffer[avance] == ' ' or buffer[avance] == 'eof':
                if inicio != avance:
                    lexema = ''.join(buffer[inicio:avance])
                    print(f"Lexema procesado: {lexema}")
                if buffer[avance] == 'eof':
                    return
                inicio = avance + 1
            avance += 1
        
        # Guardar lexema parcial si hay
        if inicio < len(buffer):
            lexema_parcial = buffer[inicio:]
        else:
            lexema_parcial = []
        buffer = []

def main():
    entrada = list("Esto es un ejemplo de entrada con eof")
    tamano_buffer = 10
    procesar_buffer(entrada, tamano_buffer)

if __name__ == "__main__":
    main()
