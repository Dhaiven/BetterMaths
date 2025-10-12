package org.bettermaths.token.symbol.delimiter;

import org.bettermaths.token.Token;

public class Delimiter implements Token {

    private final String start;
    private final String end;

    public Delimiter(String start, String end) {
        this.start = start;
        this.end = end;
    }

    public String getStart() {
        return start;
    }

    public String getEnd() {
        return end;
    }
}
