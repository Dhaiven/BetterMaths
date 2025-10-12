package org.bettermaths.token.symbol;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;

public class Identifier {

    private final List<String> symbols = new ArrayList<>();

    public Identifier(String symbol, String... symbols) {
        this.symbols.add(symbol);
        this.symbols.addAll(Arrays.asList(symbols));
        this.symbols.sort(Comparator.comparing(String::length, Comparator.reverseOrder()));
    }

    public List<String> getSymbols() {
        return symbols;
    }

    /**
     * Vérifie si l'expression commence par l'un des symboles de cet Identifier à la position donnée.
     * @param expr L'expression complète.
     * @param pos La position de départ.
     * @return le symbole correspondant, ou null si aucun ne correspond.
     */
    public String getStartsWithAny(String expr, int pos) {
        for (String s : symbols) {
            if (expr.startsWith(s, pos)) {
                return s;
            }
        }

        return null;
    }

    public String getFindId(String expression) {
        for (String id : symbols) {
            if (expression.contains(id)) {
                // If length is 1, we need to add "\\" to resolve error during split operation
                if (id.length() > 1) {
                    return id;
                }
                return "\\" + id;
            }
        }

        return null;
    }

    @Override
    public String toString() {
        return "Identifier{" +
                "symbols=" + symbols +
                '}';
    }
}
