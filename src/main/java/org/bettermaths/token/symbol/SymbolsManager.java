package org.bettermaths.token.symbol;

import org.bettermaths.token.function.SumFunction;
import org.bettermaths.result.ComparableResult;
import org.bettermaths.token.symbol.operator.AndSymbol;
import org.bettermaths.token.symbol.operator.DivisionSymbol;
import org.bettermaths.token.symbol.operator.MultiplicationSymbol;
import org.bettermaths.token.symbol.operator.SubtractionSymbol;
import org.bettermaths.token.symbol.relation.EqualSymbol;
import org.bettermaths.token.symbol.relation.RelationSymbol;

import java.util.*;

public class SymbolsManager {

    private static boolean isInitialized = false;

    private static final List<Symbol> sortedSymbols = new ArrayList<>();
    private static final Map<Identifier, Symbol> symbols = new HashMap<>();

    public static void init() {
        if (isInitialized) {
            throw new RuntimeException("Symbols already initialized");
        }
        isInitialized = true;

        add(new AliasFunctionSymbol(new Identifier("+"), 1, true, new SumFunction()));
        add(new SubtractionSymbol());
        add(new MultiplicationSymbol());
        add(new DivisionSymbol());

        add(new AndSymbol());

        add(new EqualSymbol());
        add(new RelationSymbol<ComparableResult<?>>(new Identifier(">"), ComparableResult::isGreaterThan));
        add(new RelationSymbol<ComparableResult<?>>(new Identifier(">="), ComparableResult::isGreaterOrEqualThan));
        add(new RelationSymbol<ComparableResult<?>>(new Identifier("<"), ComparableResult::isSmallerThan));
        add(new RelationSymbol<ComparableResult<?>>(new Identifier("<="), ComparableResult::isSmallerOrEqualThan));
    }

    public static Map<Identifier, Symbol> all() {
        if (!isInitialized) {
            init();
        }

        return symbols;
    }

    public static List<Symbol> allSorted() {
        if (!isInitialized) {
            init();
        }

        return sortedSymbols;
    }

    public static Symbol get(Identifier identifier) {
        if (!isInitialized) {
            init();
        }

        return symbols.get(identifier);
    }

    public static Symbol get(String symbol) {
        if (!isInitialized) {
            init();
        }

        for (Identifier identifier : symbols.keySet()) {
            if (identifier.getFindId(symbol) != null) {
                return symbols.get(identifier);
            }
        }

        return null;
    }

    public static void add(Symbol symbol) {
        symbols.put(symbol.getIdentifier(), symbol);
        sortSymbols();
    }

    public static void remove(String symbol) {
        for (Identifier identifier : symbols.keySet()) {
            if (identifier.getFindId(symbol) != null) {
                symbols.remove(identifier);
                sortSymbols();
                break;
            }
        }
    }

    private static void sortSymbols() {
        var sortedSymbolByPriority = symbols.values().stream().sorted(Comparator.comparing(Symbol::getPriority));
        sortedSymbols.clear();

        var iterator = sortedSymbolByPriority.iterator();
        List<Symbol> tempSortedSymbol = new ArrayList<>();

        var tempPriority = Long.MIN_VALUE;
        while (iterator.hasNext()) {
            var next = iterator.next();
            if (next.getPriority() > tempPriority) {
                sortSymbolsByLength(tempSortedSymbol);
                sortedSymbols.addAll(tempSortedSymbol);
                tempSortedSymbol.clear();
                tempPriority = next.getPriority();
            }

            tempSortedSymbol.add(next);
        }

        sortSymbolsByLength(tempSortedSymbol);
        sortedSymbols.addAll(tempSortedSymbol);
    }

    private static void sortSymbolsByLength(List<Symbol> symbols) {
        // Take first element because identifier sort symbols by String::length
        symbols.sort(Comparator.comparing(symbol -> symbol.getIdentifier().getSymbols().getFirst().length(), Comparator.reverseOrder()));
    }
}
