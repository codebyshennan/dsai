.PHONY: clean build build-all-slides prep all data-fundamentals python stats linear-algebra pandas regenerate clean-module

# Build slides for 0-prep + module 1 (data fundamentals) only
build: prep data-fundamentals

# Rebuild every submodule that has slides/data.json
build-all-slides:
	@echo "Building all slide decks..."
	@for f in $$(find . -path '*/slides/data.json' -type f); do \
		moddir=$$(dirname $$(dirname "$$f")); \
		echo " -> $$moddir"; \
		node slides/build.js "$$moddir" || exit 1; \
	done

# Build preparation slides
prep:
	@echo "Building preparation slides..."
	@node slides/build.js 0-prep

# Build data fundamentals slides
data-fundamentals: data-analytics python stats linear-algebra pandas

# Build individual module slides
data-analytics:
	@echo "Building data analytics slides..."
	@node slides/build.js 1-data-fundamentals/1.1-intro-data-analytics

python:
	@echo "Building Python slides..."
	@node slides/build.js 1-data-fundamentals/1.2-intro-python

stats:
	@echo "Building statistics slides..."
	@node slides/build.js 1-data-fundamentals/1.3-intro-statistics

linear-algebra:
	@echo "Building linear algebra slides..."
	@node slides/build.js 1-data-fundamentals/1.4-data-foundation-linear-algebra

pandas:
	@echo "Building pandas slides..."
	@node slides/build.js 1-data-fundamentals/1.5-data-analysis-pandas

# Clean generated slide HTML only (not other index.html files)
clean:
	@echo "Cleaning generated slide index.html files..."
	@find . -path '*/slides/index.html' -type f -delete

# Clean specific module
clean-module:
	@echo "Cleaning specific module..."
	@if [ -z "$(MODULE)" ]; then \
		echo "Error: MODULE variable not set. Usage: make clean-module MODULE=module-name"; \
		exit 1; \
	fi
	@find . -path "*/$(MODULE)/*" -type f -name "index.html" -delete

# Regenerate specific module (MODULE = path under docs/, e.g. 2-data-wrangling/2.1-sql)
regenerate:
	@echo "Regenerating specific module..."
	@if [ -z "$(MODULE)" ]; then \
		echo "Error: MODULE variable not set. Example: make regenerate MODULE=2-data-wrangling/2.1-sql"; \
		exit 1; \
	fi
	@$(MAKE) clean-module MODULE=$(MODULE)
	@node slides/build.js $(MODULE)

# Default target
all: build 
