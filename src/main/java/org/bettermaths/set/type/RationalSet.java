package org.bettermaths.set.type;

import org.bettermaths.result.Result;
import org.bettermaths.result.primary.DoubleResult;
import org.bettermaths.set.Set;

public class RationalSet extends IntegersSet {

    @Override
    public boolean contains(Set other) {
        return other instanceof RationalSet;
    }
    
    @Override
    public boolean strictContains(Set other) {
        return other instanceof RationalSet && !this.equals(other);
    }

    @Override
    public boolean belongs(Result<?> other) {
        // TODO: just fractional result
        return other instanceof DoubleResult;
    }
}
