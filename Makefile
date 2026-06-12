# Project Makefile

.PHONY: up down restart logs ps shell build

ENV_FILE=devops/env/local

help:
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

image: ## Build docker images
	docker compose -f docker-compose.local.yml build

up:  ## Make services up with main docker-compose file
	docker compose -f docker-compose.local.yml up -d

down: ## Make services down with main docker-compose file
	docker compose -f docker-compose.local.yml down

build-migrations: ## Create a new migration file revision (migration)
	docker exec -it edtech_local_django python manage.py makemigrations

migrate: ## Migrate to db change
	docker exec -it edtech_local_django python manage.py migrate ${module}

createsuperuser: ## create django superuse
	docker compose -f docker-compose.local.yml run --rm django python manage.py createsuperuser

restart: ## Make restart services
	make down && make up
 
logs: ## display logs
	docker compose -f docker-compose.local.yml logs

shell: ## Enter app shell 
	docker exec -it edtech_local_django /bin/bash

worker-shell: ## Enter worker shell
	docker compose exec celery bash

db-shell: ## Enter database shell
	docker exec -it edtech_local_postgres_data bash

generate-trans: ## Generate translation files
	docker-compose -f docker-compose.local.yml run django python manage.py makemessages --no-wrap --no-location --locale=ar

compile-trans: ## Compile translation files
	docker-compose -f docker-compose.local.yml run django python manage.py compilemessages --locale=ar