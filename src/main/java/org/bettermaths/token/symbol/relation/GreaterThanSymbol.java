package org.bettermaths.token.symbol.relation;

import org.bettermaths.result.ComparableResult;
import org.bettermaths.token.symbol.Identifier;

public class GreaterThanSymbol extends RelationSymbol<ComparableResult<?>> {

    public GreaterThanSymbol() {
        super(new Identifier(">"), 5, ComparableResult::isGreaterThan);
    }
}