PDF = 2015_AA2_FR_onitu.pdf
TPL = tpl.tex
SRC = introduction.md taille_et_performance.md qualite.md
HEADER = resume.tex header.tex

FLAGS = --chapters --toc --template=$(TPL) $(HEADER:%=-B %)

FIGURES = $(wildcard figures/*)
DEPS = $(TPL) $(HEADER) $(FIGURES) commands.tex revisions.tex

GEN = $(PDF)

$(PDF):	$(SRC) $(DEPS)
	pandoc $(SRC) -o $@ $(FLAGS)

clean:
	rm -f $(GEN)

re:	clean $(GEN)

.PHONY:	clean re
