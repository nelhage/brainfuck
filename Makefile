quine.bf: gen.py tail.bf
	python gen.py

q.bf: quine.bf
	beef "$?" > "$@"

q1.bf: q.bf
	beef "$?" > "$@"

test: q.bf q1.bf
	@if cmp $^; then \
		echo "OK"; rm -f $^; \
	else\
		echo FAIL; exit 1; \
	fi
