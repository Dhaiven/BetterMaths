package org.bettermaths.token;

import org.bettermaths.result.custom.ErrorResult;
import org.bettermaths.token.function.Function;
import org.bettermaths.token.function.FunctionsManager;
import org.bettermaths.token.function.Params;
import org.bettermaths.result.Result;
import org.bettermaths.result.ResultManager;
import org.bettermaths.token.symbol.delimiter.Delimiter;
import org.bettermaths.token.symbol.delimiter.DelimitersManager;
import org.bettermaths.token.symbol.Symbol;
import org.bettermaths.token.symbol.SymbolsManager;
import org.bettermaths.token.symbol.WordManager;
import org.bettermaths.util.Utils;

import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Tokenizer {

    private final List<Symbol> symbols = new ArrayList<>();
    private final List<Function> functions = new ArrayList<>();
    private final List<String> words;

    public Tokenizer(Collection<String> extraWords) {
        symbols.addAll(SymbolsManager.allSorted());
        functions.addAll(FunctionsManager.all().values());

        var words = new HashSet<>(WordManager.allWords());
        if (extraWords != null) words.addAll(extraWords);
        this.words = words.stream()
                .sorted(Comparator.comparing(String::length, Comparator.reverseOrder()))
                .toList();
    }

    public Tokenizer() {
        this(null);
    }

    public void register(Symbol symbol) {
        symbols.add(symbol);
    }

    public void register(Function function) {
        functions.add(function);
    }

    public Result<?> evaluate(String expression) {
        List<Token> tokens = tokenize(expression);
        var normalized = normalize(tokens);
        List<Token> postfix = toPostfix(normalized);
        return evaluatePostfix(postfix);
    }

    // ----------------------------
    // Tokenisation
    // ----------------------------
    private List<Token> tokenize(String expr) {
        List<Token> tokens = new ArrayList<>();
        int i = 0;

        while (i < expr.length()) {
            boolean matched = false;
            Token currentToken = null;

            for (Symbol symbol : symbols) {
                String s = symbol.getIdentifier().getStartsWithAny(expr, i);
                if (s != null) {
                    currentToken = symbol;
                    i += s.length();
                    matched = true;
                    break;
                }
            }

            if (!matched) {
                for (Function function : functions) {
                    String name = function.getName();
                    String delimStart = function.getDelimiter().getStart();
                    if (expr.startsWith(name + delimStart, i)) {
                        currentToken = new StartDelimiter(function.getDelimiter(), function);
                        i += name.length() + delimStart.length();
                        matched = true;
                        break;
                    }
                }
            }

            if (!matched) {
                for (Delimiter delimiter : DelimitersManager.all().values()) {
                    if (expr.startsWith(delimiter.getStart(), i)) {
                        int closeIdx = Utils.getIndexForDelimiterClose(expr, i, delimiter);
                        if (closeIdx != -1) {
                            String candidate = expr.substring(i, closeIdx);
                            var pr = ResultManager.get(candidate);
                            if (!(pr instanceof ErrorResult)) {
                                currentToken = pr;
                                i += candidate.length();
                                matched = true;
                            }
                        }

                        if (!matched) {
                            currentToken = new StartDelimiter(delimiter);
                            i += delimiter.getStart().length();
                            matched = true;
                        }
                        break;
                    } else if (expr.startsWith(delimiter.getEnd(), i)) {
                        currentToken = new EndDelimiter(delimiter);
                        i += delimiter.getEnd().length();
                        matched = true;
                        break;
                    }
                }
            }

            if (!matched) {
                int end = expr.length();
                Result<?> result;

                while (end > i) {
                    String candidate = expr.substring(i, end);
                    result = ResultManager.get(candidate);
                    if (result != null && !(result instanceof ErrorResult)) {
                        currentToken = result;
                        i = end;
                        matched = true;
                        break;
                    }
                    end--;
                }
            }

            if (!matched) {
                for (Function function : functions) {
                    if (function.getSeparator() == null) continue;
                    for (String sep : function.getSeparator().getSymbols()) {
                        if (expr.startsWith(sep, i)) {
                            currentToken = new FunctionSeparatorToken();
                            i += sep.length();
                            matched = true;
                            break;
                        }
                    }
                    if (matched) break;
                }
            }
            if (!matched) {
                for (String word : words) {
                    if (expr.startsWith(word, i)) {
                        currentToken = ResultManager.get(word);
                        i += word.length();
                        matched = true;
                        break;
                    }
                }
            }
            if (!matched) {
                Matcher numberMatcher = Pattern.compile("\\G\\d+(?:\\.\\d+)?").matcher(expr);
                numberMatcher.region(i, expr.length());
                if (numberMatcher.lookingAt()) {
                    String number = numberMatcher.group();
                    currentToken = ResultManager.get(number);
                    i += number.length();
                    matched = true;
                }
            }
            if (!matched) {
                if (expr.charAt(i) == ' ') {
                    i++;
                    continue;
                }
            }

            if (!matched) {
                throw new IllegalArgumentException("Token inconnu à la position " + i + " : " + expr.charAt(i));
            }

            if (currentToken != null) {
                tokens.add(currentToken);
            }
        }

        return tokens;
    }

    private List<Token> normalize(List<Token> tokens) {
        List<Token> normalized = new ArrayList<>();
        LinkedList<Token> previous = new LinkedList<>();
        LinkedList<Token> next = new LinkedList<>(tokens);

        while (!next.isEmpty()) {
            Token actualToken = next.pollFirst();

            // Vérifie si un symbole veut injecter des tokens
            for (Symbol symbol : symbols) {
                List<Token> injected = List.of(symbol.getInjectedTokens(previous, actualToken, next));
                if (!injected.isEmpty()) {
                    normalized.addAll(injected);
                    break;
                }
            }

            normalized.add(actualToken);
            previous.addFirst(actualToken);
        }

        return normalized;
    }

    // ----------------------------
    // Conversion infix → postfix
    // ----------------------------
    private List<Token> toPostfix(List<Token> tokens) {
        List<Token> output = new ArrayList<>();
        Deque<Token> stack = new ArrayDeque<>();
        Token previous = null;

        for (Token token : tokens) {
            if (token instanceof Result) {
                output.add(token);
            } else if (token instanceof Symbol symbol) {
                boolean isUnary = symbol.supportUnary() &&
                        (previous == null || previous instanceof Symbol || previous instanceof StartDelimiter);

                if (isUnary) {
                    symbol = new UnarySymbolProxy(symbol);
                } else {
                    while (!stack.isEmpty() && stack.peek() instanceof Symbol peekSymbol && (
                            peekSymbol instanceof UnarySymbolProxy || peekSymbol.getPriority() >= symbol.getPriority()
                    )) {
                        output.add(stack.pop());
                    }
                }

                stack.push(symbol);
            } else if (token instanceof StartDelimiter start) {
                stack.push(start);
            } else if (token instanceof EndDelimiter) {
                // Récupère tout jusqu’à la parenthèse ouvrante
                List<Token> popped = new ArrayList<>();
                while (!stack.isEmpty() && !(stack.peek() instanceof StartDelimiter)) {
                    popped.add(stack.pop());
                }

                if (stack.isEmpty()) {
                    throw new IllegalStateException("Parenthèse fermante sans ouvrante correspondante.");
                }

                StartDelimiter start = (StartDelimiter) stack.pop();

                if (start.isFunctionDelimiter()) {
                    Function f = start.getFunction();

                    // Compte directement les arguments tout en ajoutant au flux de sortie
                    int argCount = 1;
                    for (int i = popped.size() - 1; i >= 0; i--) {
                        Token t = popped.get(i);
                        if (t instanceof FunctionSeparatorToken) {
                            argCount++;
                        } else {
                            output.add(t);
                        }
                    }

                    output.add(new FunctionCall(f, argCount));
                } else {
                    output.addAll(popped);
                }
            } else if (token instanceof FunctionSeparatorToken) {
                stack.push(token);
            }

            previous = token;
        }

        while (!stack.isEmpty()) {
            output.add(stack.pop());
        }

        return output;
    }

    // ----------------------------
    // Évaluation postfixée
    // ----------------------------
    private Result<?> evaluatePostfix(List<Token> postfix) {
        Deque<Result<?>> stack = new ArrayDeque<>();

        for (Token token : postfix) {
            switch (token) {
                case Result<?> r -> stack.push(r);
                case Symbol symbol -> {
                    Params params = new Params();
                    if (symbol instanceof UnarySymbolProxy) {
                        params.add(stack.pop());
                    } else {
                        Result<?> b = stack.pop();
                        Result<?> a = stack.pop();
                        params.add(a);
                        params.add(b);
                    }
                    stack.push(symbol.apply(params));
                }
                case FunctionCall(Function function, int argCount) -> {
                    Deque<Result<?>> tmp = new ArrayDeque<>();
                    for (int i = 0; i < argCount; i++) tmp.addFirst(stack.pop());
                    Params params = new Params();
                    for (Result<?> rr : tmp) params.add(rr);
                    stack.push(function.onExecute(params));
                }
                default -> throw new IllegalStateException("Token postfix inattendu: " + token);
            }
        }

        if (stack.isEmpty()) throw new IllegalStateException("Expression invalide : pile vide après évaluation");
        return stack.pop();
    }

    private static class UnarySymbolProxy extends Symbol {
        private final Symbol base;

        public UnarySymbolProxy(Symbol base) {
            super(base.getIdentifier(), base.getPriority(), base.supportUnary());
            this.base = base;
        }

        @Override
        public Result<?> apply(Params params) {
            return base.apply(params);
        }
    }

    private record FunctionCall(Function function, int argCount) implements Token { }

    public static class StartDelimiter extends Delimiter {
        private final Function function;

        public StartDelimiter(Delimiter delimiter) {
            super(delimiter.getStart(), delimiter.getEnd());
            this.function = null;
        }

        public StartDelimiter(Delimiter delimiter, Function function) {
            super(delimiter.getStart(), delimiter.getEnd());
            this.function = function;
        }

        public boolean isFunctionDelimiter() {
            return function != null;
        }

        public Function getFunction() {
            return function;
        }
    }

    public static class EndDelimiter extends Delimiter {
        public EndDelimiter(Delimiter delimiter) {
            super(delimiter.getStart(), delimiter.getEnd());
        }
    }

    private static class FunctionSeparatorToken implements Token { }

}
