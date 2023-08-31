"""Dado un conjunto de puntos en un plano cartesiano, 
se te pide encontrar los dos puntos más cercanos entre sí. 
Implementa una función llamada pares_cercanos que tome una lista de coordenadas (puntos en el plano)
y devuelva las coordenadas de los dos puntos más cercanos junto con su distancia. 
Utiliza el algoritmo "Divide y Vencerás" para resolver 
este problema de manera eficiente, este ejercicio deberá usar Decoradores, como args y kwargs."""
import math

# Metodo para calculad la distancia euclidiana entre dos puntos 
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Decorador para ordenar los puntos por coordenada x e y
def closest_pairs_decorator(func):
    def wrapper(*args):
        points_sorted_by_x = sorted(args[0], key=lambda point: point[0])
        points_sorted_by_y = sorted(args[0], key=lambda point: point[1])
        
        return func(points_sorted_by_x, points_sorted_by_y)
    return wrapper

# Función principal para encontrar los pares de puntos más cercanos
@closest_pairs_decorator
def find_closest_pairs(points_sorted_by_x, points_sorted_by_y):
    # Caso base: si hay pocos puntos, se usa fuerza bruta
    if len(points_sorted_by_x) <= 3:
        return brute_force(points_sorted_by_x)
    
    # Divide los puntos en dos mitades y obtiene el punto medio
    mid = len(points_sorted_by_x) // 2
    mid_point = points_sorted_by_x[mid]

    # Divide los puntos en las mitades izquierda y derecha según las coordenadas x
    points_left_x = points_sorted_by_x[:mid]
    points_right_x = points_sorted_by_x[mid:]

    # Filtra los puntos para obtener las mitades izquierda y derecha según las coordenadas y
    points_left_y = [p for p in points_sorted_by_y if p in points_left_x]
    points_right_y = [p for p in points_sorted_by_y if p in points_right_x]

    # Resuelve recursivamente para las mitades izquierda y derecha
    left_distance, left_p1, left_p2 = find_closest_pairs(points_left_x, points_left_y)
    right_distance, right_p1, right_p2 = find_closest_pairs(points_right_x, points_right_y)
    min_distance = min(left_distance, right_distance)

    # Encuentra los puntos cerca del punto medio
    points_near_mid = [p for p in points_sorted_by_y if abs(p[0] - mid_point[0]) < min_distance]

    # Resuelve para los puntos cercanos al punto medio usando fuerza bruta
    mid_distance, min_p1, min_p2 = brute_force(points_near_mid, min_distance)
    
    # Compara la distancia mínima entre las dos mitades y cerca del punto medio
    if mid_distance < min_distance:
        return mid_distance, min_p1, min_p2
    else:
        return min_distance, left_p1, left_p2

# Fuerza bruta para encontrar el par más cercano entre un conjunto pequeño de puntos
def brute_force(points, limit=float('inf')):
    
    min_dist = limit
    min_p1 = None
    min_p2 = None
    
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dist = distance(points[i], points[j])
            if dist < min_dist:
                min_dist = dist
                min_p1 = points[i]
                min_p2 = points[j]
    
    return min_dist, min_p1, min_p2

# Ejecucion
coordinates_list = [(1, 2), (4, 6), (8, 12), (3, 7), (10, 5)]
min_distance, point1, point2 = find_closest_pairs(coordinates_list)
print(f"Los puntos cercanos son {point1} y {point2}, con una distancia de {min_distance}")


