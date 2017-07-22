
usage:
	@echo
	@echo " dump_shop - prepare shop's app fixtures"
	@echo " load_shop - load shop's app fixtures"

dump_shop:
	@./manage.py dumpdata shop --indent 2 --output ./apps/shop/fixtures/shop.fixture.json

load_shop:
	@./manage.py loaddata ./apps/shop/fixtures/shop.fixture.json
