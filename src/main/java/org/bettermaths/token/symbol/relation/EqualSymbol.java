package org.bettermaths.token.symbol.relation;

import org.bettermaths.result.primary.BooleanResult;
import org.bettermaths.token.Token;
import org.bettermaths.token.function.Params;
import org.bettermaths.token.symbol.Identifier;
import org.bettermaths.token.symbol.Symbol;
import org.bettermaths.token.symbol.operator.AndSymbol;

import java.util.LinkedList;
import java.util.Objects;

public class EqualSymbol extends Symbol {

    public EqualSymbol() {
        super(new Identifier("="), 0);
    }

    @Override
    public Token[] getInjectedTokens(LinkedList<Token> previous, Token actualToken, LinkedList<Token> next) {
        if (!(actualToken instanceof RelationSymbol) || previous.isEmpty()) return new Token[0];

        var lastToken = previous.peek();
        while (!previous.isEmpty() && !(previous.peek() instanceof Symbol)) {
            previous.pop();
        }

        if (!previous.isEmpty()) {
            Symbol lastSymbol = (Symbol) previous.peek();
            if (lastSymbol instanceof RelationSymbol<?>) {
                return new Token[] { new AndSymbol(), lastToken };
            }
        }

        return new Token[0];
    }

    @Override
    public BooleanResult apply(Params params) {
        for (int i = 0; i < params.size() - 1; i++) {
            if (!Objects.equals(params.get(i), params.get(i + 1))) {
                return BooleanResult.FALSE;
            }
        }

        return BooleanResult.TRUE;
    }
}