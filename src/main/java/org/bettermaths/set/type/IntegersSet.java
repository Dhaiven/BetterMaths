package org.bettermaths.set.type;

import org.bettermaths.result.Result;
import org.bettermaths.result.primary.IntegerResult;
import org.bettermaths.set.Set;

public class IntegersSet extends NaturalSet {

    @Override
    public boolean contains(Set other) {
        return other instanceof IntegersSet;
    }

    @Override
    public boolean strictContains(Set other) {
        return other instanceof IntegersSet && !this.equals(other);
    }

    @Override
    public boolean belongs(Result<?> other) {
        return other instanceof IntegerResult;
    }
}
