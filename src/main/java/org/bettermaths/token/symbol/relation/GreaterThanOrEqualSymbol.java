package org.bettermaths.token.symbol.relation;

import org.bettermaths.result.ComparableResult;
import org.bettermaths.token.symbol.Identifier;

public class GreaterThanOrEqualSymbol extends RelationSymbol<ComparableResult<?>> {

    public GreaterThanOrEqualSymbol() {
        super(new Identifier(">="), 5, ComparableResult::isGreaterOrEqualThan);
    }
}