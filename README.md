# Система управления автотранспортом

Это простое приложение на Python для управления данными об автотранспорте с использованием RESTful API.
Оно позволяет пользователям выполнять различные операции, такие как получение информации о транспортных средствах,
фильтрация автомобилей на основе определенных критериев, добавление новых автомобилей, обновление существующих данных о транспортных средствах и удаление автомобилей из базы данных.

# Предварительные требования

Перед запуском приложения убедитесь, что у вас установлены следующие компоненты:

  - Python 3.12.2
  - библиотека requests (можно установить с помощью pip install requests)

# Функциональность

- Класс Vehicle
- Класс Vehicle представляет собой одиночный объект транспортного средства и имеет следующие атрибуты:

   - id
   - name
   - model
   - year
   - color
   - price
   - latitude
   - longitude
   - Класс VehicleManager

- Класс VehicleManager предоставляет методы для взаимодействия с API:

   - get_vehicles(): Получить список всех транспортных средств.
   - filter_vehicles(params): Фильтрация транспортных средств на основе указанных параметров.
   - get_vehicle(vehicle_id): Получить информацию о конкретном транспортном средстве.
   - add_vehicle(): Добавить новое транспортное средство в базу данных.
   - update_vehicle(vehicle_id): Обновить информацию о существующем транспортном средстве.
   - delete_vehicle(vehicle_id): Удалить транспортное средство из базы данных.
   - get_distance(id1, id2): Рассчитать расстояние между двумя транспортными средствами.
   - get_nearest_vehicle(id): Найти ближайшее транспортное средство к указанному транспортному средству.
   - _calculate_distance_between_points(lat1, lon1, lat2, lon2): Рассчитать расстояние между двумя географическими точками.
   
# Примеры

python 
Copy code

manager = VehicleManager(base_url=api)

# Получить все транспортные средства
print(manager.get_vehicles())

# Фильтрация транспортных средств по названию
print(manager.filter_vehicles(params={"name": "Toyota"}))

# Добавить новое транспортное средство
new_vehicle = manager.add_vehicle(name="Toyota", model="Camry", year=2022, color="Black", price=25000, latitude=40.7128, longitude=74.0060) print(new_vehicle)

# Обновить существующее транспортное средство
updated_vehicle = manager.update_vehicle(vehicle_id=1, price=28000) print(updated_vehicle)

# Удалить транспортное средство
deleted_vehicle = manager.delete_vehicle(vehicle_id=1) print(deleted_vehicle)

# Рассчитать расстояние между двумя транспортными средствами
distance = manager.get_distance(id1=1, id2=2) print(f"Расстояние: {distance} метров")

# Найти ближайшее транспортное средство к указанному
nearest_vehicle = manager.get_nearest_vehicle(id=1) print(nearest_vehicle)
