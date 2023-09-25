install:
	poetry install  #Устанавливаем Poetry


start: 
	poetry build # Команда для публикации проекта



publish:
	poetry publish --dry-run # Аргумент для отладки публикации, что бы не добавлять каталог в PyPl.


package-install:
	python3 -m pip install requests



package-force-reinstall:
	python3 -m pip install -force-reinstall dist/*.whl # Установка пакета операциолнной системы. Ее необходимо запускать из корневой директории проекта.


lint:
	poetry run flake8 brain_games


