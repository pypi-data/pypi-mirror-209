# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SPHINXAPIDOC  ?= sphinx-apidoc
SOURCEDIR     = source
BUILDDIR      = "../build/doc"
ROOTDIR       = "../"
MODULE_PATH   = "../sknrf/"

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

api:
	@$(SPHINXAPIDOC) --force --separate -o "$(SOURCEDIR)/api" "$(MODULE_PATH)" $(ROOTDIR)/sknrf/tutorial $(ROOTDIR)/tests $(ROOTDIR)/*/tests $(ROOTDIR)/*/*/tests $(ROOTDIR)/*/*/*/tests $(ROOTDIR)/*/*/*/*/tests $(ROOTDIR)/*/*/*/*/*/tests

.PHONY: api

html:
	mkdir -p $(BUILDDIR)/html
	rsync -a --delete $(SOURCEDIR)/_images/ $(BUILDDIR)/html/_images/
	@$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: html

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
