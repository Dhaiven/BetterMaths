package org.bettermaths.util;

import org.bettermaths.token.symbol.Symbol;
import org.bettermaths.token.symbol.delimiter.Delimiter;

import java.util.Comparator;
import java.util.List;

public class Utils {

    public static void sortSymbolsByLength(List<Symbol> symbols) {
        symbols.sort(Comparator.comparing(symbol -> symbol.getIdentifier().getSymbols().getFirst().length(), Comparator.reverseOrder()));
    }

    // utilitaire : renvoie l'indice après la delimiter fermant (ou -1 si pas trouvé)
    public static int getIndexForDelimiterClose(String s, int start, Delimiter delimiter) {
        int depth = 0;
        int i = start;
        while (i < s.length()) {
            if (s.startsWith(delimiter.getStart(), i)) {
                depth++;
                i += delimiter.getStart().length();
            } else if (s.startsWith(delimiter.getEnd(), i)) {
                depth--;
                i += delimiter.getEnd().length();
                if (depth == 0) {
                    return i;
                }
            } else {
                i++;
            }
        }

        return -1; // non équilibré
    }
}
