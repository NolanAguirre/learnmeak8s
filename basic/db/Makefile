# Usage:
#   make deploy                # Deploys to latest version in sqitch.plan
#   make deploy.<version>      # Deploys to a specific version (e.g., make deploy.1.000.0)
#   make revert                # Reverts the last change
#   make revert.<version>      # Reverts to a specific version (e.g., make revert.0.0.0)
#   make reset                 # Reverts all changes (resets to base)

SQITCH ?= sqitch

deploy:
	$(SQITCH) deploy --target localhost

deploy.%:
	$(SQITCH) deploy --to $* --target localhost

revert:
	$(SQITCH) revert --target localhost

revert.%:
	$(SQITCH) revert --to $* --target localhost

reset:
	$(SQITCH) revert --to @ROOT --target localhost

