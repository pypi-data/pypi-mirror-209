import guidance

def test_basic():
    llm = guidance.llms.Transformers('gpt2', caching=False)
    with llm.session() as s:
        out = s("this is a test", max_tokens=5)
        print(out)

def test_repeat():
    llm = guidance.llms.Transformers('gpt2', caching=False)
    with llm.session() as s:
        out1 = s("this is a test", max_tokens=5)
        out2 = s("this is a test like another", max_tokens=5)
        print(out2)

def test_stop():
    llm = guidance.llms.Transformers('gpt2', caching=False)
    program = guidance("""Repeat this. Repeat this. Repeat this. Repeat this. Repeat this. Repeat this.{{gen stop="this" max_tokens=10}}""", llm=llm)
    out = program()
    assert str(out) == "Repeat this. Repeat this. Repeat this. Repeat this. Repeat this. Repeat this. Repeat "

def test_pattern():
    import re
    llm = guidance.llms.Transformers('gpt2', caching=False)
    program = guidance("""Repeat this. Repeat this. Repeat this. Repeat this. {{gen pattern="[0-9]+" max_tokens=1}}""", llm=llm)
    out = program()
    assert re.match("^Repeat this. Repeat this. Repeat this. Repeat this. [0-9]+$", str(out))

def test_select():
    llm = guidance.llms.Transformers('gpt2', caching=False)
    program = guidance('''Answer "yes" or "no": "{{#select 'answer'}}yes{{or}}no{{/select}}"''', llm=llm)
    out = program()
    assert out["answer"] in ["yes", "no"]