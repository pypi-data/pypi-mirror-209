""" Esta es la documentación de player"""

class Player:
    """
    Esta clase crea un reproductor de musica
    """

    def play(self, song):
        """
        Reproduce la cannción que recibio en el constructor
        Parametros:
        song (str): es un string con el path de la canción

        Returns:
        Int: devuelve 1 si fue exitoso, sino devuelve 0
        """
        print("Reproduciendo cancnión")

    def stop(self):
        print("Stopping")