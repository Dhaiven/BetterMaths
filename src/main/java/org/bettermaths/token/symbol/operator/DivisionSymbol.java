package org.bettermaths.token.symbol.operator;

import org.bettermaths.token.function.Params;
import org.bettermaths.result.OperationalResult;
import org.bettermaths.result.Result;
import org.bettermaths.token.symbol.Identifier;
import org.bettermaths.token.symbol.Symbol;

public class DivisionSymbol extends Symbol {

    public DivisionSymbol() {
        super(new Identifier("/"), 3);
    }

    @Override
    public Result<?> apply(Params params) {
        OperationalResult<?> result = params.get(0);
        for (int i = 1; i < params.size(); i++) {
            result = result.div(params.get(i));
        }

        return result;
    }
}
