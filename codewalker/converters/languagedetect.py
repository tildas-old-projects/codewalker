def detect(lang: str or int):
    """
    Tries to assume what language a user wants using limited input. May be wrong sometimes.

    Arguments:

    lang (str/int) - A language name or language ID.
    """
    # note: this is a generalized thing
    if type(lang) == str:
        lang = lang.lower()
    elif type(lang) == int:
        return lang
    elif lang == 'c':
        return 4
    elif lang == 'bash':
        return 1
    elif lang == 'cpp' or 'c++':
        return 10
    elif lang == 'csharp' or 'c#':
        return 16
    elif lang == 'clojure' or 'clj':
        return 18
    elif lang == 'crystal':
        return 19
    elif lang == 'elixir':
        return 20
    elif lang == 'erlang':
        return 21
    elif lang == 'go':
        return 22
    elif lang == 'haskell':
        return 23
    elif lang == 'insect':
        return 25
    elif lang == 'java':
        # I would've returned 26, but there are some things that dont work well with OpenJ9
        # plus Java 8 works with basically anything anyways
        return 27
    elif lang == 'js' or 'javascript':
        return 29
    elif lang == 'ocaml':
        return 31
    elif lang == 'octave':
        return 32
    elif lang == 'pascal':
        return 33
    elif lang == 'python' or 'py':
        return 34
    elif lang == 'ruby':
        return 38
    elif lang == 'rust':
        return 42