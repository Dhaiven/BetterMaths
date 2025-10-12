package org.bettermaths.token.symbol.operator;

import org.bettermaths.result.primary.BooleanResult;
import org.bettermaths.token.function.Params;
import org.bettermaths.token.symbol.Identifier;
import org.bettermaths.token.symbol.Symbol;

public class XorSymbol extends Symbol {

    public XorSymbol() {
        super(new Identifier("xor"), 4);
    }

    @Override
    public BooleanResult apply(Params params) {
        return ((BooleanResult) params.get(0)).xor(params.get(1));
    }
}
