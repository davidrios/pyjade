from pyjade.lexer import Lexer
from pyjade.utils import odict

expected_results = {
    "p Here is some #[strong: em text] and look at #[a(href='http://google.com') this link!]": [
        {'buffer': None, 'line': 1, 'type': 'tag', 'val': u'p'},
        {'buffer': None, 'line': 1, 'type': 'text', 'val': u' Here is some '},
        {'buffer': None, 'type': 'tag', 'line': 1, 'insert_inline': True, 'val': u'strong'},
        {'buffer': None, 'type': ':', 'line': 1, 'insert_inline': True, 'val': None},
        {'buffer': None, 'type': 'tag', 'line': 1, 'insert_inline': True, 'val': u'em'},
        {'buffer': None, 'type': 'text', 'line': 1, 'insert_inline': True, 'val': u' text'},
        {'buffer': None, 'line': 1, 'type': 'text', 'val': u' and look at '},
        {'buffer': None, 'insert_inline': True, 'line': 1, 'type': 'tag', 'val': u'a'},
        {'insert_inline': True, 'val': None, 'buffer': None, 'static_attrs': set([u'href']), 'attrs': odict([(u'href', u"'http://google.com'")]), 'line': 1, 'type': 'attrs'},
        {'buffer': None, 'insert_inline': True, 'line': 1, 'type': 'text', 'val': u' this link!'},
        {'buffer': None, 'line': 1, 'type': 'text', 'val': u''}],

    "p Other inline #[strong= 'test']": [
        {'buffer': None, 'line': 1, 'type': 'tag', 'val': u'p'},
        {'buffer': None, 'line': 1, 'type': 'text', 'val': u' Other inline '},
        {'buffer': None, 'type': 'tag', 'line': 1, 'insert_inline': True, 'val': u'strong'},
        {'insert_inline': True, 'val': u" 'test'", 'buffer': True, 'escape': True, 'line': 1, 'type': 'code'},
        {'buffer': None, 'line': 1, 'type': 'text', 'val': u''}],

    "p Test #[|text line]": [
        {'buffer': None, 'line': 1, 'type': 'tag', 'val': u'p'},
        {'buffer': None, 'line': 1, 'type': 'text', 'val': u' Test '},
        {'buffer': None, 'type': 'string', 'line': 1, 'insert_inline': True, 'val': u'text line'},
        {'buffer': None, 'line': 1, 'type': 'text', 'val': u''}],

    "p Test buffered #[= map(str, zip('iln', 'nie')) + 'code']": [
        {'buffer': None, 'line': 1, 'type': 'tag', 'val': u'p'},
        {'buffer': None, 'line': 1, 'type': 'text', 'val': u' Test buffered '},
        {'insert_inline': True, 'val': u" map(str, zip('iln', 'nie')) + 'code'", 'buffer': True, 'escape': True, 'line': 1, 'type': 'code'},
        {'buffer': None, 'line': 1, 'type': 'text', 'val': u''}],

    "p #[- abcf = [[123, [[],[]], []],'abc']] #[= abcf]": [
        {'buffer': None, 'line': 1, 'type': 'tag', 'val': u'p'},
        {'buffer': None, 'line': 1, 'type': 'text', 'val': u' '},
        {'insert_inline': True, 'val': u" abcf = [[123, [[],[]], []],'abc']", 'buffer': False, 'escape': False, 'line': 1, 'type': 'code'},
        {'buffer': None, 'line': 1, 'type': 'text', 'val': u' '},
        {'insert_inline': True, 'val': u' abcf', 'buffer': True, 'escape': True, 'line': 1, 'type': 'code'},
        {'buffer': None, 'line': 1, 'type': 'text', 'val': u''}],

    "#[#[#[a a#[b #[i a] b]] d]e]": [
        {'buffer': None, 'line': 1, 'type': 'text', 'val': u''},
        {'buffer': None, 'type': 'text', 'line': 1, 'insert_inline': True, 'val': u''},
        {'buffer': None, 'type': 'text', 'line': 1, 'insert_inline': True, 'val': u''},
        {'buffer': None, 'type': 'tag', 'line': 1, 'insert_inline': True, 'val': u'a'},
        {'buffer': None, 'type': 'text', 'line': 1, 'insert_inline': True, 'val': u' a'},
        {'buffer': None, 'type': 'tag', 'line': 1, 'insert_inline': True, 'val': u'b'},
        {'buffer': None, 'type': 'text', 'line': 1, 'insert_inline': True, 'val': u' '},
        {'buffer': None, 'type': 'tag', 'line': 1, 'insert_inline': True, 'val': u'i'},
        {'buffer': None, 'type': 'text', 'line': 1, 'insert_inline': True, 'val': u' a'},
        {'buffer': None, 'type': 'text', 'line': 1, 'insert_inline': True, 'val': u' b'},
        {'buffer': None, 'type': 'text', 'line': 1, 'insert_inline': True, 'val': u''},
        {'buffer': None, 'type': 'text', 'line': 1, 'insert_inline': True, 'val': u' d'},
        {'buffer': None, 'type': 'text', 'line': 1, 'insert_inline': True, 'val': u'e'},
        {'buffer': None, 'line': 1, 'type': 'text', 'val': u''}],

    "p We can also #[strong combine #[em multiple #[img(src='http://jade-lang.com/style/logo.png')]]]": [
        {'buffer': None, 'line': 1, 'type': 'tag', 'val': u'p'},
        {'buffer': None, 'line': 1, 'type': 'text', 'val': u' We can also '},
        {'buffer': None, 'type': 'tag', 'line': 1, 'insert_inline': True, 'val': u'strong'},
        {'buffer': None, 'type': 'text', 'line': 1, 'insert_inline': True, 'val': u' combine '},
        {'buffer': None, 'type': 'tag', 'line': 1, 'insert_inline': True, 'val': u'em'},
        {'buffer': None, 'type': 'text', 'line': 1, 'insert_inline': True, 'val': u' multiple '},
        {'buffer': None, 'type': 'tag', 'line': 1, 'insert_inline': True, 'val': u'img'},
        {'insert_inline': True, 'val': None, 'buffer': None, 'static_attrs': set([u'src']), 'attrs': odict([(u'src', u"'http://jade-lang.com/style/logo.png'")]), 'line': 1, 'type': 'attrs'},
        {'buffer': None, 'type': 'text', 'line': 1, 'insert_inline': True, 'val': u''},
        {'buffer': None, 'type': 'text', 'line': 1, 'insert_inline': True, 'val': u''},
        {'buffer': None, 'line': 1, 'type': 'text', 'val': u''}],

    "#[strong start] line with #[i]\#[j] inline": [
        {'buffer': None, 'line': 1, 'type': 'text', 'val': u''},
        {'buffer': None, 'type': 'tag', 'line': 1, 'insert_inline': True, 'val': u'strong'},
        {'buffer': None, 'type': 'text', 'line': 1, 'insert_inline': True, 'val': u' start'},
        {'buffer': None, 'line': 1, 'type': 'text', 'val': u' line with '},
        {'buffer': None, 'type': 'tag', 'line': 1, 'insert_inline': True, 'val': u'i'},
        {'buffer': None, 'line': 1, 'type': 'text', 'val': u'#[j] inline'}],

    "p Another #[strong.lil#okf(acs=[1,2]) test [[with brackets]] [in#[='side']]]": [
        {'buffer': None, 'line': 1, 'type': 'tag', 'val': u'p'},
        {'buffer': None, 'line': 1, 'type': 'text', 'val': u' Another '},
        {'buffer': None, 'type': 'tag', 'line': 1, 'insert_inline': True, 'val': u'strong'},
        {'buffer': None, 'type': 'class', 'line': 1, 'insert_inline': True, 'val': u'lil'},
        {'buffer': None, 'type': 'id', 'line': 1, 'insert_inline': True, 'val': u'okf'},
        {'val': None, 'buffer': None, 'static_attrs': set([]), 'attrs': odict([(u'acs', u'[1,2]')]), 'line': 1, 'type': 'attrs', 'insert_inline': True},
        {'buffer': None, 'type': 'text', 'line': 1, 'insert_inline': True, 'val': u' test [[with brackets]] [in'},
        {'insert_inline': True, 'val': u"'side'", 'buffer': True, 'escape': True, 'line': 1, 'type': 'code'},
        {'buffer': None, 'type': 'text', 'line': 1, 'insert_inline': True, 'val': u']'},
        {'buffer': None, 'line': 1, 'type': 'text', 'val': u''}],

    """mixin lala(a, b)
  span lala(#{a}, #{b})
p Test inline mixin #[+lala(123, 'lala inside inline')] end""": [
        {'args': u'a, b', 'buffer': None, 'line': 1, 'type': 'mixin', 'val': u'lala'},
        {'buffer': None, 'line': 2, 'type': 'indent', 'val': 2},
        {'buffer': None, 'line': 2, 'type': 'tag', 'val': u'span'},
        {'buffer': None, 'line': 2, 'type': 'text', 'val': u' lala(#{a}, #{b})'},
        {'buffer': None, 'line': 3, 'type': 'outdent', 'val': None},
        {'buffer': None, 'line': 3, 'type': 'tag', 'val': u'p'},
        {'buffer': None, 'line': 3, 'type': 'text', 'val': u' Test inline mixin '},
        {'insert_inline': True, 'val': u'lala', 'buffer': None, 'args': u"123, 'lala inside inline'", 'line': 1, 'type': 'call'},
        {'buffer': None, 'line': 3, 'type': 'text', 'val': u' end'}],

    "p only class #[.strong: em inline]": [
        {'buffer': None, 'line': 1, 'type': 'tag', 'val': u'p'},
        {'buffer': None, 'line': 1, 'type': 'text', 'val': u' only class '},
        {'buffer': None, 'insert_inline': True, 'line': 1, 'type': 'class', 'val': u'strong'},
        {'buffer': None, 'insert_inline': True, 'line': 1, 'type': ':', 'val': None},
        {'buffer': None, 'insert_inline': True, 'line': 1, 'type': 'tag', 'val': u'em'},
        {'buffer': None, 'insert_inline': True, 'line': 1, 'type': 'text', 'val': u' inline'},
        {'buffer': None, 'line': 1, 'type': 'text', 'val': u''}],

    "#[asdf.lol(fff)#[asdf]]": [
        {'buffer': None, 'line': 1, 'type': 'text', 'val': u''},
        {'buffer': None, 'insert_inline': True, 'line': 1, 'type': 'tag', 'val': u'asdf'},
        {'buffer': None, 'insert_inline': True, 'line': 1, 'type': 'class', 'val': u'lol'},
        {'insert_inline': True, 'val': None, 'buffer': None, 'static_attrs': set([u'fff']), 'attrs': odict([(u'fff', True)]), 'line': 1, 'type': 'attrs'},
        {'buffer': None, 'insert_inline': True, 'line': 1, 'type': 'text', 'val': u''},
        {'buffer': None, 'insert_inline': True, 'line': 1, 'type': 'tag', 'val': u'asdf'},
        {'buffer': None, 'insert_inline': True, 'line': 1, 'type': 'text', 'val': u''},
        {'buffer': None, 'line': 1, 'type': 'text', 'val': u''}],

    "#[= '[[[[[[[[[[']": [
        {'buffer': None, 'line': 1, 'type': 'text', 'val': u''},
        {'buffer': True, 'line': 1, 'type': 'code', 'val': u" '[[[[[[[[[['", 'escape': True, 'insert_inline': True},
        {'buffer': None, 'line': 1, 'type': 'text', 'val': u''}],

    "#[= ']]]]]]]]]]']": [
        {'buffer': None, 'line': 1, 'type': 'text', 'val': u''},
        {'buffer': True, 'line': 1, 'type': 'code', 'val': u" ']]]]]]]]]]'", 'escape': True, 'insert_inline': True},
        {'buffer': None, 'line': 1, 'type': 'text', 'val': u''}],
}


def generate_expected(jade):
    lx = Lexer(jade)
    res = []
    while True:
        tok = lx.advance()
        if tok.type == 'eos':
            break
        res.append(tok.__dict__)
    return res


def process(jade):
    assert expected_results[jade] == generate_expected(jade)


def test_lexer():
    for k, v in expected_results.iteritems():
        yield process, k
