"""1. Queremos implementar una clase para gestionar un juego de Pokemon con las siguientes
características:
- Los atributos base que manejaremos serán código, nombre y tipo
- Sólo trabajaremos con pokemon de primera generación por lo que el código estará entre el
1 y el 151, ambos incluidos
- Los posibles tipos son Normal, Agua, Fuego, Planta, Volador, Lucha, Veneno, Eléctrico,
Tierra, Roca, Psíquico, Hielo, Bicho, Fantasma y Dragón.
- Cada pokemon debe de ser de un tipo pero podría ser de dos. Nunca mas
- No necesitamos setters (ya que un pokemon una vez creado no puede modificar sus
características) pero si getters apropiados para todas ellas
- Además, crearemos un método que se llame evolución que permitirá que un pokemon
evolucione en otro diferente. Para ello si un pokemon puede evolucionar en otro debe de
tener de alguna forma una referencia al pokemon en el que evoluciona.
2. Queremos implementar una clase para gestionar nuestra colección de mangas con las
siguientes características:
- Por cada manga guardaremos el nombre del mangaka (autor) el título de la colección (en
japonés, obligatorio y en español, opcional), el género prinicpal (shonen, shojo, seinen, josei,
kodomo, yuri, spokon, isekai y hentai) y el último número publicado en la colección. Crea
getters para todos ellos y setter para el título en castellano (por si originalmente no lo
sabemos y luego lo queremos añadir) y para el número por el que va la colección.
- Queremos, además, poder actualizar los números que tenemos y saber que números nos
faltan. Para ello crearemos dos métodos: uno que nos permitirá introducir los números que
vamos comprando (permitiendo una entrada variable de argumentos para cuando
compramos mas de uno a la vez) y otro que nos diga que números nos faltan para completar
la colección.
- Si cuando introducimos los números que compramos resulta que ya tenemos alguno de
ellos repetido debería de advertirnos
- También necesitaremos un método que nos permita eliminar un número (lo hemos perdido,
etc.). Si tratamos de eliminar un número que no tenemos debería de advertírsenos"""

"""1"""
# ===============================
# Clase Pokemon
# ===============================
class Pokemon:
    TIPOS_VALIDOS = ["Normal", "Agua", "Fuego", "Planta", "Volador", "Lucha",
                     "Veneno", "Eléctrico", "Tierra", "Roca", "Psíquico",
                     "Hielo", "Bicho", "Fantasma", "Dragón"]

    def __init__(self, codigo, nombre, tipos, evolucion=None):
        # Validación del código
        if codigo < 1 or codigo > 151:
            raise ValueError("Código fuera del rango 1-151")
        self.codigo = codigo
        self.nombre = nombre

        # Validación de tipos
        if isinstance(tipos, str):
            tipos = [tipos]
        if len(tipos) > 2:
            raise ValueError("Un pokemon solo puede tener como máximo 2 tipos")
        for t in tipos:
            if t not in Pokemon.TIPOS_VALIDOS:
                raise ValueError(f"Tipo '{t}' no válido")
        self.tipos = tipos

        # Evolución (referencia a otro Pokemon)
        self.evolucion_pokemon = evolucion

    # Getters
    def get_codigo(self):
        return self.codigo

    def get_nombre(self):
        return self.nombre

    def get_tipos(self):
        return self.tipos

    def get_evolucion(self):
        return self.evolucion_pokemon

    # Método de evolución
    def evolucion(self):
        if self.evolucion_pokemon:
            print(f"{self.nombre} evoluciona a {self.evolucion_pokemon.get_nombre()}")
            return self.evolucion_pokemon
        else:
            print(f"{self.nombre} no tiene evolución")
            return None

    # Representación
    def __str__(self):
        return f"{self.nombre} (Código: {self.codigo}, Tipos: {', '.join(self.tipos)})"

# ===============================
# EJEMPLO DE USO
# ===============================
# Bulbasaur solo es tipo Planta
bulbasaur = Pokemon(1, "Bulbasaur", "Planta")

# Ivysaur será Planta y Veneno
ivysaur = Pokemon(2, "Ivysaur", ["Planta", "Veneno"])
bulbasaur.evolucion_pokemon = ivysaur

print(bulbasaur)  # Bulbasaur (Código: 1, Tipos: Planta)
print(ivysaur)    # Ivysaur (Código: 2, Tipos: Planta, Veneno)

# Evolucionamos
nuevo_pokemon = bulbasaur.evolucion()
print(nuevo_pokemon)


"""2"""
# ===============================
# Clase Manga
# ===============================
class Manga:
    GENEROS_VALIDOS = ["shonen", "shojo", "seinen", "josei", "kodomo", "yuri", "spokon", "isekai", "hentai"]

    def __init__(self, autor, titulo_jap, genero, ultimo_num, titulo_es=None):
        self.autor = autor
        self.titulo_jap = titulo_jap
        self.titulo_es = titulo_es
        if genero not in Manga.GENEROS_VALIDOS:
            raise ValueError("Género no válido")
        self.genero = genero
        self.ultimo_num = ultimo_num
        self.numeros_comprados = set()  # para almacenar números adquiridos

    # Getters
    def get_autor(self):
        return self.autor

    def get_titulo_jap(self):
        return self.titulo_jap

    def get_titulo_es(self):
        return self.titulo_es

    def get_genero(self):
        return self.genero

    def get_ultimo_num(self):
        return self.ultimo_num

    # Setters
    def set_titulo_es(self, titulo):
        self.titulo_es = titulo

    def set_ultimo_num(self, num):
        self.ultimo_num = num

    # Método para añadir números comprados (acepta varios)
    def añadir_numeros(self, *numeros):
        for num in numeros:
            if num in self.numeros_comprados:
                print(f"Advertencia: Ya tienes el número {num}")
            else:
                self.numeros_comprados.add(num)

    # Método para eliminar un número
    def eliminar_numero(self, num):
        if num in self.numeros_comprados:
            self.numeros_comprados.remove(num)
            print(f"Número {num} eliminado.")
        else:
            print(f"No tienes el número {num} para eliminar.")

    # Método para mostrar números faltantes
    def numeros_faltantes(self):
        faltantes = []
        for i in range(1, self.ultimo_num + 1):
            if i not in self.numeros_comprados:
                faltantes.append(i)
        return faltantes

    # Representación
    def mostrar_info(self):
        print(f"Manga: {self.titulo_jap} ({self.titulo_es if self.titulo_es else 'Sin título español'})")
        print(f"Autor: {self.autor}, Género: {self.genero}, Último número: {self.ultimo_num}")
        print(f"Números comprados: {sorted(self.numeros_comprados)}")
        print(f"Números faltantes: {self.numeros_faltantes()}\n")

# ===============================
# EJEMPLO DE USO
# ===============================
manga1 = Manga("Eiichiro Oda", "One Piece", "shonen", 5)
manga1.añadir_numeros(1, 2, 3)
manga1.mostrar_info()

# Intentar añadir un número repetido
manga1.añadir_numeros(2, 4)
manga1.mostrar_info()

# Eliminar un número
manga1.eliminar_numero(3)
manga1.eliminar_numero(10)  # número que no existe
manga1.mostrar_info()
