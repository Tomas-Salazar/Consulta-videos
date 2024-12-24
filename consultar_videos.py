class Video:
    def __init__(self, nombre, visualizaciones, reparto):
        """
        Inicializa una nueva instancia de la clase Video
        Este método es el constructor de la clase. Se llama automáticamente cuando se crea un nuevo objeto Video
        
        Recibe como parámetros nombre, visualización y reparto de cada video
        
        Devuelve un objeto Video con sus atributos y métodos
        """
        self.nombre = nombre
        self.visualizaciones = visualizaciones
        self.reparto = reparto
        
    def obtener_info(self):
        """
        Devuelve un tupla con la información del video (objeto instanciado)
        """
        return self.nombre, self.visualizaciones, self.reparto


class Serie(Video):
    def __init__(self, nombre, visualizaciones, reparto, n_temporadas):
        """
        Inicializa una nueva instancia de la clase Serie.
        Ésta clase hereda de Video y añade características específicas de series
        
        Recibe como parámetros nombre, visualización, reparto y n_temporadas, el número de temporadas de la serie
        
        Devuelve un objeto Serie con sus atributos y métodos, incluídos los heredados
        """
        # Se asignan características heredadas y propias
        super().__init__(nombre, visualizaciones, reparto)
        self.n_temporadas = n_temporadas
    
    def obtener_info(self):
        info_padre = super().obtener_info()     # En info_padre se almacenan las características heredadas del padre
        return info_padre + (self.n_temporadas,)    # Se concatenan tuplas para conservar el tipo de dato


class Pelicula(Video):
    def __init__(self, nombre, visualizaciones, reparto, duracion):
        """
        Inicializa una nueva instancia de la clase Película
        Ésta clase hereda de Video y añade características específicas de películas
        
        Recibe como parámetros nombre, visualización, reparto y duracion, la duración en minutos de la película
        
        Devuelve un objeto Pelicula con sus atributos y métodos, incluídos los heredados
        """
        # Se asignan características heredadas y propias
        super().__init__(nombre, visualizaciones, reparto)
        self.duracion = duracion
    
    def obtener_info(self):
        info_padre = super().obtener_info()     # En info_padre se almacenan las características heredadas del padre
        return info_padre + (self.duracion,)    # Se concatenan tuplas para conservar el tipo de dato


def obtener_video_mas_visto(lista_videos):
    """
    Función que itera la lista de videos, para ver cuál tiene la mayor visualización
    
    Recibe como parámetro la lista de los videos a iterar con dicho atributo
    
    Imprime por pantalla el resultado de la búsqueda
    """
    max_visualizaciones = 0
    mayores_vistas = None
    
    for video in lista_videos:
        if video.visualizaciones > max_visualizaciones:
            max_visualizaciones = video.visualizaciones
            mayores_vistas = video.nombre
        
    print(f'El video con mayor visualización fue: "{mayores_vistas}" con un total de {max_visualizaciones} de vistas.\n')


def obtener_promedio_duraciones(lista_videos):
    """
    Función que itera la lista de videos, para sumar el total de duraciones(si es que existe ese atributo) y así luego evaluar el promedio
    
    Recibe como parámetro la lista de los videos a iterar
    
    Imprime por pantalla el resultado de la búsqueda
    """
    total_duraciones = 0
    i = 0
    
    for video in lista_videos:
        try:    # Se utiliza bloque try en lugar de if ya que con el if si no puede acceder a la propiedad video.duración arroja un error detiendo el código.
            total_duraciones += video.duracion
            i += 1
        except:
            print(f'No hay información sobre la duración de {video.nombre}.')
            
    promedio_duraciones = total_duraciones / i
    
    print(f'El promedio de duración de las películas es de {round(promedio_duraciones, 2)} minutos.\n')


def obtener_actores_series_y_peliculas(lista_videos):
    """
    Función que itera la lista de videos, para evaluar qué actores trabajan tanto en series como en películas
    Para ello debe antes filtrar cuáles son repartos de películas y cuáles de series, obteniendo valores únicos para cada lista y luego viendo si se cruzan datos
    
    Recibe como parámetro la lista de los videos a iterar con dicho atributo
    
    Imprime por pantalla el resultado de la búsqueda
    """
    actores_peliculas = []
    actores_series = []
    
    # Se evalúa si es una serie o una película
    for video in lista_videos:
        if isinstance(video, Pelicula):
            actores_peliculas.extend(video.reparto)     # Se utiliza extend() debido a que se necesitan insertar valores de a uno, tratándose de una lista a otra
        elif isinstance(video, Serie):
            actores_series.extend(video.reparto)
        else:
            print(f'El video "{video.nombre}" no es ni una película ni una serie conocida.')
    
    # Se conservan valores únicos (sin duplicados)
    actores_peliculas_unicos = list(set(actores_peliculas))
    actores_series_unicos = list(set(actores_series))
    
    actores_series_y_peliculas = []
    
    # Se evalúa si los actores de las películas trabajaron en alguna serie
    for actor in actores_peliculas_unicos:
        if actor in actores_series_unicos:
            actores_series_y_peliculas.append(actor)
    
    print(f'Los actores que trabajan tanto en series como en películas son los siguientes:')
    print(', '.join(actores_series_y_peliculas))     # Muestra la lista en un único string
    print()     # Para dejar un salto de línea al finalizar


