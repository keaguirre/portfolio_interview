from django.shortcuts import render, redirect
from .forms import CargarExcelForm
from .models import Precio, Portafolio
import pandas as pd

def excel_load(request):
    if request.method == 'POST':
        form = CargarExcelForm(request.POST, request.FILES)
        if form.is_valid():
            archivo = request.FILES['archivo']
            try:
                # Leer ambas hojas del Excel
                excel_data = pd.read_excel(archivo, sheet_name=['weights', 'Precios'])

                # Procesar hoja "weights" para el modelo Portafolio
                weights_df = excel_data['weights']
                for _, fila in weights_df.iterrows():
                    Portafolio.objects.create(
                        fecha=fila['Fecha'],
                        activos=fila['activos'],
                        portafolio_1=fila.get('portafolio 1'),
                        portafolio_2=fila.get('portafolio 2')
                    )

                # Procesar hoja "Precios" para el modelo Precio
                precios_df = excel_data['Precios']
                for _, fila in precios_df.iterrows():
                    Precio.objects.create(
                        dates=fila['Dates'],
                        eeuu=fila.get('EEUU'),
                        europa=fila.get('Europa'),
                        japon=fila.get('Japón'),
                        em_asia=fila.get('EM asia'),
                        latam=fila.get('Latam'),
                        high_yield=fila.get('High Yield'),
                        ig_corporate=fila.get('IG Corporate'),
                        emhc=fila.get('EMHC'),
                        latam_hy=fila.get('Latam HY'),
                        uk=fila.get('UK'),
                        asia_desarrollada=fila.get('Asia Desarrollada'),
                        emea=fila.get('EMEA'),
                        otros_rv=fila.get('Otros RV'),
                        tesoro=fila.get('Tesoro'),
                        mbs_cmbs_ambs=fila.get('MBS+CMBS+AMBS'),
                        abs=fila.get('ABS'),
                        mm_caja=fila.get('MM/Caja')
                    )

                return redirect('success')  # Cambia esto a tu vista de éxito o un mensaje
            except Exception as e:
                form.add_error(None, f'Error al procesar el archivo: {e}')
    else:
        form = CargarExcelForm()

    return render(request, 'excel_load_form.html', {'form': form})
