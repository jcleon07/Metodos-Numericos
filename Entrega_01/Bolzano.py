import numpy as np
import sympy as sp
import matplotlib.pyplot as plt



 # ---------------      Funcion y tabla       -------------------------

def bolzano(function,a,b,iterations):
    if function(a)*function(b) >= 0:
        print("No se puede encontrar la raiz en el intervalo")
        return None
    
    #Se imprime una tabla con (a,b,c,f(c))
    print("\n{:<10} {:<15} {:<15} {:<15} {:<15}".format("Iteración", "a", "b", "c", "f(c)"))
    print("-" * 70)

    for i in range(iterations+1):
        c = (a+b)/2
        fc = function(c)

        #Se imprime una tabla con los valores actuales de cada iteracion
        print("{:<10} {:<15.8f} {:<15.8f} {:<15.8f} {:<15.8f}".format(i, a, b, c, fc))

        if fc == 0.0:
            print("La raiz es:", c)
            return c
        elif fc*function(a) < 0:
            b = c
        else:
            a = c

    return (a+b)/2



 # ---------------      Entrada usuario e impresion del resultado       -------------------------

if __name__ == "__main__":
    #Definimos la variable x
    x = sp.Symbol('x')

    # Input del usuario como cadena
    fun = input("Ingrese la función (ejemplo: x**3 - 5): ")

    try:
        # Convertir la entrada en una expresión simbólica (SymPy)
        expr = sp.sympify(fun)

        # Convertir a función numérica usando lambdify (usa numpy internamente)
        mi_funcion = sp.lambdify(x, expr, modules=["numpy"])

        #Definir el intervalo [a,b] y el numero de iteraciones deseadas
        a = float(input("Ingrese el valor de a: "))
        b = float(input("Ingrese el valor de b: "))
        iterations = int(input("Ingrese el numero de iteraciones: "))

        #Variable que almacena el resultado de la funcion
        resultado = bolzano(mi_funcion, a, b, iterations)
        
        #Se imprime el resultado final despues de las iteraciones
        print("\nLa raíz aproximada después de", iterations, "iteraciones es:", resultado)



 # ---------------      Grafica       -------------------------


        #Grafica
        x_graphic = np.linspace(a, b, 400)
        y_graphic = mi_funcion(x_graphic)  # Evalúa la función ingresada por el usuario en cada punto de x_graphic

        #Raiz
        plt.scatter(resultado,0, color='red',label = 'Punto de corte')

        #Personalizacion grafica 
        plt.axhline(0, color='black', linewidth=0.5)  # eje x
        plt.plot(x_graphic, y_graphic, label=f'f(x) = {expr}')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.title('Gráfica de la función')
        plt.grid(True)
        plt.legend()
        plt.show()

    # Manejo de errores
    except ValueError:
        print("Entrada invalida. Por favor ingrese numeros validos.")   
    except Exception as e:
        print("Ocurrio un error:", e) 
     