def obtener_series_mas_3_temp(lista_videos):
    """
    Función que itera la lista de videos, para buscar aquellos videos que posean más de 3 temporadas
    
    Recibe como parámetro la lista de los videos a iterar
    
    Imprime por pantalla el resultado de la búsqueda
    """
    series_mas_3_temp = []
    
    for video in lista_videos:
        try:    # Se utiliza bloque try debido a que si no puede acceder a dicha propiedad arroja error
            if video.n_temporadas > 3:
                series_mas_3_temp.append(video.nombre)
        except:
            print(f'No hay información sobre la cantidad de temporadas de {video.nombre}.')
    
    if series_mas_3_temp:       # Esto es para evaluar si existen o no series con más de 3 temporadas
        print(f'Las series que poseen más de 3 temporadas son las siguientes:')
        print(', '.join(series_mas_3_temp))     # Muestra la lista en un único string
    else:
        print('No se encontraron series con más de 3 temporadas.')
    print()     # Para dejar un salto de línea al finalizar


def mostrar_menu():     # Se agrega ésta función par auna mejor legibilidad del código
    menu = """
Seleccione la opción que quiera realizar:
Opción 1: Conocer video más visto
Opción 2: Conocer duración promedio de películas
Opción 3: Conocer qué actores participaron en series y películas
Opción 4: Conocer series extensas
Opción 5: Ver las cuatro opciones juntas
Opción 6: Salir
"""
    print(menu)


def main():
    # Registro de los repartos de cada video
    reparto_peaky = ['Cillian Murphy', 'Paul Anderson', 'Helen McCrory']
    reparto_umbrella = ['Tom Hopper', 'Emmy Raver-Lampman', 'Ellen Page', 'David Castañeda']
    reparto_inception = ['Leonardo DiCaprio', 'Ellen Page', 'Joseph Gordon-Levitt']
    reparto_batman = ['Christian Bale', 'Cillian Murphy', 'Michael Caine']
    reparto_inmortales = ['Mirtha Legrand', 'Leonardo DiCaprio', 'Elizabeth Segunda']
    
    # Instanciación de cada objeto
    peaky = Serie('Peaky Blinders', 1234567, reparto_peaky, 5)
    umbrella = Serie('The Umbrella Academy', 2434908, reparto_umbrella, 2)
    inception = Pelicula('Inception', 4760183, reparto_inception, 148)
    batman = Pelicula('Batman Begins', 17319533, reparto_batman, 140)
    inmortales = Pelicula('Inmortales', 35, reparto_inmortales, 30)
    
    # Se añaden los objetos a una lista para poder iterarla
    lista_videos = [peaky, umbrella, inception, batman, inmortales]
    
    opcion = None
    while not opcion:
        mostrar_menu()
        
        # Ingreso de opción por parte del usuario
        try:        # El try evalúa únicamente que el valor pueda convertirse a int, si es numérico pero no está en opciones, vuelve a pedir nueva opción
            opcion = int(input('Opción: '))
        except ValueError:
            print('Elija una opción disponible.') 
            opcion = None
            continue
        
        # Menú de opciones
        if opcion == 1:
            # Video más visto
            obtener_video_mas_visto(lista_videos)
            
        elif opcion == 2:
            # Promedio de duraciones
            obtener_promedio_duraciones(lista_videos)
            
        elif opcion == 3:
            # Lista de actores para cada película
            obtener_actores_series_y_peliculas(lista_videos)
            
        elif opcion == 4:
            # Lista de series extensas
            obtener_series_mas_3_temp(lista_videos)
            
        elif opcion == 5:
            # Selecciona todas las opciones a la vez
            obtener_video_mas_visto(lista_videos)
            obtener_promedio_duraciones(lista_videos)
            obtener_actores_series_y_peliculas(lista_videos)
            obtener_series_mas_3_temp(lista_videos)
            
        elif opcion == 6:
            # Salida del programa sin utilizar exit() (1)
            print('Usted ha finalizado la ejecución.\n¡Hasta pronto!\n')
            break
            
        else:
            print('Elija una opción disponible.')       # Ataja cualquier otra respuesta que no esté dentro de las opciones
            opcion = None
            continue
        
        # Consulta de confirmación de continuidad al usuario
        continuar = None
        while not continuar:
            continuar = input('¿Desea continuar? Responda si o no: ').lower().strip()
            if continuar == 'no':
                # Salida del programa sin utilizar exit() (2)
                print('Usted ha finalizado la ejecución.\n¡Hasta pronto!\n')
            elif continuar == 'si':
                opcion = None
            else:
                print('Intente escribir sólamente si o no.\n')      # Atrapa respuestas que no sean derivados de si o no
                continuar = None

# Evita ejecución del script automática al importar el módulo
if __name__ == '__main__':
    main()