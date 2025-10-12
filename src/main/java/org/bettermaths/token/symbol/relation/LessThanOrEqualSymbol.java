package org.bettermaths.token.symbol.relation;

import org.bettermaths.result.ComparableResult;
import org.bettermaths.token.symbol.Identifier;

public class LessThanOrEqualSymbol extends RelationSymbol<ComparableResult<?>> {

    public LessThanOrEqualSymbol() {
        super(new Identifier("<="), 5, ComparableResult::isLessOrEqualThan);
    }
}