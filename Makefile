.PHONY:  install help update-cursor-rules

help:
	@echo "Available commands:"
	@echo "  install                Install dependencies and update cursor rules"
	@echo "  update-cursor-rules    Update the .cursorrules file from the remote repository"
	@echo "  help                   Show this help message"


install:
	$(MAKE) update-cursor-rules

update-cursor-rules:
	git clone --depth 1 git@github.com:NolanAguirre/cursor-rules.git /tmp/cursor-rules && cp /tmp/cursor-rules/.cursorrules .cursorrules && rm -rf /tmp/cursor-rules
