Opis:
  Skrypt air_quality_fetcher.py pobiera dane o jakości powietrza (PM10 i PM2.5)
  z publicznego API GIOŚ, cyklicznie (domyślnie co 10 minut).
  Dane są normalizowane do formatu JSON, a następnie:
    - wysyłane do Apache Kafka (topic: air_quality_raw),
    - (opcjonalnie) zapisywane lokalnie do plików JSON w katalogu `data/`.

  Logi działania zapisywane są do pliku `fetcher.log`.

Wymagania:
  - Python 3.10 lub nowszy
  - Apache Kafka + Zookeeper (uruchamiane przez Docker Compose)
  - Docker Desktop

Instalacja:
  1. Stwórz środowisko wirtualne (opcjonalne, ale zalecane):
     python3 -m venv RTA
     source RTA/bin/activate

  2. Zainstaluj zależności:
     pip install -r requirements.txt

  3. Uruchom kontenery z Kafką:
     docker-compose up -d

Jak uruchomić (w terminalu):
  python air_quality_fetcher.py

  Skrypt działa w pętli – pobiera dane, wysyła do Kafka, zapisuje lokalnie
  i powtarza co X minut (domyślnie 10 minut).

Sprawdzenie działania (opcjonalnie):
  Otwórz (kolejny) terminal z konsumentem Kafka, by obserwować dane:
    docker exec -it kafka kafka-console-consumer \
      --bootstrap-server localhost:9092 \
      --topic air_quality_raw \
      --from-beginning

Wyłączenie:
  - w terminalach:
        ctrl + C
  - w katalogu z docker-compose.yml:
        docker-compose down
  - (opcjonalnie) wyłączenie środowiska venv
        deactivate



Dane wejściowe:
  - API GIOŚ (otwarte, bez autoryzacji)
  - Lista stacji i sensorów PM10/PM2.5

Dane wyjściowe:
  - JSON (Kafka topic: air_quality_raw)
  - JSON (lokalnie w ./data/...)
  - Logi: ./fetcher.log

Konfiguracja (przez zmienne środowiskowe – opcjonalnie):
  - GIOS_STATION_IDS       – lista ID stacji (domyślnie: 400,401)
  - FETCH_INTERVAL_MIN     – interwał pobierania w minutach (domyślnie: 10)
  - OUTPUT_DIR             – folder na pliki JSON (domyślnie: ./data)

Dodatkowe pliki:
  - docker-compose.yml     – uruchamia Kafka + Zookeeper
  - kafka_producer.py      – moduł odpowiedzialny za wysyłkę danych do Kafka
