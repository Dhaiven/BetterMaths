package org.bettermaths.token.symbol.operator;

import org.bettermaths.result.primary.BooleanResult;
import org.bettermaths.token.function.Params;
import org.bettermaths.token.symbol.Identifier;
import org.bettermaths.token.symbol.Symbol;

public class OrSymbol extends Symbol {

    public OrSymbol() {
        super(new Identifier("||", "or"), 4);
    }

    @Override
    public BooleanResult apply(Params params) {
        for (BooleanResult result : params.values(BooleanResult.class)) {
            if (result.get()) {
                return BooleanResult.TRUE;
            }
        }

        return BooleanResult.FALSE;
    }
}