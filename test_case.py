import requests
import math

#API для подключения к БД
api = 'https://test.tspb.su/test-task'


#Инициализируем объект Транспорт
class Vehicle:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.model = data['model']
        self.year = data['year']
        self.color = data['color']
        self.price = data['price']
        self.latitude = data['latitude']
        self.longitude = data['longitude']

    #Представление объекта ввиде строки
    def __str__(self):
        return f"<Vehicle: {self.name} {self.model} {self.year} {self.color} {self.price}>"


#Инициализируем класс для работы с API
class VehicleManager:
    def __init__(self, base_url):
        self.base_url = base_url

    #Метод GET для получения списка всех автомобилей
    def get_vehicles(self):
        url = f"{self.base_url}/vehicles"
        response = requests.get(url)
        data = response.json()
        vehicle_list = []
        for item in data:
            vehicle = Vehicle(item)
            vehicle_list.append(str(vehicle))
        return vehicle_list

    #Метод GET для получения автомобилей через перданные get параметры
    def filter_vehicles(self, params=None):
        if params is None:
            params = {}
        url = f"{self.base_url}/vehicles/"
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
        except requests.exceptions.HTTPError as err:
            print(f"HTTP Error: {err}")
            return []
        except requests.exceptions.JSONDecodeError as err:
            print(f"JSON Decode Error: {err}")
            return []

        filtered_vehicles = [Vehicle(item) for item in data]
        return filtered_vehicles

    #Метод GET для получения определенного автомобиля по его идентификатору
    def get_vehicle(self, vehicle_id):
        url = f"{self.base_url}/vehicles/{vehicle_id}"
        response = requests.get(url)
        data = response.json()
        vehicle_data = {
            "id": data['id'],
            "name": data['name'],
            "model": data['model'],
            "year": data['year'],
            "color": data['color'],
            "price": data['price'],
            "latitude": data['latitude'],
            "longitude": data['longitude']
        }
        return Vehicle(vehicle_data)

    #Метод POST для cоздания автомобиля
    def add_vehicle(self, name=None, model=None, year=None, color=None, price=None, latitude=None, longitude=None):
        url = f"{self.base_url}/vehicles"
        vehicle_data = {
            'name': name,
            'model': model,
            'year': year,
            'color': color,
            'price': price,
            'latitude': latitude,
            'longitude': longitude
        }
        response = requests.post(url, json=vehicle_data)
        data = response.json()
        return Vehicle(data)

    #Метод PUT для обновления данных автомобиля
    def update_vehicle(self, vehicle_id, name=None, model=None, year=None, color=None, price=None, latitude=None, longitude=None):
        url = f"{self.base_url}/vehicles/{vehicle_id}"
        update_data = {}
        if name is not None:
            update_data['name'] = name
        if model is not None:
            update_data['model'] = model
        if year is not None:
            update_data['year'] = year
        if color is not None:
            update_data['color'] = color
        if price is not None:
            update_data['price'] = price
        if latitude is not None:
            update_data['latitude'] = latitude
        if longitude is not None:
            update_data['longitude'] = longitude

        response = requests.put(url, json=update_data)
        data = response.json()
        return Vehicle(data)

    #Метод DELETE для удаления автомобиля
    def delete_vehicle(self, vehicle_id):
        url = f"{self.base_url}/vehicles/{vehicle_id}"
        response = requests.delete(url)
        data = response.json()
        return Vehicle(data)

    #Метод GET для полуения расстояния между двумя автомобилями
    def get_distance(self, id1, id2):
        vehicle1 = self.get_vehicle(id1)
        vehicle2 = self.get_vehicle(id2)
        distance = self._calculate_distance_between_points(vehicle1.latitude, vehicle1.longitude, vehicle2.latitude, vehicle2.longitude)
        return distance

    # Метод GET для нахождения ближайшего автомобиля к автомобилю, идентификатор которого был передан
    def get_nearest_vehicle(self, id):
        target_vehicle = self._get_vehicle_data(id)
        vehicles = self._get_vehicles_data()

        vehicle_min_distance = vehicles[0]
        min_distance = self.get_distance(id, vehicle_min_distance['id'])

        for vehicle_index in range(len(vehicles)):
            if vehicles[vehicle_index]['id'] == target_vehicle['id']:
                continue
            distance = self.get_distance(id, vehicles[vehicle_index]['id'])
            if distance < min_distance:
                min_distance = distance
                vehicle_min_distance = self._get_vehicle_data(vehicles[vehicle_index]['id'])

        return Vehicle(vehicle_min_distance)

    #Функция расчёта дистанции между двумя автомобилями
    def _calculate_distance_between_points(self, lat1, lon1, lat2, lon2):
        R = 6371000
        lat1_rad = math.radians(lat1)
        lon1_rad = math.radians(lon1)
        lat2_rad = math.radians(lat2)
        lon2_rad = math.radians(lon2)
        d_lat = lat2_rad - lat1_rad
        d_lon = lon2_rad - lon1_rad
        a = math.sin(d_lat / 2) ** 2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(d_lon / 2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distance = R * c
        return distance

    #Метод, который возращает список словарей данных об автомобилях
    def _get_vehicles_data(self):
        url = f"{self.base_url}/vehicels"
        response = requests.get(url)
        data = response.json()
        return data

    #Метод, который возращает данные об авомобиле ввиде словаря
    def _get_vehicle_data(self, vehicle_id):
        url = f"{self.base_url}/vehicles/{vehicle_id}"
        response = requests.get(url)
        data = response.json()
        return data


manager = VehicleManager(base_url=api)
print(manager.get_vehicles())
print(manager.filter_vehicles(params={"name": "Toyota"}))





