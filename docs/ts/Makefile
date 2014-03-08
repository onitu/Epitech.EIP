PDF = 2015_TS_FR_onitu.pdf
TPL = tpl.tex
SRC =	introduction.md \
	version.md \
	perimetre.md \
	livrables.md \
	risques.md \
	types_tests.md \
	estimation_charge.md \
	outils.md
HEADER = print_json.tex
BEFORE = resume.tex header.tex

FLAGS = --chapters --toc --template=$(TPL) $(HEADER:%=-H %) $(BEFORE:%=-B %)

DEPS = $(TPL) $(HEADER) $(BEFORE) commands.tex revisions.tex

GEN = $(PDF)

$(PDF):	$(SRC) $(DEPS)
	pandoc $(SRC) -o $@ $(FLAGS)

clean:
	rm -f $(GEN)

re:	clean $(GEN)

.PHONY:	clean re
