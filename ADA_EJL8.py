def numdeSubarreglos(arr, k, threshold):
    # Condición mínima para que el promedio cumpla el umbral
    sum_req = k * threshold
    sum_act = sum(arr[:k])  # Suma inicial para la primera ventana
    cont = 0  # Contador de subarreglos válidos

    # Verificar la primera ventana
    if sum_act >= sum_req:
        cont += 1

    # Desplazar la ventana
    for i in range(k, len(arr)):
        # Actualizar la suma al mover la ventana
        sum_act += arr[i] - arr[i - k]
        # Verificar si la nueva suma cumple el umbral
        if sum_act >= sum_req:
            cont += 1

    return cont


arr = [2,2,2,2,5,5,5,8]
k = 3
threshold = 4
print("Para el arreglo:",arr)
print("Con k=",k,"y treshold =", threshold)
print("La salida es:",numdeSubarreglos(arr, k, threshold))  
