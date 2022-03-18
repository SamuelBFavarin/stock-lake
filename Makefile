####################### RUN CI #######################
.PHONY: run-ci
run-ci:
	@echo "RUN All Commands"
	@make tests-client-api
	@make flake-client-api
	@echo "RUN Spark Job"
	@make tests-spark-job
	@make flake-spark-job

####################### CLIENT API commands #######################
.PHONY: tests-client-api
tests-client-api:
	@echo ""
	@echo "Client API Unit Tests"
	@echo "====================="
	@echo ""
	@cd ./client_api_consumer; python -m pytest --import-mode=append

.PHONY: flake-client-api
flake-client-api:
	@echo ""
	@echo "Client API Flake8"
	@echo "=================="
	@echo ""
	@flake8 ./client_api_consumer --count --select=E9,F63,F7,F82 --show-source --statistics
	@flake8 ./client_api_consumer --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

####################### SPARK JOBS commands #######################
.PHONY: tests-spark-job
tests-spark-job:
	@echo ""
	@echo "Spark Job Unit Tests"
	@echo "====================="
	@echo ""
	@cd ./spark_job; python -m pytest --import-mode=append

.PHONY: flake-spark-job
flake-spark-job:
	@echo ""
	@echo "Spark Job Flake8"
	@echo "================"
	@echo ""
	@flake8 ./spark_job --count --select=E9,F63,F7,F82 --show-source --statistics
	@flake8 ./spark_job --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics