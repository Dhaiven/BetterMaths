package org.bettermaths.token.symbol.operator;

import org.bettermaths.token.function.Params;
import org.bettermaths.result.primary.BooleanResult;
import org.bettermaths.token.symbol.Identifier;
import org.bettermaths.token.symbol.Symbol;

public class AndSymbol extends Symbol {

    public AndSymbol() {
        super(new Identifier("&&", "and"), 4);
    }

    @Override
    public BooleanResult apply(Params params) {
        for (BooleanResult result : params.values(BooleanResult.class)) {
            if (!result.get()) {
                return BooleanResult.FALSE;
            }
        }

        return BooleanResult.TRUE;
    }
}
