PDF = 2015_UD1_FR_onitu.pdf
TPL = tpl.tex
SRC =	presentation.md \
	installation.md \
	configuration.md \
	infos.md
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
