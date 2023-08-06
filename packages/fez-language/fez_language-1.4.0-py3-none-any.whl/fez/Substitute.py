"""
Substitute
==========

Substitution rules are created using the ``Substitute`` verb. There are two
forms of this verb:

- a simple substitution, which simply has a number of glyph
  selectors on each side of an arrow (``->``)
- a contextual substitution, which wraps the main glyphs to be substituted in
  parentheses, and optionally surrounds them with prefix and/or suffix glyphs.

Examples::

    Substitute f i -> f_i;

    Substitute [CH_YEu1 BEu1] ( NUNu1 ) -> NUNf2;

Within the right hand side of a ``Substitute`` operation, you may use
*backreferences* as glyph selectors to refer to glyph selectors in equivalent
positions on the left hand side. For example, the following rule::

    Substitute [a e i o u] comma -> $1;

is equivalent to::

    Substitute [a e i o u] comma -> [a e i o u];

The ``ReverseSubstitute`` verb is equivalent but creates reverse chaining
substitution rules.

Substitution rules, as with any "basic" (substitute/position/attach/chain) rule,
can be optionally followed by a list of script/language pairs in double angle brackets::

    Substitute @letter (semicolon) -> space semicolon <<latn/FRA latn/DEU>>;

"""

import fontFeatures
from . import FEZVerb
import lark
from .util import extend_args_until

PARSEOPTS = dict(use_helpers=True)

# A different variable is used so Chain.py can import it and redefine pre/left/post/right
BASE_GRAMMAR = """
pre: glyphselector* // these two make sure they get grouped into a list
post: glyphselector*

dollar_gs: "$" DIGIT+ gs_suffixes
gs_suffixes: glyphsuffix*
"""

GRAMMAR = BASE_GRAMMAR+"""
normal_action: leftside "->" rightside languages?
contextual_action: pre "(" leftside ")" post "->" rightside languages?

leftside: (glyphselector WS)* glyphselector
rightside: (glyphselector WS| dollar_gs WS)* (glyphselector|dollar_gs)
"""

Substitute_GRAMMAR = """
?start: action
action: normal_action | contextual_action
"""

ReverseSubstitute_GRAMMAR = """
?start: action
action: normal_action
"""

VERBS = ["Substitute", "ReverseSubstitute"]

class Substitute(FEZVerb):
    def dollar_gs(self, args):
        (ref, suffixes) = args
        return {"reference": int(ref.value), "suffixes": suffixes}

    def leftside(self, args):
        return [t for t in args if not isinstance(t, lark.Token) or t.type != "WS"]

    rightside = leftside
    pre = leftside
    post = leftside

    gs_suffixes = leftside

    def languages(self, args):
        rv = []
        while args:
            rv.append(tuple(map((lambda x: "%-4s" % x),args[0:2])))
            args = args[2:]
        return rv

    def contextual_action(self, args):
        args = extend_args_until(args, 5)
        (pre, l, post, r, languages) = args
        args = [l, r, languages, pre, post]
        return args

    def normal_action(self, args):
        args = extend_args_until(args, 5)
        return args

    def action(self, args):
        (l, r, languages, pre, post) = args[0]
        inputs  = [g.resolve(self.parser.fontfeatures, self.parser.font) for g in l]
        pre     = [g.resolve(self.parser.fontfeatures, self.parser.font) for g in pre]
        post     = [g.resolve(self.parser.fontfeatures, self.parser.font) for g in post]
        for ix, output in enumerate(r):
        	if isinstance(output, dict):
        		r[ix] = l[output["reference"]-1]
        		if "suffixes" in output:
	        		r[ix].suffixes = output["suffixes"]
        outputs = [g.resolve(self.parser.fontfeatures, self.parser.font) for g in r]
        return [fontFeatures.Substitution(inputs, outputs,
            precontext = pre,
            postcontext = post,
            languages=languages)]

class ReverseSubstitute(Substitute):
    def action(self, args):
        (l, r, languages, _, _) = args[0]

        s = super().action([[l, r, languages, [], []]])
        s[0].reverse = True
        return s
