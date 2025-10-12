package org.bettermaths.token.symbol;

import org.bettermaths.token.function.Params;
import org.bettermaths.result.Result;
import org.bettermaths.token.Token;

import java.util.LinkedList;
import java.util.Stack;

public abstract class Symbol implements Token {

    private final Identifier identifier;
    private final int priority;
    private final boolean supportUnary;

    public Symbol(Identifier identifier, int priority) {
        this(identifier, priority, false);
    }

    public Symbol(Identifier identifier, int priority, boolean supportUnary) {
        this.identifier = identifier;
        this.priority = priority;
        this.supportUnary = supportUnary;
    }

    public Identifier getIdentifier() {
        return identifier;
    }

    public int getPriority() {
        return priority;
    }

    public boolean supportUnary() {
        return supportUnary;
    }

    public Token[] getInjectedTokens(LinkedList<Token> previous, Token actualToken, LinkedList<Token> next) {
        return new Token[0];
    }

    public abstract Result<?> apply(Params params);

    @Override
    public String toString() {
        return "Symbol{" +
                "identifier=" + identifier +
                ", priority=" + priority +
                '}';
    }
}
