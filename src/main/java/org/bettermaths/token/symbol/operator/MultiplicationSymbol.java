package org.bettermaths.token.symbol.operator;

import org.bettermaths.token.Token;
import org.bettermaths.token.Tokenizer;
import org.bettermaths.token.function.Function;
import org.bettermaths.token.function.Params;
import org.bettermaths.result.OperationalResult;
import org.bettermaths.result.Result;
import org.bettermaths.token.symbol.Identifier;
import org.bettermaths.token.symbol.Symbol;

import java.util.LinkedList;

public class MultiplicationSymbol extends Symbol {

    public MultiplicationSymbol() {
        super(new Identifier("*"), 3);
    }

    @Override
    public Token[] getInjectedTokens(LinkedList<Token> previous, Token actualToken, LinkedList<Token> next) {
        var needInjection = !previous.isEmpty() && previous.peek() instanceof Result<?> && (actualToken instanceof Function || actualToken instanceof Tokenizer.StartDelimiter);
        return needInjection ? new Token[] { new MultiplicationSymbol() } : new Token[0];
    }

    @Override
    public Result<?> apply(Params params) {
        OperationalResult<?> result = params.get(0);
        for (int i = 1; i < params.size(); i++) {
            result = result.pow(params.get(i));
        }

        return result;
    }
}
