BF = beef

quine.bf: gen.py tail.bf
	python gen.py

q.bf: quine.bf
	$(BF) "$?" > "$@"

q1.bf: q.bf
	$(BF) "$?" > "$@"

test: q.bf q1.bf
	@if cmp $^; then \
		echo "OK"; \
		echo "$$(wc -c q.bf) bytes"; \
		rm -f $^; \
	else\
		echo FAIL; exit 1; \
	fi
