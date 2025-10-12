package org.bettermaths.result.custom;

import org.bettermaths.result.Result;
import org.bettermaths.result.ResultManager;
import org.bettermaths.token.symbol.delimiter.Delimiter;
import org.bettermaths.token.symbol.delimiter.DelimitersManager;
import org.bettermaths.util.Utils;

import java.util.*;

public class UpletResult implements Result<Result<?>> {

    public static UpletResult from(final Object o) {
        if (!(o instanceof String stringObject)) return null;
        stringObject = stringObject.trim();

        if (!stringObject.startsWith("(") || !stringObject.endsWith(")")) return null;

        stringObject = stringObject.substring(1, stringObject.length() - 1).trim();

        List<Object> parts = new ArrayList<>();
        StringBuilder current = new StringBuilder();

        int i = 0;
        while (i < stringObject.length()) {
            boolean jumped = false;

            // Vérifie si on rencontre un délimiteur d'ouverture
            for (Delimiter delimiter : DelimitersManager.all().values()) {
                if (stringObject.startsWith(delimiter.getStart(), i)) {
                    int closeIndex = Utils.getIndexForDelimiterClose(stringObject, i, delimiter);
                    if (closeIndex == -1) {
                        throw new IllegalArgumentException("Délimiteurs non équilibrés : " + stringObject);
                    }

                    // Ajoute le bloc complet sans le découper
                    current.append(stringObject, i, closeIndex);
                    i = closeIndex;
                    jumped = true;
                    break;
                }
            }

            if (jumped) continue;

            char c = stringObject.charAt(i);

            if (c == ',') {
                // Virgule de premier niveau → séparation
                parts.add(current.toString().trim());
                current.setLength(0);
            } else {
                current.append(c);
            }

            i++;
        }

        /**
         * Si part est vide, c'est a dire il n'y a pas de virgule donc ce n'est pas un uplet
         * TODO: uplet avec 1 élément ?
         */
        if (parts.isEmpty()) {
            return null;
        }

        // Ajoute le dernier élément
        if (!current.isEmpty()) {
            parts.add(current.toString().trim());
        }

        return new UpletResult(parts);
    }

    private final List<Result<?>> collection;

    public UpletResult(Collection<Object> results) {
        List<Result<?>> result = new ArrayList<>();
        for (Object o : results) {
            if (o instanceof Result<?> result1) {
                result.add(result1);
            } else {
                result.add(ResultManager.get(o, Result.class));
            }
        }

        this.collection = result;
    }

    public UpletResult(Result<?> ...results) {
        this.collection = List.of(results);
    }

    public int size() {
        return this.collection.size();
    }

    @Override
    public Result<?> get() {
        return this;
    }

    public Result<?> getResult(int index) {
        return collection.get(index);
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (!(obj instanceof UpletResult other)) return false;
        if (this.size() != other.size()) return false;
        for (int i = 0; i < this.size(); i++) {
            if (!Objects.equals(this.getResult(i), other.getResult(i))) {
                return false;
            }
        }

        return true;
    }

    @Override
    public int hashCode() {
        return Objects.hash(collection);
    }

    @Override
    public String toString() {
        StringJoiner joiner = new StringJoiner(", ", "(", ")");
        for (Result<?> result : collection) {
            joiner.add(result.toString());
        }
        return joiner.toString();
    }
}
