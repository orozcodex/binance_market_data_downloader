import requests
import csv
from datetime import datetime, timezone

def timestamp(date_str):
    """Convierte una fecha en formato string 'YYYY-mm-dd' a timestamp."""
    try:
        return int(datetime.strptime(date_str, "%Y-%m-%d").timestamp() * 1000)
    except ValueError:
        print("Formato de fecha incorrecto. Por favor, usa el formato YYYY-MM-DD.")
        exit()

def write_to_csv(writer, data):
    """Escribe los datos de mercado en el archivo CSV actual."""
    for line in data:
        # Convertir el tiempo de apertura y cierre a enteros antes de realizar operaciones
        market_data = [int(line[0]), line[1], line[2], line[3], line[4], line[5], int(line[6]), line[7], line[8], line[9], line[10], line[11]]
        writer.writerow(market_data)

# Solicitar al usuario el símbolo, fecha de inicio, fecha de fin y timeframe
symbol = input("Introduce el símbolo (ejemplo: BTCUSDT): ").upper()
interval = input("Introduce el timeframe (1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 3d, 1w, 1M): ")
start_date = input("Fecha de inicio (YYYY-MM-DD): ")
end_date = input("Fecha de fin (YYYY-MM-DD): ")

# Configuración inicial
url = "https://api.binance.com/api/v3/klines"

# Convertir fechas de inicio y fin a timestamp
start_ts = timestamp(start_date)
end_ts = timestamp(end_date)

current_year = None

try:
    while start_ts < end_ts:
        response = requests.get(url, params={"symbol": symbol, "interval": interval, "startTime": start_ts, "limit": 1000})
        data = response.json()

        if not data:
            print("No se encontraron más datos o hubo un error en la solicitud.")
            break

        for line in data:
            year = datetime.fromtimestamp(int(line[0]) / 1000, timezone.utc).year
            if year != current_year:
                if 'file' in locals():  # Cerrar el archivo anterior si existe
                    file.close()
                filename = f"{symbol}_{interval}_market_data_{year}.csv"
                file = open(filename, mode='w', newline='')
                writer = csv.writer(file)
                write_to_csv(writer, [data[0]])  # Escribir cabecera y primera línea
                current_year = year
            else:
                write_to_csv(writer, [line])  # Continuar escribiendo datos sin cabecera

        start_ts = data[-1][6] + 1
finally:
    if 'file' in locals():
        file.close()

print(f"Datos de mercado para {symbol} con timeframe {interval} guardados en archivos CSV por año seleccionado.")
