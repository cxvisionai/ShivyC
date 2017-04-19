"""The token kinds currently recognized."""

from tokens import TokenKind

keyword_kinds = []
symbol_kinds = []

# Until function definition is ready, we define `main` as a hardcoded keyword
main = TokenKind("main", keyword_kinds)

bool_kw = TokenKind("_Bool", keyword_kinds)
char_kw = TokenKind("char", keyword_kinds)
short_kw = TokenKind("short", keyword_kinds)
int_kw = TokenKind("int", keyword_kinds)
long_kw = TokenKind("long", keyword_kinds)
signed_kw = TokenKind("signed", keyword_kinds)
unsigned_kw = TokenKind("unsigned", keyword_kinds)
void_kw = TokenKind("void", keyword_kinds)

return_kw = TokenKind("return", keyword_kinds)
if_kw = TokenKind("if", keyword_kinds)
while_kw = TokenKind("while", keyword_kinds)

auto_kw = TokenKind("auto", keyword_kinds)
static_kw = TokenKind("static", keyword_kinds)
extern_kw = TokenKind("extern", keyword_kinds)

plus = TokenKind("+", symbol_kinds)
star = TokenKind("*", symbol_kinds)
slash = TokenKind("/", symbol_kinds)
equals = TokenKind("=", symbol_kinds)
twoequals = TokenKind("==", symbol_kinds)
notequal = TokenKind("!=", symbol_kinds)
amp = TokenKind("&", symbol_kinds)

dquote = TokenKind('"', symbol_kinds)

open_paren = TokenKind("(", symbol_kinds)
close_paren = TokenKind(")", symbol_kinds)
open_brack = TokenKind("{", symbol_kinds)
close_brack = TokenKind("}", symbol_kinds)
open_sq_brack = TokenKind("[", symbol_kinds)
close_sq_brack = TokenKind("]", symbol_kinds)

comma = TokenKind(",", symbol_kinds)
semicolon = TokenKind(";", symbol_kinds)

identifier = TokenKind()
number = TokenKind()
string = TokenKind()
