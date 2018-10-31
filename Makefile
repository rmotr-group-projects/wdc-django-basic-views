.PHONY: runserver shell

TAG="\n\n\033[0;32m\#\#\# "
END=" \#\#\# \033[0m\n"

HOST=0.0.0.0
PORT=8080
PYTHONPATH=django_basic_views
DJANGO_SETTINGS=django_basic_views.settings

# django-command = django-admin $(1) $(HOST):$(PORT) --settings $(DJANGO_SETTINGS) --pythonpath $(PYTHONPATH)
django-command = django-admin $(1) $(2) --settings $(DJANGO_SETTINGS) --pythonpath $(PYTHONPATH)

runserver:
	@echo $(TAG)Running Server $(END)
	$(call django-command, runserver, $(HOST):$(PORT))

shell:
	@echo $(TAG)Running Shell $(END)
	$(call django-command, shell)

test:
	@echo $(TAG)Testing$(END)
	$(call django-command, test django_basic_views)
