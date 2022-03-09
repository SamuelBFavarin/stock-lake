####################### PYTHON commands #######################
.PHONY: tests-client-api
tests-client-api:
	@echo ""
	@echo "Client API Unit Tests"
	@echo "=========="
	@echo ""
	@export PYTHONPATH=./client_api_consumer; pytest

.PHONY: flake-client-api
flake-client-api:
	@echo ""
	@echo "Client API Flake8"
	@echo "=========="
	@echo ""
	@flake8 ./client_api_consumer --count --select=E9,F63,F7,F82 --show-source --statistics
	@flake8 ./client_api_consumer --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics