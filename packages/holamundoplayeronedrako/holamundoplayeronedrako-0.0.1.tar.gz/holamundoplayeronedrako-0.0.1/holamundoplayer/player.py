"""
Este es el modulo que incluye la clase de reproductor de música
"""

class Player:
    """
    Esta clase crea un reproductor de música
    """
    def play(self, song):
        """
        Reproduce la canción que recibió como parametro

        Parameters:
        song (str): Este es un string con el path de la canción a reproducir

        Returns:
        int: Devuelve 1 si reproduce con éxito en caso contrario devuelve 0
        """
        print("reproduciendo cancion")

    def stop(self):
        """
        Detiene la reproducción de la canción
        """
        print("deteniendo cancion")