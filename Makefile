.PHONY: help
help:  ## Show this help.
	@egrep '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-22s\033[0m %s\n", $$1, $$2}'

.PHONY: run
run:  ## Run the application.
	docker compose up

.PHONY: stop
stop:  ## Stop the application
	docker compose stop

.PHONY: clean
clean:  ## Clean up.
	docker compose rm -fsv