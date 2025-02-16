# MockApi
This project implements a API mocking server using Django, SQLite, and Docker.

## Setup
1. Clone the repo
```
git clone https://github.com/katiyarhrithik/mockapi.git
cd mockapi
```
2. Install requirements
```
pip install -r requirements.txt
```
3. Run Migrations
```
python mange.py migrate
```
4. Create admin user
```
python manage.py createsuperuser --username admin --email admin@example.com
```
5. Make the `entrypoint.sh` file executable
```
chmod +x entrypoint.sh
```
6. Start the server using docker-compose
```
docker-compose build
docker-compose up
```

## Usage
1. Open Django Admin page. Go to `http://127.0.0.1:8000/admin/` and Log in with your credentials. <img width="487" alt="image" src="https://github.com/user-attachments/assets/ee6c9fac-4615-4e6c-8dcc-35883749e5c0" />
<img width="1231" alt="image" src="https://github.com/user-attachments/assets/051dbbd5-6aa6-4f92-8e1a-2f46295eb186" />
2. Create new Endpoints to mock in `Endpoints` section
<img width="1239" alt="image" src="https://github.com/user-attachments/assets/e6911ee7-7341-40ee-b140-a6a6f4187163" />
<img width="1248" alt="image" src="https://github.com/user-attachments/assets/bc020410-4417-43eb-9cf7-0e36231632b4" />
3. Now, Call the mocked endpoints with the given methods
<img width="557" alt="image" src="https://github.com/user-attachments/assets/13412c3b-cd65-457e-b98f-78ed4a2b3e4b" />
4. Usage of the endpoints can be viewd in `Endpoint usages` section
<img width="1258" alt="image" src="https://github.com/user-attachments/assets/c1ce05cd-95de-4e19-9ec1-d4d217de1524" />
5. Usage can also be viewed by calling `http://127.0.0.1:8000/usage/<endpoint>`
<img width="564" alt="image" src="https://github.com/user-attachments/assets/16edf7b5-4698-472a-9afc-4f009d86fea0" />

## Features
1. Custom endpoints can be mocked
2. Supports method mocking restriction(only the given methods will be allowed)
3. To disable method restriction, choose `Any` as the method. This will enable the endpoint to be called using any of the supported methods.
4. Supports status code mocking. The given status code will be returned in the response.
