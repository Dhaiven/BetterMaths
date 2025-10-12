package org.bettermaths.token.symbol.operator;

import org.bettermaths.token.function.Params;
import org.bettermaths.result.OperationalResult;
import org.bettermaths.result.Result;
import org.bettermaths.token.symbol.Identifier;
import org.bettermaths.token.symbol.Symbol;

public class SubtractionSymbol extends Symbol {

    public SubtractionSymbol() {
        super(new Identifier("-"), 1, true);
    }

    @Override
    public Result<?> apply(Params params) {
        if (params.size() == 1) {
            var first = (OperationalResult<?>) params.get(0);
            System.out.println("first: " + first);
            return first.invert();
        }

        OperationalResult<?> result = params.get(0);
        for (int i = 1; i < params.size(); i++) {
            result = result.subtract(params.get(i));
        }

        return result;
    }
}
