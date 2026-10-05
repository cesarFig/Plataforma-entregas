from django.http import HttpResponse, JsonResponse
from .reglas import elegir_medio


def hola(request):
    return HttpResponse("Hola. Plataforma de entregas (aún sin pedidos).")


def estado(request):
    return JsonResponse({
        "servicio": "entregas",
        "version": 1,
        "medios_disponibles": ["camioneta", "moto", "bicicleta", "dron"],
    })



def cotizar_entrega(request):
    km_str = request.GET.get("km")
    kg_str = request.GET.get("kg")

    if km_str is None or kg_str is None:
        return JsonResponse({"error": "Faltan los parámetros km o kg"}, status=400)

    try:
        km = float(km_str)
        kg = float(kg_str)
        if km < 0 or kg < 0:
            raise ValueError("Los valores no pueden ser negativos")
    except ValueError:
        return JsonResponse({"error": "km y kg deben ser números válidos y positivos"}, status=400)

    medio, motivo = elegir_medio(km, kg)

    return JsonResponse({
        "km": km,
        "kg": kg,
        "medio": medio,
        "motivo": motivo
    })