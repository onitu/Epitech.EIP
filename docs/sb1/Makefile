PDF = 2015_SB1_FR_onitu.pdf
TPL = tpl.tex
SRC =	scope_baseline.md
HEADER = print_json.tex
BEFORE = header.tex \
	tableau.tex

FLAGS = --template=$(TPL) $(HEADER:%=-H %) $(BEFORE:%=-B %)

DEPS = $(TPL) $(HEADER) $(BEFORE) commands.tex revisions.tex

GEN = $(PDF)

$(PDF):	$(SRC) $(DEPS)
	pandoc $(SRC) -o $@ $(FLAGS)

clean:
	rm -f $(GEN)

re:	clean $(GEN)

.PHONY:	clean re
