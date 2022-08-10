.PHONY: init
init: compose.build compose.up

.PHONY: compose.build
compose.build:
	cd local/docker && docker-compose build

.PHONY: compose.build.nocache
compose.build.nocache:
	cd local/docker && docker-compose build --no-cache

.PHONY: compose.up
compose.up:
	cd local/docker && docker-compose up -d

.PHONY: compose.down
compose.down:
	cd local/docker && docker-compose down -v

.PHONY: compose.restart
compose.restart: compose.down compose.build compose.up

.PHONY: test
test:
	cd local/docker && docker-compose exec blog behave tests_behave/features
